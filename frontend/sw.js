/**
 * Rural Siksha Service Worker
 * Provides offline support by caching app shell and API responses
 */

const CACHE_VERSION = 'rural-siksha-v25';
const APP_SHELL_CACHE = `${CACHE_VERSION}-shell`;
const API_CACHE = `${CACHE_VERSION}-api`;
const RESOURCE_CACHE = `${CACHE_VERSION}-resources`;

// App shell files - cached on install
const APP_SHELL = [
    '/',
    '/static/css/style.css',
    '/static/js/api.js',
    '/static/js/utils.js',
    '/static/js/offline.js',
    '/static/js/auth.js',
    '/static/js/resources.js',
    '/static/js/quizzes.js',
    '/static/js/doubts.js',
    '/static/js/ai-tutor.js',
    '/static/js/progress.js',
    '/static/js/app.js',
    '/static/manifest.json',
    'https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap'
];

// API endpoints to cache for offline access
const CACHEABLE_API_PATTERNS = [
    /\/api\/resources/,
    /\/api\/quizzes/,
    /\/api\/progress/,
    /\/api\/auth\/me/
];

/**
 * Install event - cache app shell
 */
self.addEventListener('install', event => {
    console.log('[SW] Installing...');
    event.waitUntil(
        caches.open(APP_SHELL_CACHE)
            .then(cache => {
                console.log('[SW] Caching app shell');
                return cache.addAll(APP_SHELL.filter(url => !url.startsWith('http')));
            })
            .then(() => {
                console.log('[SW] App shell cached');
                return self.skipWaiting();
            })
            .catch(err => console.error('[SW] Install failed:', err))
    );
});

/**
 * Activate event - clean up old caches
 */
self.addEventListener('activate', event => {
    console.log('[SW] Activating...');
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(name => !name.startsWith(CACHE_VERSION))
                    .map(name => {
                        console.log('[SW] Deleting old cache:', name);
                        return caches.delete(name);
                    })
            );
        }).then(() => self.clients.claim())
    );
});

/**
 * Fetch event - serve from cache or network
 */
self.addEventListener('fetch', event => {
    const url = new URL(event.request.url);

    // SKIP Ollama requests - let them pass through directly
    if (url.hostname === 'localhost' && url.port === '11434') {
        return; // Don't intercept Ollama calls
    }

    // Skip non-GET requests for caching
    if (event.request.method !== 'GET') {
        // For POST/PUT/DELETE - try network only
        event.respondWith(
            fetch(event.request).catch(err => {
                console.log('[SW] Network failed for', event.request.method, url.pathname);
                return new Response(JSON.stringify({
                    error: 'You are offline. Action will be retried when online.',
                    offline: true
                }), {
                    status: 503,
                    headers: { 'Content-Type': 'application/json' }
                });
            })
        );
        return;
    }

    // Cache-first for PDF downloads (resources and papers)
    if (url.pathname.includes('/download') && url.pathname.startsWith('/api/')) {
        event.respondWith(cacheFirstStrategy(event.request));
        return;
    }

    // Network-first for API requests, fallback to cache
    if (url.pathname.startsWith('/api/')) {
        // Health check - always go to network
        if (url.pathname === '/api/health' || url.pathname.includes('ai-status')) {
            event.respondWith(
                fetch(event.request).catch(() =>
                    new Response(JSON.stringify({
                        status: 'offline',
                        details: { database: false, ollama: false }
                    }), { headers: { 'Content-Type': 'application/json' } })
                )
            );
            return;
        }

        event.respondWith(networkFirstStrategy(event.request));
        return;
    }

    // Cache-first for app shell and static assets
    event.respondWith(cacheFirstStrategy(event.request));
});

/**
 * Network-first strategy: try network, fallback to cache
 */
async function networkFirstStrategy(request) {
    const cache = await caches.open(API_CACHE);

    try {
        const networkResponse = await fetch(request);

        // Cache successful responses
        if (networkResponse.ok) {
            // Clone before caching (response can only be used once)
            cache.put(request, networkResponse.clone());
        }

        return networkResponse;
    } catch (err) {
        console.log('[SW] Network failed, trying cache for:', request.url);
        const cachedResponse = await cache.match(request);

        if (cachedResponse) {
            console.log('[SW] Serving from cache:', request.url);
            return cachedResponse;
        }

        // Return offline indicator response
        return new Response(JSON.stringify({
            error: 'You are offline and this content is not cached.',
            offline: true,
            data: []
        }), {
            status: 503,
            headers: { 'Content-Type': 'application/json' }
        });
    }
}

/**
 * Cache-first strategy: try cache, fallback to network
 */
async function cacheFirstStrategy(request) {
    const cache = await caches.open(APP_SHELL_CACHE);
    const cachedResponse = await cache.match(request);

    if (cachedResponse) {
        // Update cache in background
        fetch(request).then(networkResponse => {
            if (networkResponse.ok) {
                cache.put(request, networkResponse);
            }
        }).catch(() => {});

        return cachedResponse;
    }

    try {
        const networkResponse = await fetch(request);

        if (networkResponse.ok) {
            cache.put(request, networkResponse.clone());
        }

        return networkResponse;
    } catch (err) {
        // For navigation requests, return the cached index page
        if (request.mode === 'navigate') {
            return cache.match('/');
        }

        return new Response('Offline - content not available', {
            status: 503,
            headers: { 'Content-Type': 'text/plain' }
        });
    }
}

/**
 * Background sync for queued requests
 */
self.addEventListener('sync', event => {
    console.log('[SW] Background sync:', event.tag);

    if (event.tag === 'sync-doubts') {
        event.waitUntil(syncDoubts());
    } else if (event.tag === 'sync-quiz-answers') {
        event.waitUntil(syncQuizAnswers());
    }
});

async function syncDoubts() {
    // Get queued doubts from IndexedDB and send to server
    console.log('[SW] Syncing queued doubts');
}

async function syncQuizAnswers() {
    console.log('[SW] Syncing queued quiz answers');
}

/**
 * Message handler for client communication
 */
self.addEventListener('message', event => {
    if (event.data && event.data.type === 'SKIP_WAITING') {
        self.skipWaiting();
    }

    if (event.data && event.data.type === 'CACHE_RESOURCES') {
        cacheResources(event.data.resources);
    }
});

async function cacheResources(resources) {
    const cache = await caches.open(RESOURCE_CACHE);
    for (const url of resources) {
        try {
            await cache.add(url);
        } catch (e) {
            console.log('[SW] Failed to cache:', url);
        }
    }
}

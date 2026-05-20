/**
 * Offline support using IndexedDB
 * Handles caching and sync queue
 */

const offlineDB = {
    dbName: 'RuralSiksha',
    version: 1,
    db: null,

    /**
     * Initialize IndexedDB
     */
    async init() {
        return new Promise((resolve, reject) => {
            const request = indexedDB.open(this.dbName, this.version);

            request.onerror = () => reject(request.error);
            request.onsuccess = () => {
                this.db = request.result;
                resolve(this.db);
            };

            request.onupgradeneeded = (e) => {
                const db = e.target.result;

                // Cache storage
                if (!db.objectStoreNames.contains('cache')) {
                    db.createObjectStore('cache', { keyPath: 'endpoint' });
                }

                // Sync queue for offline changes
                if (!db.objectStoreNames.contains('syncQueue')) {
                    db.createObjectStore('syncQueue', { keyPath: 'id', autoIncrement: true });
                }

                // Offline quiz answers
                if (!db.objectStoreNames.contains('quizAnswers')) {
                    db.createObjectStore('quizAnswers', { keyPath: 'id', autoIncrement: true });
                }

                // Offline doubts (draft)
                if (!db.objectStoreNames.contains('draftDoubts')) {
                    db.createObjectStore('draftDoubts', { keyPath: 'id', autoIncrement: true });
                }
            };
        });
    },

    /**
     * Cache GET response
     */
    async cache(endpoint, data) {
        if (!this.db) return;
        const tx = this.db.transaction(['cache'], 'readwrite');
        const store = tx.objectStore('cache');
        await store.put({
            endpoint,
            data,
            timestamp: Date.now()
        });
    },

    /**
     * Get cached data
     */
    async getCached(endpoint) {
        if (!this.db) return null;
        return new Promise((resolve, reject) => {
            const tx = this.db.transaction(['cache'], 'readonly');
            const store = tx.objectStore('cache');
            const request = store.get(endpoint);

            request.onerror = () => reject(request.error);
            request.onsuccess = () => resolve(request.result?.data || null);
        });
    },

    /**
     * Add request to sync queue
     */
    async addToSyncQueue(item) {
        if (!this.db) return;
        const tx = this.db.transaction(['syncQueue'], 'readwrite');
        const store = tx.objectStore('syncQueue');
        return store.add(item);
    },

    /**
     * Get all pending sync items
     */
    async getPendingSync() {
        if (!this.db) return [];
        return new Promise((resolve, reject) => {
            const tx = this.db.transaction(['syncQueue'], 'readonly');
            const store = tx.objectStore('syncQueue');
            const request = store.getAll();

            request.onerror = () => reject(request.error);
            request.onsuccess = () => resolve(request.result);
        });
    },

    /**
     * Remove item from sync queue
     */
    async removeSyncQueue(id) {
        if (!this.db) return;
        const tx = this.db.transaction(['syncQueue'], 'readwrite');
        const store = tx.objectStore('syncQueue');
        return store.delete(id);
    },

    /**
     * Sync pending changes when online
     */
    async syncPending() {
        if (!navigator.onLine) return;

        const items = await this.getPendingSync();
        for (const item of items) {
            try {
                const result = await API.request(item.method, item.endpoint, item.data);
                if (result && !result.queued) {
                    await this.removeSyncQueue(item.id);
                    console.log(`Synced: ${item.method} ${item.endpoint}`);
                }
            } catch (error) {
                console.error(`Sync failed for ${item.endpoint}:`, error);
                // Will retry on next online event
            }
        }
    },

    /**
     * Save quiz answers locally
     */
    async saveQuizAnswers(quizId, answers) {
        if (!this.db) return;
        const tx = this.db.transaction(['quizAnswers'], 'readwrite');
        const store = tx.objectStore('quizAnswers');
        return store.add({
            quizId,
            answers,
            timestamp: Date.now()
        });
    },

    /**
     * Get quiz answers locally
     */
    async getQuizAnswers(quizId) {
        if (!this.db) return null;
        return new Promise((resolve, reject) => {
            const tx = this.db.transaction(['quizAnswers'], 'readonly');
            const store = tx.objectStore('quizAnswers');
            const index = store.index('quizId');
            const request = index.get(quizId);

            request.onerror = () => reject(request.error);
            request.onsuccess = () => resolve(request.result || null);
        });
    },

    /**
     * Save draft doubt
     */
    async saveDraftDoubt(doubt) {
        if (!this.db) return;
        const tx = this.db.transaction(['draftDoubts'], 'readwrite');
        const store = tx.objectStore('draftDoubts');
        return store.add({
            ...doubt,
            timestamp: Date.now()
        });
    },

    /**
     * Get draft doubts
     */
    async getDraftDoubts() {
        if (!this.db) return [];
        return new Promise((resolve, reject) => {
            const tx = this.db.transaction(['draftDoubts'], 'readonly');
            const store = tx.objectStore('draftDoubts');
            const request = store.getAll();

            request.onerror = () => reject(request.error);
            request.onsuccess = () => resolve(request.result);
        });
    },

    /**
     * Clear all data (on logout)
     */
    async clear() {
        if (!this.db) return;
        const stores = ['cache', 'syncQueue', 'quizAnswers', 'draftDoubts'];
        for (const storeName of stores) {
            const tx = this.db.transaction([storeName], 'readwrite');
            const store = tx.objectStore(storeName);
            store.clear();
        }
    }
};

// Initialize on page load
document.addEventListener('DOMContentLoaded', async () => {
    try {
        await offlineDB.init();
        console.log('Offline DB initialized');

        // Sync pending changes periodically when online
        setInterval(() => {
            if (navigator.onLine) {
                offlineDB.syncPending();
            }
        }, 30000);
    } catch (error) {
        console.warn('IndexedDB not available:', error);
    }
});

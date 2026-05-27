/**
 * Pro UI - Professional toast notifications, loading states, and animations
 */

/**
 * Pro Toast Notifications - Replace browser alert()
 */
class ToastManager {
    constructor() {
        this.container = null;
        this.init();
    }

    init() {
        if (document.getElementById('toastContainer')) return;
        const container = document.createElement('div');
        container.id = 'toastContainer';
        container.className = 'toast-container';
        document.body.appendChild(container);
        this.container = container;
    }

    show(message, type = 'info', duration = 3500) {
        if (!this.container) this.init();

        const icons = {
            success: '✅',
            error: '❌',
            warning: '⚠️',
            info: 'ℹ️',
            loading: '⏳'
        };

        const toast = document.createElement('div');
        toast.className = `pro-toast pro-toast-${type}`;
        toast.innerHTML = `
            <div class="toast-icon">${icons[type] || icons.info}</div>
            <div class="toast-content">${message}</div>
            <button class="toast-close" onclick="this.parentElement.remove()">×</button>
        `;

        this.container.appendChild(toast);

        // Trigger animation
        setTimeout(() => toast.classList.add('show'), 10);

        // Auto-dismiss
        if (duration > 0) {
            setTimeout(() => {
                toast.classList.remove('show');
                setTimeout(() => toast.remove(), 300);
            }, duration);
        }

        return toast;
    }

    success(message, duration = 3500) {
        return this.show(message, 'success', duration);
    }

    error(message, duration = 5000) {
        return this.show(message, 'error', duration);
    }

    warning(message, duration = 4000) {
        return this.show(message, 'warning', duration);
    }

    info(message, duration = 3500) {
        return this.show(message, 'info', duration);
    }

    loading(message) {
        return this.show(message, 'loading', 0);
    }
}

const toast = new ToastManager();

/**
 * Pro confirm dialog - Replace browser confirm()
 */
function proConfirm(message, title = 'Confirm') {
    return new Promise((resolve) => {
        const overlay = document.createElement('div');
        overlay.className = 'pro-confirm-overlay';
        overlay.innerHTML = `
            <div class="pro-confirm-dialog">
                <h3>${title}</h3>
                <p>${message}</p>
                <div class="pro-confirm-buttons">
                    <button class="btn btn-secondary" id="confirmCancel">Cancel</button>
                    <button class="btn btn-primary" id="confirmOk">OK</button>
                </div>
            </div>
        `;
        document.body.appendChild(overlay);

        setTimeout(() => overlay.classList.add('show'), 10);

        const cleanup = () => {
            overlay.classList.remove('show');
            setTimeout(() => overlay.remove(), 300);
        };

        overlay.querySelector('#confirmCancel').onclick = () => {
            cleanup();
            resolve(false);
        };

        overlay.querySelector('#confirmOk').onclick = () => {
            cleanup();
            resolve(true);
        };
    });
}

/**
 * Pro Splash Screen with progress
 */
function showSplashScreen() {
    if (document.getElementById('splashScreen')) return;

    const splash = document.createElement('div');
    splash.id = 'splashScreen';
    splash.className = 'splash-screen';
    splash.innerHTML = `
        <div class="splash-content">
            <div class="splash-logo">🎓</div>
            <h1 class="splash-title">Rural Siksha</h1>
            <p class="splash-tagline">Empowering Rural Education with AI</p>
            <div class="splash-loader">
                <div class="splash-loader-bar"></div>
            </div>
            <p class="splash-status">Loading...</p>
        </div>
    `;
    document.body.appendChild(splash);

    // Auto-hide after page loads
    setTimeout(() => {
        splash.classList.add('fade-out');
        setTimeout(() => splash.remove(), 500);
    }, 1500);
}

/**
 * Skeleton Loader Generator
 */
function createSkeletonCard() {
    return `
        <div class="skeleton-card">
            <div class="skeleton-header"></div>
            <div class="skeleton-line"></div>
            <div class="skeleton-line short"></div>
            <div class="skeleton-buttons">
                <div class="skeleton-button"></div>
                <div class="skeleton-button"></div>
            </div>
        </div>
    `;
}

function showSkeletonLoader(containerId, count = 6) {
    const container = document.getElementById(containerId);
    if (container) {
        container.innerHTML = Array(count).fill(0).map(() => createSkeletonCard()).join('');
    }
}

/**
 * Smooth scroll to top
 */
function scrollToTop() {
    window.scrollTo({top: 0, behavior: 'smooth'});
}

/**
 * Add back-to-top button
 */
function addBackToTopButton() {
    if (document.getElementById('backToTop')) return;

    const btn = document.createElement('button');
    btn.id = 'backToTop';
    btn.className = 'back-to-top';
    btn.innerHTML = '↑';
    btn.title = 'Back to top';
    btn.onclick = scrollToTop;
    document.body.appendChild(btn);

    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            btn.classList.add('show');
        } else {
            btn.classList.remove('show');
        }
    });
}

/**
 * Connection status notifier
 */
function setupConnectionNotifier() {
    window.addEventListener('online', () => {
        toast.success('You are back online!');
    });

    window.addEventListener('offline', () => {
        toast.warning('You are offline. Some features may not work.');
    });
}

/**
 * Add tooltips to elements with data-tooltip
 */
function setupTooltips() {
    document.addEventListener('mouseover', (e) => {
        const el = e.target.closest('[data-tooltip]');
        if (!el) return;

        const existing = document.querySelector('.pro-tooltip');
        if (existing) existing.remove();

        const tooltip = document.createElement('div');
        tooltip.className = 'pro-tooltip';
        tooltip.textContent = el.dataset.tooltip;
        document.body.appendChild(tooltip);

        const rect = el.getBoundingClientRect();
        tooltip.style.left = rect.left + rect.width/2 - tooltip.offsetWidth/2 + 'px';
        tooltip.style.top = rect.bottom + 5 + 'px';

        setTimeout(() => tooltip.classList.add('show'), 10);
    });

    document.addEventListener('mouseout', (e) => {
        if (e.target.closest('[data-tooltip]')) {
            const tooltip = document.querySelector('.pro-tooltip');
            if (tooltip) {
                tooltip.classList.remove('show');
                setTimeout(() => tooltip.remove(), 200);
            }
        }
    });
}

// Override Utils.showSuccess with pro toast
if (typeof Utils !== 'undefined') {
    const originalShow = Utils.showSuccess;
    Utils.showSuccess = function(message) {
        toast.success(message);
    };
}

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', () => {
    showSplashScreen();
    addBackToTopButton();
    setupConnectionNotifier();
    setupTooltips();
});

// Replace alert globally
window.alert = function(msg) {
    toast.info(msg);
};

/**
 * Utility functions
 */

const Utils = {
    /**
     * Format date to readable format
     */
    formatDate: (date) => {
        if (!date) return '';
        const d = new Date(date);
        return d.toLocaleDateString() + ' ' + d.toLocaleTimeString();
    },

    /**
     * Format file size in human-readable format
     */
    formatFileSize: (bytes) => {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return Math.round((bytes / Math.pow(k, i)) * 100) / 100 + ' ' + sizes[i];
    },

    /**
     * Debounce function
     */
    debounce: (func, wait) => {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },

    /**
     * Show error message
     */
    showError: (elementId, message) => {
        const el = document.getElementById(elementId);
        if (el) {
            el.textContent = message;
            el.style.display = 'block';
        }
    },

    /**
     * Clear error message
     */
    clearError: (elementId) => {
        const el = document.getElementById(elementId);
        if (el) {
            el.textContent = '';
            el.style.display = 'none';
        }
    },

    /**
     * Show success message temporarily
     */
    showSuccess: (message, duration = 3000) => {
        const div = document.createElement('div');
        div.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: #2ecc71;
            color: white;
            padding: 15px 20px;
            border-radius: 4px;
            z-index: 9999;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        `;
        div.textContent = message;
        document.body.appendChild(div);
        setTimeout(() => div.remove(), duration);
    },

    /**
     * Get current user from localStorage
     */
    getCurrentUser: () => {
        const user = localStorage.getItem('currentUser');
        return user ? JSON.parse(user) : null;
    },

    /**
     * Set current user in localStorage
     */
    setCurrentUser: (user) => {
        localStorage.setItem('currentUser', JSON.stringify(user));
    },

    /**
     * Clear current user
     */
    clearCurrentUser: () => {
        localStorage.removeItem('currentUser');
    },

    /**
     * Check if online
     */
    isOnline: () => navigator.onLine,

    /**
     * Truncate text with ellipsis
     */
    truncate: (text, length = 100) => {
        return text.length > length ? text.substring(0, length) + '...' : text;
    },

    /**
     * Check if user is student
     */
    isStudent: () => {
        const user = Utils.getCurrentUser();
        return user && user.role === 'student';
    },

    /**
     * Check if user is teacher
     */
    isTeacher: () => {
        const user = Utils.getCurrentUser();
        return user && user.role === 'teacher';
    }
};

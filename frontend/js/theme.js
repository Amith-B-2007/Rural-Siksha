/**
 * Dark/Light Theme Toggle
 */

function getCurrentTheme() {
    return localStorage.getItem('theme') || 'light';
}

function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    updateThemeIcon();
}

function toggleTheme() {
    const current = getCurrentTheme();
    setTheme(current === 'light' ? 'dark' : 'light');
}

function updateThemeIcon() {
    const btn = document.getElementById('themeToggle');
    if (btn) {
        const theme = getCurrentTheme();
        btn.innerHTML = theme === 'dark' ? '☀️' : '🌙';
        btn.title = theme === 'dark' ? 'Switch to Light Mode' : 'Switch to Dark Mode';
    }
}

// Apply theme on load
document.addEventListener('DOMContentLoaded', () => {
    setTheme(getCurrentTheme());
    updateThemeIcon();
});

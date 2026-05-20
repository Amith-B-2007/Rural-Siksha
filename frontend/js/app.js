/**
 * Main app initialization and routing
 */

/**
 * Get the currently selected viewing grade
 */
function getCurrentViewingGrade() {
    const user = Utils.getCurrentUser();
    if (!user) return null;

    // Teachers: no grade restriction
    if (user.role === 'teacher') return null;

    // Students: use selector value or default to their grade
    const selector = document.getElementById('viewingGrade');
    if (selector && selector.value) {
        return parseInt(selector.value);
    }
    return user.gradeLevel;
}

/**
 * Switch active panel
 */
function switchPanel(panelId, navBtn) {
    document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));

    const panel = document.getElementById(panelId);
    if (panel) panel.classList.add('active');
    if (navBtn) navBtn.classList.add('active');
}

/**
 * Navigate to a panel directly (used by home page cards)
 */
function goToPanel(panelId) {
    console.log('Navigating to panel:', panelId);

    // Hide all panels
    document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));

    // Show target panel
    const panel = document.getElementById(panelId);
    if (panel) {
        panel.classList.add('active');

        // Load appropriate data
        if (panelId === 'doubtsPanel') {
            const askSection = document.getElementById('askDoubtSection');
            if (askSection && Utils.isStudent()) {
                askSection.classList.remove('hidden');
            }
            if (typeof checkAiStatus === 'function') checkAiStatus();
            if (typeof loadDoubts === 'function') loadDoubts();
        } else if (panelId === 'careerPanel') {
            if (typeof showCareerPaths === 'function') showCareerPaths();
        } else if (panelId === 'progressPanel') {
            if (typeof loadProgress === 'function') loadProgress();
        } else if (panelId === 'toolsPanel') {
            if (typeof showCalculator === 'function') showCalculator();
        }

        // Scroll to top
        window.scrollTo({top: 0, behavior: 'smooth'});
    } else {
        console.error('Panel not found:', panelId);
    }
}

/**
 * Load dashboard for current user
 */
async function loadDashboard() {
    const user = Utils.getCurrentUser();
    if (!user) return;

    // Setup logout button FIRST (works for all roles)
    const logoutBtn = document.getElementById('logoutBtn');
    if (logoutBtn) {
        // Remove any old handler first to avoid duplicates
        logoutBtn.onclick = null;
        logoutBtn.onclick = function(e) {
            e.preventDefault();
            handleLogout();
        };
    }

    // Show user info in navbar
    const userInfo = document.getElementById('userInfo');
    if (userInfo) {
        const roleText = user.role === 'student' ? `Grade ${user.gradeLevel}` :
                         user.role === 'teacher' ? user.subject :
                         user.role === 'parent' ? 'Parent Account' : '';
        userInfo.innerHTML = `👤 ${user.fullName}<br><small>${roleText}</small>`;
    }

    // Show grade selector for students
    const gradeSelector = document.getElementById('gradeSelector');
    if (gradeSelector) {
        if (user.role === 'student') {
            gradeSelector.classList.remove('hidden');
            const viewingGrade = document.getElementById('viewingGrade');
            if (viewingGrade) {
                viewingGrade.value = user.gradeLevel || 5;

                // Reload content when grade changes
                viewingGrade.addEventListener('change', () => {
                    const activePanel = document.querySelector('.panel.active');
                    if (activePanel) {
                        if (activePanel.id === 'resourcesPanel') loadResources();
                        else if (activePanel.id === 'quizzesPanel') loadQuizzes();
                        else if (activePanel.id === 'progressPanel') loadProgress();
                    }
                });
            }
        } else {
            gradeSelector.classList.add('hidden');
        }
    }

    // Show/hide teacher-specific buttons
    if (user.role === 'teacher') {
        document.getElementById('uploadResourceBtn')?.classList.remove('hidden');
        document.getElementById('createQuizBtn')?.classList.remove('hidden');
        document.getElementById('aiTutorBtn')?.classList.remove('nav-btn-highlight');

        // Hide home button for teachers (they have teacherDashBtn instead)
        document.getElementById('homeBtn').style.display = 'none';

        // Show teacher dashboard button
        const teacherDashBtn = document.getElementById('teacherDashBtn');
        if (teacherDashBtn) {
            teacherDashBtn.style.display = 'flex';
            teacherDashBtn.classList.add('active');
        }

        // Show teacher dashboard panel
        document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
        const teacherPanel = document.getElementById('teacherPanel');
        if (teacherPanel) {
            teacherPanel.classList.add('active');
        }

        // Hide grade selector for teachers
        document.getElementById('gradeSelector')?.classList.add('hidden');

        // Load teacher dashboard
        if (typeof loadTeacherDashboard === 'function') {
            await loadTeacherDashboard();
        }
        return; // Skip student dashboard loading
    } else {
        document.getElementById('uploadResourceBtn')?.classList.add('hidden');
        document.getElementById('createQuizBtn')?.classList.add('hidden');
        // Hide teacher dashboard button for non-teachers
        document.getElementById('teacherDashBtn').style.display = 'none';
    }

    // For parents, hide student tabs and show parent dashboard
    if (user.role === 'parent') {
        // Hide all student tabs from navbar
        document.getElementById('homeBtn')?.style.setProperty('display', 'none');
        document.getElementById('resourcesBtn')?.style.setProperty('display', 'none');
        document.getElementById('quizzesBtn')?.style.setProperty('display', 'none');
        document.getElementById('aiTutorBtn')?.style.setProperty('display', 'none');
        document.getElementById('papersBtn')?.style.setProperty('display', 'none');
        document.getElementById('toolsBtn')?.style.setProperty('display', 'none');
        document.getElementById('careerBtn')?.style.setProperty('display', 'none');
        document.getElementById('doubtsBtn')?.style.setProperty('display', 'none');
        document.getElementById('progressBtn')?.style.setProperty('display', 'none');

        // Show parent dashboard button (which we'll add)
        const parentBtn = document.getElementById('parentDashBtn');
        if (parentBtn) {
            parentBtn.style.display = 'flex';
            parentBtn.classList.add('active');
        }

        // Hide grade selector (parents don't use it)
        document.getElementById('gradeSelector')?.classList.add('hidden');

        // Hide all panels except parent panel
        document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
        const parentPanel = document.getElementById('parentPanel');
        if (parentPanel) {
            parentPanel.classList.add('active');
        }

        // Load parent dashboard
        if (typeof loadParentDashboard === 'function') {
            loadParentDashboard();
        }
        return; // Skip student dashboard loading
    }

    // Load home stats by default
    if (typeof loadHomeStats === 'function') {
        await loadHomeStats();
    }
}

/**
 * Setup main navigation
 */
document.addEventListener('DOMContentLoaded', () => {
    // Setup logout button globally (works on page load)
    const logoutBtn = document.getElementById('logoutBtn');
    if (logoutBtn) {
        logoutBtn.onclick = function(e) {
            e.preventDefault();
            console.log('Logout clicked');
            if (typeof handleLogout === 'function') {
                handleLogout();
            } else {
                // Fallback - clear and reload
                localStorage.clear();
                sessionStorage.clear();
                window.location.href = '/';
            }
        };
    }

    // Resources tab
    const resourcesBtn = document.getElementById('resourcesBtn');
    if (resourcesBtn) {
        resourcesBtn.addEventListener('click', () => {
            switchPanel('resourcesPanel', resourcesBtn);
            loadResources();
        });
    }

    // Online/offline status
    updateOnlineStatus();
    window.addEventListener('online', updateOnlineStatus);
    window.addEventListener('offline', updateOnlineStatus);

    // Health check periodic
    setInterval(checkSystemHealth, 60000);
});

function updateOnlineStatus() {
    const isOnline = navigator.onLine;
    const banner = document.getElementById('offlineBanner');
    const indicator = document.getElementById('connectionStatus');

    if (isOnline) {
        if (banner) banner.classList.add('hidden');
        if (indicator) {
            indicator.textContent = '🟢';
            indicator.title = 'Online';
            indicator.className = 'connection-status online';
        }
        console.log('Status: Online - syncing pending data');
        // Try to sync pending data
        if (typeof offlineDB !== 'undefined' && offlineDB.syncPending) {
            offlineDB.syncPending().catch(err => console.warn('Sync failed:', err));
        }
    } else {
        if (banner) banner.classList.remove('hidden');
        if (indicator) {
            indicator.textContent = '🔴';
            indicator.title = 'Offline - Using cached content';
            indicator.className = 'connection-status offline';
        }
        console.log('Status: Offline - Using cached content');
    }
}

async function checkSystemHealth() {
    try {
        const health = await API.health.check();
        if (!health.details.ollama) {
            console.warn('Ollama is unavailable');
        }
    } catch (error) {
        console.warn('Health check failed:', error);
    }
}

/**
 * Initialize app on load
 */
window.addEventListener('load', async () => {
    try {
        await offlineDB.init();

        if (navigator.onLine) {
            await offlineDB.syncPending();
        }

        const user = Utils.getCurrentUser();
        if (user) {
            document.getElementById('authScreen').classList.remove('active');
            document.getElementById('dashboardScreen').classList.add('active');
            await loadDashboard();
        }

        await checkSystemHealth();
    } catch (error) {
        console.error('Initialization error:', error);
    }
});

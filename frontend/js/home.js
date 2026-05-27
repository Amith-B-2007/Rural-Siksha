/**
 * Home Dashboard - Stats and quick actions
 */

async function loadHomeStats() {
    const user = Utils.getCurrentUser();
    if (!user) return;

    // Welcome message
    const welcomeEl = document.getElementById('welcomeMessage');
    if (welcomeEl) {
        if (user.role === 'student') {
            welcomeEl.textContent = `Hello ${user.fullName}! Continue learning - Grade ${user.gradeLevel}`;
        } else {
            welcomeEl.textContent = `Welcome ${user.fullName}! Manage your classes and students`;
        }
    }

    // Render gamification stats for students
    if (user.role === 'student') {
        const gamifyContainer = document.getElementById('gamificationContainer');
        if (gamifyContainer && typeof renderGamificationStats === 'function') {
            gamifyContainer.innerHTML = renderGamificationStats();
        }
        // Track login
        if (typeof trackLogin === 'function') {
            trackLogin();
        }
    }

    try {
        const grade = typeof getCurrentViewingGrade === 'function' ? getCurrentViewingGrade() : user.gradeLevel;

        // Fetch counts in parallel
        const [resources, quizzes, papers, progress] = await Promise.all([
            API.resources.list(grade).catch(() => []),
            API.quizzes.list(grade).catch(() => []),
            API.request('GET', '/question-papers' + (grade ? `?grade=${grade}` : '')).catch(() => []),
            API.progress.summary().catch(() => ({quizzes_completed: 0}))
        ]);

        // Update stats
        document.getElementById('totalResources').textContent = resources.length || 0;
        document.getElementById('totalQuizzes').textContent = quizzes.length || 0;
        document.getElementById('totalPapers').textContent = papers.length || 0;
        document.getElementById('totalCompleted').textContent = progress.quizzes_completed || 0;
    } catch (error) {
        console.error('Failed to load home stats:', error);
    }
}

/**
 * Filter resources by subject from home
 */
function filterBySubject(subject) {
    document.getElementById('resourcesBtn').click();
    const filter = document.getElementById('subjectFilter');
    if (filter) {
        filter.value = subject;
        loadResources();
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const homeBtn = document.getElementById('homeBtn');
    if (homeBtn) {
        homeBtn.addEventListener('click', () => {
            switchPanel('homePanel', homeBtn);
            loadHomeStats();
        });
    }
});

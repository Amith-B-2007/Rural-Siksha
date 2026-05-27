/**
 * Gamification System - XP, Streaks, Badges
 */

const BADGES = [
    {id: 'first_login', name: 'First Steps', icon: '👶', desc: 'Logged in for the first time', xp: 10},
    {id: 'first_quiz', name: 'Quiz Beginner', icon: '🎯', desc: 'Completed your first quiz', xp: 50},
    {id: 'quiz_master', name: 'Quiz Master', icon: '🏆', desc: 'Passed 5 quizzes', xp: 200},
    {id: 'perfect_score', name: 'Perfect Score', icon: '💯', desc: 'Got 100% in a quiz', xp: 100},
    {id: 'streak_3', name: '3-Day Warrior', icon: '🔥', desc: '3-day learning streak', xp: 75},
    {id: 'streak_7', name: 'Week Champion', icon: '⭐', desc: '7-day learning streak', xp: 150},
    {id: 'streak_30', name: 'Monthly Legend', icon: '👑', desc: '30-day learning streak', xp: 500},
    {id: 'reader_5', name: 'Bookworm', icon: '📚', desc: 'Read 5 resources', xp: 50},
    {id: 'reader_25', name: 'Scholar', icon: '🎓', desc: 'Read 25 resources', xp: 200},
    {id: 'curious_mind', name: 'Curious Mind', icon: '🧠', desc: 'Asked 5 questions to AI Tutor', xp: 75},
    {id: 'helper', name: 'Helper', icon: '🤝', desc: 'Saved 3 doubts for review', xp: 50},
    {id: 'all_subjects', name: 'Well-Rounded', icon: '🌟', desc: 'Studied all 6 subjects', xp: 300},
];

const XP_REWARDS = {
    login: 10,
    quiz_completed: 50,
    quiz_passed: 25,
    resource_viewed: 5,
    doubt_asked: 15,
    ai_question: 5,
    perfect_quiz: 50,
};

/**
 * Get game data from localStorage
 */
function getGameData() {
    const user = Utils.getCurrentUser();
    if (!user) return null;

    const key = `gamification_${user.id}`;
    const data = localStorage.getItem(key);
    if (data) {
        return JSON.parse(data);
    }
    return {
        xp: 0,
        level: 1,
        streak: 0,
        lastActivityDate: null,
        badges: [],
        quizzesCompleted: 0,
        quizzesPassed: 0,
        resourcesViewed: 0,
        aiQuestionsAsked: 0,
        doubtsAsked: 0,
        subjectsStudied: []
    };
}

/**
 * Save game data
 */
function saveGameData(data) {
    const user = Utils.getCurrentUser();
    if (!user) return;
    const key = `gamification_${user.id}`;
    localStorage.setItem(key, JSON.stringify(data));
}

/**
 * Calculate level from XP
 */
function calculateLevel(xp) {
    return Math.floor(xp / 100) + 1;
}

/**
 * Get XP needed for next level
 */
function xpForNextLevel(xp) {
    const level = calculateLevel(xp);
    return level * 100 - xp;
}

/**
 * Award XP for an action
 */
function awardXP(action, amount = null) {
    const data = getGameData();
    if (!data) return;

    const xpAmount = amount || XP_REWARDS[action] || 5;
    const oldLevel = data.level;
    data.xp += xpAmount;
    data.level = calculateLevel(data.xp);

    saveGameData(data);

    // Show notification
    showXPGain(xpAmount, action);

    // Level up notification
    if (data.level > oldLevel) {
        showLevelUp(data.level);
    }
}

/**
 * Update streak
 */
function updateStreak() {
    const data = getGameData();
    if (!data) return;

    const today = new Date().toDateString();

    if (data.lastActivityDate === today) {
        return; // Already counted today
    }

    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    const yesterdayStr = yesterday.toDateString();

    if (data.lastActivityDate === yesterdayStr) {
        // Continued streak
        data.streak += 1;
    } else if (data.lastActivityDate !== null) {
        // Broken streak
        data.streak = 1;
    } else {
        // First time
        data.streak = 1;
    }

    data.lastActivityDate = today;
    saveGameData(data);

    // Check streak badges
    if (data.streak >= 3 && !data.badges.includes('streak_3')) {
        awardBadge('streak_3');
    }
    if (data.streak >= 7 && !data.badges.includes('streak_7')) {
        awardBadge('streak_7');
    }
    if (data.streak >= 30 && !data.badges.includes('streak_30')) {
        awardBadge('streak_30');
    }
}

/**
 * Award a badge
 */
function awardBadge(badgeId) {
    const data = getGameData();
    if (!data) return;

    if (data.badges.includes(badgeId)) return; // Already earned

    const badge = BADGES.find(b => b.id === badgeId);
    if (!badge) return;

    data.badges.push(badgeId);
    data.xp += badge.xp;
    data.level = calculateLevel(data.xp);

    saveGameData(data);
    showBadgeEarned(badge);
}

/**
 * Track quiz completion
 */
function trackQuizCompleted(passed, percentage) {
    const data = getGameData();
    if (!data) return;

    data.quizzesCompleted += 1;
    if (passed) data.quizzesPassed += 1;

    saveGameData(data);

    awardXP('quiz_completed');
    if (passed) awardXP('quiz_passed');
    if (percentage === 100) {
        awardXP('perfect_quiz');
        awardBadge('perfect_score');
    }

    if (data.quizzesCompleted === 1) {
        awardBadge('first_quiz');
    }
    if (data.quizzesPassed >= 5) {
        awardBadge('quiz_master');
    }

    updateStreak();
}

/**
 * Track resource view
 */
function trackResourceViewed(subject) {
    const data = getGameData();
    if (!data) return;

    data.resourcesViewed += 1;

    if (subject && !data.subjectsStudied.includes(subject)) {
        data.subjectsStudied.push(subject);
    }

    saveGameData(data);
    awardXP('resource_viewed');

    if (data.resourcesViewed >= 5) {
        awardBadge('reader_5');
    }
    if (data.resourcesViewed >= 25) {
        awardBadge('reader_25');
    }
    if (data.subjectsStudied.length >= 6) {
        awardBadge('all_subjects');
    }

    updateStreak();
}

/**
 * Track AI question
 */
function trackAIQuestion() {
    const data = getGameData();
    if (!data) return;

    data.aiQuestionsAsked += 1;
    saveGameData(data);
    awardXP('ai_question');

    if (data.aiQuestionsAsked >= 5) {
        awardBadge('curious_mind');
    }

    updateStreak();
}

/**
 * Track doubt creation
 */
function trackDoubtAsked() {
    const data = getGameData();
    if (!data) return;

    data.doubtsAsked += 1;
    saveGameData(data);
    awardXP('doubt_asked');

    if (data.doubtsAsked >= 3) {
        awardBadge('helper');
    }
}

/**
 * Track login - daily streak
 */
function trackLogin() {
    const data = getGameData();
    if (!data) return;

    if (data.badges.length === 0) {
        awardBadge('first_login');
    }

    updateStreak();
}

/**
 * Show XP gained notification (toast)
 */
function showXPGain(amount, action) {
    showToast(`+${amount} XP`, '⚡', 'xp');
}

/**
 * Show level up notification
 */
function showLevelUp(level) {
    showToast(`Level Up! You are now Level ${level}!`, '🎉', 'levelup');
}

/**
 * Show badge earned notification
 */
function showBadgeEarned(badge) {
    showToast(`Badge Earned: ${badge.name}`, badge.icon, 'badge');
}

/**
 * Generic toast notification
 */
function showToast(message, icon, type) {
    const toast = document.createElement('div');
    toast.className = `gamify-toast gamify-${type}`;
    toast.innerHTML = `
        <span class="toast-icon">${icon}</span>
        <span class="toast-text">${message}</span>
    `;
    document.body.appendChild(toast);

    setTimeout(() => toast.classList.add('show'), 10);
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

/**
 * Display gamification stats on home page
 */
function renderGamificationStats() {
    const data = getGameData();
    if (!data) return '';

    const xpForNext = xpForNextLevel(data.xp);
    const progressPercent = ((data.xp % 100) / 100) * 100;

    return `
        <div class="gamify-card">
            <div class="gamify-header">
                <h3>🎮 Your Learning Journey</h3>
                <button onclick="showAllBadges()" class="btn btn-secondary btn-small">View All Badges</button>
            </div>
            <div class="gamify-stats">
                <div class="gamify-stat">
                    <div class="gamify-stat-value">${data.xp}</div>
                    <div class="gamify-stat-label">⚡ Total XP</div>
                </div>
                <div class="gamify-stat">
                    <div class="gamify-stat-value">${data.level}</div>
                    <div class="gamify-stat-label">📊 Level</div>
                </div>
                <div class="gamify-stat">
                    <div class="gamify-stat-value">${data.streak}</div>
                    <div class="gamify-stat-label">🔥 Day Streak</div>
                </div>
                <div class="gamify-stat">
                    <div class="gamify-stat-value">${data.badges.length}</div>
                    <div class="gamify-stat-label">🏅 Badges</div>
                </div>
            </div>
            <div class="gamify-progress">
                <div class="gamify-progress-text">
                    Level ${data.level} → ${data.level + 1} (${xpForNext} XP to go)
                </div>
                <div class="gamify-progress-bar">
                    <div class="gamify-progress-fill" style="width: ${progressPercent}%"></div>
                </div>
            </div>
            ${data.badges.length > 0 ? `
                <div class="earned-badges">
                    <h4>🏆 Recent Badges:</h4>
                    <div class="badge-list">
                        ${data.badges.slice(-5).map(bid => {
                            const b = BADGES.find(x => x.id === bid);
                            return b ? `<span class="badge-item" title="${b.desc}">${b.icon} ${b.name}</span>` : '';
                        }).join('')}
                    </div>
                </div>
            ` : ''}
        </div>
    `;
}

/**
 * Show all badges modal
 */
function showAllBadges() {
    const data = getGameData();
    if (!data) return;

    const html = `
        <h2>🏆 All Badges</h2>
        <p class="section-info">Earn badges by completing learning activities</p>
        <div class="all-badges-grid">
            ${BADGES.map(b => {
                const earned = data.badges.includes(b.id);
                return `
                    <div class="badge-card ${earned ? 'earned' : 'locked'}">
                        <div class="badge-icon-big">${earned ? b.icon : '🔒'}</div>
                        <h4>${b.name}</h4>
                        <p>${b.desc}</p>
                        <div class="badge-xp">+${b.xp} XP</div>
                        ${earned ? '<div class="earned-tag">✓ Earned</div>' : ''}
                    </div>
                `;
            }).join('')}
        </div>
        <button onclick="closeModal()" class="btn btn-primary" style="margin-top:20px">Close</button>
    `;
    openModal(html);
}

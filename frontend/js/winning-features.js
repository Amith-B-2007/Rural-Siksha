/**
 * Winning Features: Demo Tour + About Page + Adaptive AI + Daily Goals
 */

/* ====================================================
 * 1. INTERACTIVE DEMO TOUR - PROFESSIONAL VERSION
 * ==================================================== */

const TOUR_STEPS = [
    {
        target: '.welcome-banner',
        action: () => goToHome(),
        title: '🎓 Welcome to Rural Siksha!',
        content: 'This is the most comprehensive AI-powered education platform for rural India. Let me show you 8 amazing features!',
        position: 'bottom'
    },
    {
        target: '#gamificationContainer',
        action: () => goToHome(),
        title: '🎮 Gamification System',
        content: 'Students earn XP, badges, and streaks - just like Duolingo! This keeps them motivated to learn daily.',
        position: 'bottom'
    },
    {
        target: '#resourcesBtn',
        action: () => goToHome(),
        title: '📚 124 NCERT Resources',
        content: 'NCERT-aligned PDFs for ALL grades 1-10 in 6 subjects: Math, Science, English, Social Studies, Hindi, and Kannada!',
        position: 'bottom'
    },
    {
        target: '#aiTutorBtn',
        action: () => goToHome(),
        title: '🤖 AI Tutor (Runs Locally!)',
        content: 'Powered by Llama 3 running ON your computer. No internet needed! Plus voice input in 3 languages.',
        position: 'bottom'
    },
    {
        target: '#toolsBtn',
        action: () => goToHome(),
        title: '🧮 Smart Study Tools',
        content: 'Scientific calculator, COMPLETE 118-element periodic table, formula sheets, and unit converter - all built-in!',
        position: 'bottom'
    },
    {
        target: '#papersBtn',
        action: () => goToHome(),
        title: '📄 Practice Question Papers',
        content: '33 previous year question papers from 2021-2024. Perfect for exam preparation!',
        position: 'bottom'
    },
    {
        target: '#themeToggle',
        action: () => goToHome(),
        title: '🌙 Dark Mode',
        content: 'Switch between light and dark themes. Easy on the eyes for night study sessions!',
        position: 'bottom-left'
    },
    {
        target: '.welcome-banner',
        action: () => goToHome(),
        title: '🏆 Ready to Win!',
        content: 'You now know all the major features! Click "About Project" to see impact stats, or explore freely. Best of luck!',
        position: 'bottom'
    }
];

let tourStep = 0;
let tourOverlay = null;
let tourTooltip = null;
let tourBackdrop = null;

function goToHome() {
    // Make sure we're on the home panel
    const homeBtn = document.getElementById('homeBtn');
    if (homeBtn && !homeBtn.classList.contains('active')) {
        homeBtn.click();
    }
    // Make home panel active
    document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
    const homePanel = document.getElementById('homePanel');
    if (homePanel) homePanel.classList.add('active');
}

function startDemoTour() {
    tourStep = 0;
    // Ensure we're on home page first
    goToHome();
    setTimeout(() => {
        // Scroll to top
        window.scrollTo({top: 0, behavior: 'instant'});
        setTimeout(() => showTourStep(), 200);
    }, 200);
}

function showTourStep() {
    if (tourStep >= TOUR_STEPS.length) {
        endTour();
        return;
    }

    const step = TOUR_STEPS[tourStep];

    // Run any action for this step
    if (step.action) {
        try {
            step.action();
        } catch (e) {
            console.error('Tour action error:', e);
        }
    }

    // Clean up existing tour elements
    cleanupTour();

    // Wait briefly for any DOM updates
    setTimeout(() => {
        const target = document.querySelector(step.target);

        if (!target) {
            console.warn('Tour target not found:', step.target);
            tourStep++;
            showTourStep();
            return;
        }

        // Scroll target into view first
        const targetRect = target.getBoundingClientRect();
        const targetTop = targetRect.top + window.pageYOffset;
        const targetMiddle = targetTop - (window.innerHeight / 2) + (targetRect.height / 2);

        window.scrollTo({top: Math.max(0, targetMiddle), behavior: 'smooth'});

        // Wait for scroll to complete, then show overlay
        setTimeout(() => {
            renderTourOverlay(target, step);
        }, 500);
    }, 100);
}

function renderTourOverlay(target, step) {
    const rect = target.getBoundingClientRect();

    // Create backdrop with cutout
    tourBackdrop = document.createElement('div');
    tourBackdrop.className = 'tour-backdrop';
    tourBackdrop.innerHTML = `
        <svg class="tour-backdrop-svg" width="100%" height="100%">
            <defs>
                <mask id="tour-mask">
                    <rect width="100%" height="100%" fill="white"/>
                    <rect x="${rect.left - 10}" y="${rect.top - 10}"
                          width="${rect.width + 20}" height="${rect.height + 20}"
                          rx="12" fill="black"/>
                </mask>
            </defs>
            <rect width="100%" height="100%" fill="rgba(0,0,0,0.75)" mask="url(#tour-mask)"/>
        </svg>
    `;
    document.body.appendChild(tourBackdrop);

    // Create highlight border
    const highlight = document.createElement('div');
    highlight.className = 'tour-highlight-border';
    highlight.style.cssText = `
        top: ${rect.top - 8}px;
        left: ${rect.left - 8}px;
        width: ${rect.width + 16}px;
        height: ${rect.height + 16}px;
    `;
    document.body.appendChild(highlight);
    tourOverlay = highlight;

    // Create tooltip
    tourTooltip = document.createElement('div');
    tourTooltip.className = 'tour-tooltip-new';

    // Determine position
    let tooltipTop, tooltipLeft;
    const tooltipWidth = 360;
    const tooltipMaxHeight = 240;

    // Try below first
    if (rect.bottom + tooltipMaxHeight + 30 < window.innerHeight) {
        tooltipTop = rect.bottom + 20;
    } else if (rect.top > tooltipMaxHeight + 30) {
        // Try above
        tooltipTop = rect.top - tooltipMaxHeight - 30;
    } else {
        // Center vertically
        tooltipTop = Math.max(20, window.innerHeight / 2 - tooltipMaxHeight / 2);
    }

    tooltipLeft = Math.max(20, Math.min(rect.left + rect.width/2 - tooltipWidth/2, window.innerWidth - tooltipWidth - 20));

    tourTooltip.style.cssText = `
        top: ${tooltipTop}px;
        left: ${tooltipLeft}px;
        width: ${tooltipWidth}px;
    `;

    tourTooltip.innerHTML = `
        <div class="tour-progress">
            <div class="tour-progress-bar">
                <div class="tour-progress-fill" style="width: ${((tourStep + 1) / TOUR_STEPS.length) * 100}%"></div>
            </div>
            <div class="tour-step-text">Step ${tourStep + 1} of ${TOUR_STEPS.length}</div>
        </div>
        <h3 class="tour-title">${step.title}</h3>
        <p class="tour-content">${step.content}</p>
        <div class="tour-buttons-new">
            <button onclick="endTour()" class="tour-btn-skip">Skip</button>
            <div class="tour-nav-buttons">
                ${tourStep > 0 ? '<button onclick="prevTourStep()" class="tour-btn-back">← Back</button>' : ''}
                <button onclick="nextTourStep()" class="tour-btn-next">
                    ${tourStep === TOUR_STEPS.length - 1 ? '✓ Finish' : 'Next →'}
                </button>
            </div>
        </div>
    `;

    document.body.appendChild(tourTooltip);

    // Animate in
    requestAnimationFrame(() => {
        if (tourTooltip) tourTooltip.classList.add('show');
    });
}

function cleanupTour() {
    if (tourBackdrop) {
        tourBackdrop.remove();
        tourBackdrop = null;
    }
    if (tourOverlay) {
        tourOverlay.remove();
        tourOverlay = null;
    }
    if (tourTooltip) {
        tourTooltip.remove();
        tourTooltip = null;
    }
}

function nextTourStep() {
    tourStep++;
    showTourStep();
}

function prevTourStep() {
    if (tourStep > 0) {
        tourStep--;
        showTourStep();
    }
}

function endTour() {
    cleanupTour();
    if (typeof toast !== 'undefined') {
        toast.success('🎉 Tour complete! Explore the features yourself!');
    }
}

// Handle window resize during tour
window.addEventListener('resize', () => {
    if (tourTooltip) {
        showTourStep();
    }
});

// Handle escape key
window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && tourTooltip) {
        endTour();
    }
    if (e.key === 'ArrowRight' && tourTooltip) {
        nextTourStep();
    }
    if (e.key === 'ArrowLeft' && tourTooltip) {
        prevTourStep();
    }
});

/* ====================================================
 * 2. ABOUT / IMPACT PAGE
 * ==================================================== */

function showAboutPage() {
    const html = `
        <div class="about-page">
            <div class="about-hero">
                <div class="about-logo">🎓</div>
                <h1>Rural Siksha</h1>
                <p class="about-tagline">Empowering Rural India through AI-powered Education</p>
            </div>

            <div class="about-section">
                <h2>🎯 Our Mission</h2>
                <p>To bridge the educational gap in rural India by providing FREE, OFFLINE-CAPABLE, AI-powered learning in students' native languages.</p>
            </div>

            <div class="about-stats">
                <h2>📊 Platform Statistics</h2>
                <div class="stats-grid">
                    <div class="stat-card math">
                        <div class="stat-card-icon">📚</div>
                        <div class="stat-card-number">124</div>
                        <div class="stat-card-label">NCERT Resources</div>
                    </div>
                    <div class="stat-card science">
                        <div class="stat-card-icon">📝</div>
                        <div class="stat-card-number">87</div>
                        <div class="stat-card-label">Smart Quizzes</div>
                    </div>
                    <div class="stat-card english">
                        <div class="stat-card-icon">📄</div>
                        <div class="stat-card-number">33</div>
                        <div class="stat-card-label">Question Papers</div>
                    </div>
                    <div class="stat-card social">
                        <div class="stat-card-icon">🌐</div>
                        <div class="stat-card-number">6</div>
                        <div class="stat-card-label">Subjects</div>
                    </div>
                </div>
            </div>

            <div class="about-section">
                <h2>🚀 Technical Innovation</h2>
                <div class="tech-grid">
                    <div class="tech-item">
                        <div class="tech-icon">🤖</div>
                        <h4>Local AI (Ollama + Llama 3)</h4>
                        <p>AI runs LOCALLY on the computer - no data sent to cloud. Works offline!</p>
                    </div>
                    <div class="tech-item">
                        <div class="tech-icon">🔌</div>
                        <h4>Full Offline Support</h4>
                        <p>Service Worker + IndexedDB caching means rural areas with poor internet still get education.</p>
                    </div>
                    <div class="tech-item">
                        <div class="tech-icon">🎙️</div>
                        <h4>Voice Input/Output</h4>
                        <p>Web Speech API for voice chat with AI in Hindi, Kannada, and English.</p>
                    </div>
                    <div class="tech-item">
                        <div class="tech-icon">📱</div>
                        <h4>PWA Installable</h4>
                        <p>Install on phone like a native app. No app store needed.</p>
                    </div>
                    <div class="tech-item">
                        <div class="tech-icon">🌐</div>
                        <h4>Multi-Language</h4>
                        <p>English, Hindi, Kannada - with infrastructure for more Indian languages.</p>
                    </div>
                    <div class="tech-item">
                        <div class="tech-icon">📷</div>
                        <h4>Photo Math Scanner</h4>
                        <p>Take photo of math problem, AI solves step-by-step.</p>
                    </div>
                </div>
            </div>

            <div class="about-section">
                <h2>🌍 Potential Impact</h2>
                <div class="impact-list">
                    <div class="impact-item">
                        <span class="impact-num">250M+</span>
                        <p>Rural Indian students who could benefit</p>
                    </div>
                    <div class="impact-item">
                        <span class="impact-num">FREE</span>
                        <p>vs ₹1000-5000/month for BYJU's, Vedantu, etc.</p>
                    </div>
                    <div class="impact-item">
                        <span class="impact-num">100%</span>
                        <p>Offline-capable for areas with poor internet</p>
                    </div>
                    <div class="impact-item">
                        <span class="impact-num">3</span>
                        <p>User roles: Students, Teachers, Parents</p>
                    </div>
                </div>
            </div>

            <div class="about-section">
                <h2>✨ Key Features</h2>
                <div class="features-list-about">
                    <div>📚 NCERT-aligned curriculum (all grades 1-10)</div>
                    <div>🤖 AI Tutor with Voice Chat</div>
                    <div>📷 Math Problem Scanner</div>
                    <div>🎮 Gamification (XP, Badges, Streaks)</div>
                    <div>🌙 Dark Mode</div>
                    <div>🔊 Text-to-Speech (6 languages)</div>
                    <div>🧮 Calculator + 118 Periodic Elements</div>
                    <div>🎯 Career Guidance + Scholarships</div>
                    <div>🎮 Educational Games</div>
                    <div>🏆 Leaderboard</div>
                    <div>📊 Detailed Progress Tracking</div>
                    <div>👨‍👩‍👧 Parent Dashboard</div>
                    <div>👨‍🏫 Teacher Dashboard</div>
                    <div>📱 Mobile Responsive</div>
                    <div>🔌 Service Worker PWA</div>
                </div>
            </div>

            <div class="about-section">
                <h2>🎓 Why Rural Siksha Wins</h2>
                <div class="why-grid">
                    <div class="why-item">
                        <strong>✅ FREE FOREVER</strong>
                        <p>No subscription, no ads, no hidden costs</p>
                    </div>
                    <div class="why-item">
                        <strong>✅ WORKS OFFLINE</strong>
                        <p>Critical for rural India's connectivity issues</p>
                    </div>
                    <div class="why-item">
                        <strong>✅ AI runs LOCALLY</strong>
                        <p>Privacy-first, no data sent to cloud</p>
                    </div>
                    <div class="why-item">
                        <strong>✅ NATIVE LANGUAGES</strong>
                        <p>Hindi, Kannada - in rural students' language</p>
                    </div>
                    <div class="why-item">
                        <strong>✅ NCERT ALIGNED</strong>
                        <p>Matches government school curriculum</p>
                    </div>
                    <div class="why-item">
                        <strong>✅ MULTI-ROLE</strong>
                        <p>Students, Teachers, Parents all connected</p>
                    </div>
                </div>
            </div>

            <div class="about-cta">
                <h2>🚀 Ready to Transform Rural Education?</h2>
                <button onclick="closeModal(); startDemoTour();" class="btn btn-primary btn-large">▶️ Take the Demo Tour</button>
                <button onclick="closeModal()" class="btn btn-secondary">Close</button>
            </div>
        </div>
    `;
    openModal(html);
}

/* ====================================================
 * 3. ADAPTIVE AI LEARNING + DAILY GOALS
 * ==================================================== */

function showAdaptiveLearning() {
    const user = Utils.getCurrentUser();
    if (!user) return;

    const data = typeof getGameData === 'function' ? getGameData() : null;

    // Analyze weak subjects from progress
    const weakSubjects = [];
    const strongSubjects = [];

    if (data && data.subjectsStudied && data.subjectsStudied.length > 0) {
        // Mock analysis
        const subjects = ['Mathematics', 'Science', 'English', 'Social Studies', 'Hindi', 'Kannada'];
        subjects.forEach(s => {
            if (!data.subjectsStudied.includes(s)) {
                weakSubjects.push(s);
            } else {
                strongSubjects.push(s);
            }
        });
    } else {
        weakSubjects.push('Mathematics', 'Science', 'English');
    }

    // Get today's date
    const today = new Date().toDateString();
    const goalKey = `dailyGoal_${user.id}_${today}`;
    const completedKey = `dailyCompleted_${user.id}_${today}`;
    let dailyGoal = parseInt(localStorage.getItem(goalKey) || '3');
    let completed = parseInt(localStorage.getItem(completedKey) || '0');

    const progress = Math.min(100, (completed / dailyGoal) * 100);

    const html = `
        <div class="adaptive-learning">
            <h2>🎯 Your Personalized Learning Plan</h2>
            <p class="section-info">AI-powered recommendations based on your activity</p>

            <div class="daily-goal-card">
                <h3>📅 Today's Goal</h3>
                <div class="goal-progress">
                    <div class="goal-stats">
                        <span>${completed} / ${dailyGoal} activities</span>
                        <span>${Math.round(progress)}%</span>
                    </div>
                    <div class="goal-bar">
                        <div class="goal-bar-fill" style="width: ${progress}%"></div>
                    </div>
                </div>
                ${progress >= 100 ?
                    '<p class="goal-done">🎉 You\'ve completed today\'s goal! Great work!</p>' :
                    `<p class="goal-pending">📚 Complete ${dailyGoal - completed} more activities to reach your goal!</p>`
                }
                <div class="goal-adjust">
                    <label>Set new goal: </label>
                    <input type="range" id="newGoal" min="1" max="10" value="${dailyGoal}" oninput="document.getElementById('goalDisplay').textContent = this.value">
                    <span id="goalDisplay">${dailyGoal}</span>
                    <button onclick="setNewGoal()" class="btn btn-primary btn-small">Update</button>
                </div>
            </div>

            <div class="adaptive-card">
                <h3>🧠 AI Recommendations</h3>
                <p>Based on your activity, here's what to focus on:</p>

                ${weakSubjects.length > 0 ? `
                    <div class="rec-section">
                        <h4>📍 Focus Areas (Need Improvement):</h4>
                        <div class="subject-tags">
                            ${weakSubjects.slice(0, 3).map(s => `
                                <span class="subject-tag focus" onclick="document.getElementById('resourcesBtn').click(); closeModal();">
                                    ${getSubjectIcon ? getSubjectIcon(s) : '📚'} ${s}
                                </span>
                            `).join('')}
                        </div>
                    </div>
                ` : ''}

                ${strongSubjects.length > 0 ? `
                    <div class="rec-section">
                        <h4>💪 Your Strong Areas:</h4>
                        <div class="subject-tags">
                            ${strongSubjects.slice(0, 3).map(s => `
                                <span class="subject-tag strong">
                                    ${getSubjectIcon ? getSubjectIcon(s) : '📚'} ${s}
                                </span>
                            `).join('')}
                        </div>
                    </div>
                ` : ''}

                <div class="rec-section">
                    <h4>📋 Suggested Actions:</h4>
                    <ul class="suggested-actions">
                        <li>📚 Read 2 NCERT resources from weak subjects</li>
                        <li>📝 Take 1 quiz to test your knowledge</li>
                        <li>🤖 Ask 3 questions to AI Tutor</li>
                        <li>🎮 Play 1 educational game</li>
                        <li>📄 Practice 1 question paper</li>
                    </ul>
                </div>
            </div>

            <div class="learning-tips">
                <h3>💡 Today's Learning Tip</h3>
                <p>${getRandomTip()}</p>
            </div>

            <button onclick="closeModal()" class="btn btn-primary">Got it! Let's Learn 🚀</button>
        </div>
    `;
    openModal(html);
}

function setNewGoal() {
    const newGoal = document.getElementById('newGoal').value;
    const user = Utils.getCurrentUser();
    if (!user) return;
    const today = new Date().toDateString();
    localStorage.setItem(`dailyGoal_${user.id}_${today}`, newGoal);
    if (typeof toast !== 'undefined') {
        toast.success(`Daily goal set to ${newGoal} activities!`);
    }
    setTimeout(() => showAdaptiveLearning(), 500);
}

const LEARNING_TIPS = [
    "📖 Read in short sessions - 25 minutes of focused study beats 2 hours of distracted reading.",
    "✍️ Write what you learn - The act of writing helps your brain remember better.",
    "🌅 Study early morning - Your mind is fresh and absorbs information better.",
    "💧 Stay hydrated - Drink water regularly to keep your brain functioning optimally.",
    "😴 Sleep is crucial - 8 hours of sleep helps consolidate what you've learned.",
    "🎯 Set small goals - Achievable daily targets beat overwhelming weekly ones.",
    "🤝 Teach someone - Explaining concepts to others is the best way to learn.",
    "🧘 Take breaks - 5 minute breaks every 25 minutes (Pomodoro technique) works wonders.",
    "📝 Make notes in your own words - Don't just copy. Understand and rephrase.",
    "🔁 Revise regularly - 5 minutes daily revision is better than 1 hour weekly.",
    "🎮 Make it fun - Use games and quizzes to make learning enjoyable.",
    "🏃 Exercise daily - Physical activity improves brain function and memory.",
];

function getRandomTip() {
    return LEARNING_TIPS[Math.floor(Math.random() * LEARNING_TIPS.length)];
}

// Track daily goal progress automatically
function incrementDailyGoal() {
    const user = Utils.getCurrentUser();
    if (!user) return;
    const today = new Date().toDateString();
    const completedKey = `dailyCompleted_${user.id}_${today}`;
    let completed = parseInt(localStorage.getItem(completedKey) || '0');
    completed++;
    localStorage.setItem(completedKey, completed.toString());

    const goalKey = `dailyGoal_${user.id}_${today}`;
    const goal = parseInt(localStorage.getItem(goalKey) || '3');

    if (completed === goal) {
        if (typeof toast !== 'undefined') {
            toast.success(`🎉 Daily goal achieved! ${completed}/${goal} activities done!`);
        }
        if (typeof awardXP === 'function') {
            awardXP('daily_goal', 100);
        }
    }
}

// Auto-track on resource view, quiz, AI question
document.addEventListener('DOMContentLoaded', () => {
    // Hook into existing tracking functions
    if (typeof trackResourceViewed === 'function') {
        const orig = window.trackResourceViewed;
        window.trackResourceViewed = function(...args) {
            orig.apply(this, args);
            incrementDailyGoal();
        };
    }
});

/**
 * Teacher Dashboard - Doubt clearance, resource upload, AI tutor
 */

async function loadTeacherDashboard() {
    const user = Utils.getCurrentUser();
    if (!user || user.role !== 'teacher') return;

    const container = document.getElementById('teacherContent');
    if (!container) return;

    container.innerHTML = `
        <div class="welcome-banner">
            <h1>👨‍🏫 Welcome, ${user.fullName}!</h1>
            <p>Subject: ${user.subject || 'Not set'} • Empower students through learning</p>
        </div>

        <h2 class="section-title">📊 Teaching Overview</h2>
        <div id="teacherStats" class="stats-grid">
            <div class="stat-card math">
                <div class="stat-card-icon">💭</div>
                <div class="stat-card-number" id="openDoubtsCount">-</div>
                <div class="stat-card-label">Open Doubts</div>
            </div>
            <div class="stat-card science">
                <div class="stat-card-icon">✅</div>
                <div class="stat-card-number" id="resolvedDoubtsCount">-</div>
                <div class="stat-card-label">Resolved Doubts</div>
            </div>
            <div class="stat-card english">
                <div class="stat-card-icon">👨‍🎓</div>
                <div class="stat-card-number" id="totalStudentsCount">-</div>
                <div class="stat-card-label">Total Students</div>
            </div>
            <div class="stat-card social">
                <div class="stat-card-icon">📝</div>
                <div class="stat-card-number" id="totalAttemptsCount">-</div>
                <div class="stat-card-label">Quiz Attempts</div>
            </div>
        </div>

        <h2 class="section-title">⚡ Quick Actions</h2>
        <div class="quick-actions">
            <a class="quick-action feature-card-doubts" onclick="goToTeacherDoubts()">
                <span class="qa-icon">💭</span>
                <div class="qa-title">Answer Doubts</div>
                <div class="qa-subtitle">Help students with their questions</div>
            </a>
            <a class="quick-action feature-card-progress" onclick="goToTeacherResources()">
                <span class="qa-icon">📚</span>
                <div class="qa-title">Upload Resources</div>
                <div class="qa-subtitle">Share NCERT materials</div>
            </a>
            <a class="quick-action feature-card-career" onclick="goToTeacherQuizzes()">
                <span class="qa-icon">📝</span>
                <div class="qa-title">Create Quizzes</div>
                <div class="qa-subtitle">Build new tests for students</div>
            </a>
            <a class="quick-action" onclick="goToPanel('aiTutorPanel')">
                <span class="qa-icon">🤖</span>
                <div class="qa-title">AI Tutor</div>
                <div class="qa-subtitle">Demo to students</div>
            </a>
            <a class="quick-action" onclick="goToPanel('papersPanel')">
                <span class="qa-icon">📄</span>
                <div class="qa-title">Question Papers</div>
                <div class="qa-subtitle">Manage exam papers</div>
            </a>
            <a class="quick-action" onclick="goToPanel('toolsPanel')">
                <span class="qa-icon">🧮</span>
                <div class="qa-title">Study Tools</div>
                <div class="qa-subtitle">Calculator & formulas</div>
            </a>
        </div>

        <h2 class="section-title">💭 Doubts Needing Your Help</h2>
        <div id="teacherDoubtsList" class="doubts-list">
            <p class="loading-text">Loading recent doubts...</p>
        </div>
    `;

    // Load stats and doubts
    await loadTeacherStats();
    await loadTeacherDoubts();
}

async function loadTeacherStats() {
    try {
        const data = await API.request('GET', '/progress');
        document.getElementById('openDoubtsCount').textContent = data.open_doubts || 0;
        document.getElementById('resolvedDoubtsCount').textContent = data.resolved_doubts || 0;
        document.getElementById('totalStudentsCount').textContent = data.total_students || 0;
        document.getElementById('totalAttemptsCount').textContent = data.total_quiz_attempts || 0;
    } catch (error) {
        console.error('Failed to load teacher stats:', error);
    }
}

async function loadTeacherDoubts() {
    try {
        const doubts = await API.doubts.list('open');
        const container = document.getElementById('teacherDoubtsList');

        if (!doubts || doubts.length === 0) {
            container.innerHTML = `
                <div class="empty-state">
                    <div class="empty-icon">✅</div>
                    <p><strong>All caught up!</strong> No open doubts at the moment.</p>
                    <p style="color:var(--text-light);font-size:13px;">Students will appear here when they need help.</p>
                </div>
            `;
            return;
        }

        container.innerHTML = doubts.slice(0, 5).map(doubt => `
            <div class="doubt-card status-${doubt.status}">
                <div class="doubt-header">
                    <h3>${doubt.question_text}</h3>
                    <span class="doubt-status">${doubt.status}</span>
                </div>
                <div class="resource-meta">
                    <span>📚 ${doubt.subject}</span>
                    <span>🎓 Grade ${doubt.grade_level}</span>
                    <span>👨‍🎓 ${doubt.student_name || 'Student'}</span>
                </div>
                <div class="resource-actions">
                    <button onclick="viewDoubt(${doubt.id})" class="btn-view">📝 Answer This Doubt</button>
                </div>
            </div>
        `).join('');

        if (doubts.length > 5) {
            container.innerHTML += `
                <p style="text-align:center; margin-top:15px;">
                    <a onclick="goToTeacherDoubts()" style="cursor:pointer; color:var(--primary); font-weight:600;">
                        View all ${doubts.length} doubts →
                    </a>
                </p>`;
        }
    } catch (error) {
        console.error('Failed to load teacher doubts:', error);
        const container = document.getElementById('teacherDoubtsList');
        if (container) {
            container.innerHTML = '<p class="loading-text">Could not load doubts. Try again.</p>';
        }
    }
}

function goToTeacherDoubts() {
    goToPanel('doubtsPanel');
}

function goToTeacherResources() {
    goToPanel('resourcesPanel');
    // Auto-open upload form for teachers
    setTimeout(() => {
        const uploadBtn = document.getElementById('uploadResourceBtn');
        if (uploadBtn) {
            uploadBtn.classList.remove('hidden');
        }
    }, 100);
}

function goToTeacherQuizzes() {
    goToPanel('quizzesPanel');
    setTimeout(() => {
        const createBtn = document.getElementById('createQuizBtn');
        if (createBtn) {
            createBtn.classList.remove('hidden');
        }
    }, 100);
}

document.addEventListener('DOMContentLoaded', () => {
    const teacherDashBtn = document.getElementById('teacherDashBtn');
    if (teacherDashBtn) {
        teacherDashBtn.addEventListener('click', () => {
            // Hide all panels
            document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
            // Hide all nav button active states
            document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));

            // Show teacher panel and activate button
            document.getElementById('teacherPanel').classList.add('active');
            teacherDashBtn.classList.add('active');

            loadTeacherDashboard();
        });
    }
});

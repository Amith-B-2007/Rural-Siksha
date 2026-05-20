/**
 * Parent Dashboard
 */

let currentChildEmail = null;

async function loadParentDashboard() {
    const user = Utils.getCurrentUser();
    if (!user || user.role !== 'parent') return;

    const container = document.getElementById('parentContent');
    if (!container) return;

    container.innerHTML = `
        <div class="parent-welcome">
            <h2>👨‍👩‍👧 Parent Dashboard</h2>
            <p>Track your child's learning progress</p>
        </div>

        <div class="parent-search-card">
            <h3>🔍 Find Your Child</h3>
            <p>Enter your child's registered email to view their progress</p>
            <div class="parent-search-form">
                <input type="email" id="childEmail" placeholder="child@example.com">
                <button onclick="searchChild()" class="btn btn-primary">View Progress</button>
            </div>
            <p class="hint-text">💡 Try: student@example.com (demo account)</p>
        </div>

        <div id="childProgressView"></div>
    `;
}

async function searchChild() {
    const email = document.getElementById('childEmail').value.trim();
    if (!email) {
        Utils.showSuccess('Please enter your child\'s email');
        return;
    }

    try {
        const response = await API.request('GET', `/parent/child/${encodeURIComponent(email)}/progress`);
        currentChildEmail = email;
        displayChildProgress(response);
    } catch (error) {
        console.error('Failed to load child:', error);
        document.getElementById('childProgressView').innerHTML = `
            <div class="error-message">
                <p>❌ Could not find student with email: ${email}</p>
                <p>Make sure your child has registered with this email.</p>
            </div>
        `;
    }
}

function displayChildProgress(data) {
    const container = document.getElementById('childProgressView');
    const child = data.child;
    const overall = data.overall;

    let html = `
        <div class="child-info-card">
            <div class="child-avatar">👨‍🎓</div>
            <div>
                <h3>${child.name}</h3>
                <p>Grade ${child.grade} • ${child.email}</p>
            </div>
        </div>

        <h3 class="section-title">📊 Overall Performance</h3>
        <div class="stats-grid">
            <div class="stat-card math">
                <div class="stat-card-icon">📝</div>
                <div class="stat-card-number">${overall.quizzes_completed}</div>
                <div class="stat-card-label">Quizzes Completed</div>
            </div>
            <div class="stat-card science">
                <div class="stat-card-icon">✅</div>
                <div class="stat-card-number">${overall.accuracy}%</div>
                <div class="stat-card-label">Accuracy</div>
            </div>
            <div class="stat-card english">
                <div class="stat-card-icon">📚</div>
                <div class="stat-card-number">${overall.total_questions}</div>
                <div class="stat-card-label">Questions Answered</div>
            </div>
            <div class="stat-card social">
                <div class="stat-card-icon">💭</div>
                <div class="stat-card-number">${overall.open_doubts}</div>
                <div class="stat-card-label">Open Doubts</div>
            </div>
        </div>
    `;

    if (data.by_subject && data.by_subject.length > 0) {
        html += `<h3 class="section-title">📚 Performance by Subject</h3>`;
        html += `<div class="subject-progress-grid">`;
        data.by_subject.forEach(s => {
            const icon = s.subject === 'Mathematics' ? '📐' :
                         s.subject === 'Science' ? '🔬' :
                         s.subject === 'English' ? '📖' : '🌍';
            html += `
                <div class="subject-progress-card">
                    <h4>${icon} ${s.subject}</h4>
                    <div class="progress-bar-container">
                        <div class="progress-bar" style="width: ${s.accuracy}%; background: linear-gradient(90deg, var(--primary), var(--accent-pink))"></div>
                    </div>
                    <div class="subject-stats">
                        <span>📊 ${s.accuracy}% accuracy</span>
                        <span>📝 ${s.quizzes} quizzes</span>
                        <span>✅ ${s.correct}/${s.questions}</span>
                    </div>
                </div>
            `;
        });
        html += `</div>`;
    }

    if (data.recent_attempts && data.recent_attempts.length > 0) {
        html += `<h3 class="section-title">📋 Recent Quiz Attempts</h3>`;
        html += `<div class="attempts-list">`;
        data.recent_attempts.forEach(a => {
            const passed = a.percentage >= 60;
            const statusIcon = passed ? '✅' : '⚠️';
            const date = a.date ? new Date(a.date).toLocaleDateString() : 'Pending';
            html += `
                <div class="attempt-item">
                    <div>
                        <h4>${statusIcon} ${a.quiz_title}</h4>
                        <p>📚 ${a.subject} • 📅 ${date}</p>
                    </div>
                    <div class="attempt-score ${passed ? 'pass' : 'fail'}">
                        ${a.percentage ? a.percentage.toFixed(1) + '%' : 'Pending'}
                    </div>
                </div>
            `;
        });
        html += `</div>`;
    } else {
        html += `<p class="info-tip">📝 Your child hasn't taken any quizzes yet. Encourage them to start!</p>`;
    }

    html += `
        <div class="parent-actions">
            <button onclick="viewChildDoubts()" class="btn btn-primary">💭 View Doubts</button>
            <button onclick="searchChild()" class="btn btn-secondary">🔄 Refresh</button>
        </div>
    `;

    container.innerHTML = html;
}

async function viewChildDoubts() {
    if (!currentChildEmail) return;

    try {
        const doubts = await API.request('GET', `/parent/child/${encodeURIComponent(currentChildEmail)}/doubts`);

        let html = `<h2>💭 ${currentChildEmail}'s Doubts</h2>`;
        if (doubts.length === 0) {
            html += `<p>No doubts saved yet.</p>`;
        } else {
            html += `<div class="doubts-list-parent">`;
            doubts.forEach(d => {
                const statusClass = d.status === 'resolved' ? 'resolved' : 'open';
                html += `
                    <div class="doubt-item-parent ${statusClass}">
                        <h4>${d.question}</h4>
                        <p>📚 ${d.subject} • Status: ${d.status} • Responses: ${d.response_count}</p>
                        <p class="date-small">${new Date(d.created_at).toLocaleDateString()}</p>
                    </div>
                `;
            });
            html += `</div>`;
        }
        html += `<button onclick="closeModal()" class="btn btn-primary">Close</button>`;

        openModal(html);
    } catch (error) {
        Utils.showSuccess('Could not load doubts');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const parentBtn = document.getElementById('parentBtn');
    if (parentBtn) {
        parentBtn.addEventListener('click', () => {
            switchPanel('parentPanel', parentBtn);
            loadParentDashboard();
        });
    }

    // Parent Dashboard button in navbar (for parent role)
    const parentDashBtn = document.getElementById('parentDashBtn');
    if (parentDashBtn) {
        parentDashBtn.addEventListener('click', () => {
            switchPanel('parentPanel', parentDashBtn);
            loadParentDashboard();
        });
    }
});

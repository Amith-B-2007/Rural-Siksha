/**
 * Doubts panel handlers - AI Tutor & Q&A
 */

/**
 * Check AI status and update banner
 */
async function checkAiStatus() {
    const banner = document.getElementById('aiStatusBanner');
    if (!banner) return;

    try {
        const status = await API.doubts.aiStatus();
        if (status.available) {
            banner.innerHTML = `<span class="status-ok">AI Tutor is online (${status.model})</span>`;
            banner.className = 'ai-status ok';
        } else {
            banner.innerHTML = '<span class="status-warn">AI Tutor is offline. Your questions will be saved for teacher review.</span>';
            banner.className = 'ai-status warn';
        }
    } catch (error) {
        banner.innerHTML = '<span class="status-warn">Could not check AI status</span>';
        banner.className = 'ai-status warn';
    }
}

/**
 * Load and display doubts
 */
async function loadDoubts() {
    const user = Utils.getCurrentUser();
    if (!user) return;

    try {
        const doubts = await API.doubts.list();
        await offlineDB.cache('/doubts', doubts);
        displayDoubts(doubts);
    } catch (error) {
        console.error('Failed to load doubts:', error);
        const cached = await offlineDB.getCached('/doubts');
        if (cached) displayDoubts(cached);
    }
}

/**
 * Display doubts in UI
 */
function displayDoubts(doubts) {
    const container = document.getElementById('doubtsList');

    if (!doubts || doubts.length === 0) {
        container.innerHTML = '<p>No doubts yet. Ask one above to get started!</p>';
        return;
    }

    container.innerHTML = doubts.map(doubt => `
        <div class="doubt-card status-${doubt.status}">
            <div class="doubt-header">
                <h3>${doubt.question_text}</h3>
                <span class="doubt-status">${doubt.status}</span>
            </div>
            ${doubt.question_detail ? `<p>${doubt.question_detail}</p>` : ''}
            <div class="resource-meta">
                <span>${doubt.subject}</span>
                <span>Grade ${doubt.grade_level}</span>
                <span>${Utils.formatDate(doubt.created_at)}</span>
                ${doubt.student_name ? `<span>By: ${doubt.student_name}</span>` : ''}
            </div>
            <p><strong>${doubt.response_count}</strong> response(s)</p>
            <div class="resource-actions">
                <button onclick="viewDoubt(${doubt.id})">View Responses</button>
            </div>
        </div>
    `).join('');
}

/**
 * View doubt detail and responses
 */
async function viewDoubt(doubtId) {
    try {
        const doubt = await API.doubts.get(doubtId);
        const responses = doubt.responses || [];

        let html = `
            <h2>${doubt.question_text}</h2>
            ${doubt.question_detail ? `<p>${doubt.question_detail}</p>` : ''}
            <div class="resource-meta">
                <span>${doubt.subject}</span>
                <span>Grade ${doubt.grade_level}</span>
                <span>Status: ${doubt.status}</span>
            </div>
            <hr>
            <h3>Responses (${responses.length})</h3>
        `;

        if (responses.length > 0) {
            responses.forEach(resp => {
                const icon = resp.response_type === 'ai' ? 'AI' : 'Teacher';
                html += `
                    <div class="response-card ${resp.response_type}">
                        <div class="response-header">
                            <strong>${icon}: ${resp.responder_name}</strong>
                            <span>${Utils.formatDate(resp.created_at)}</span>
                        </div>
                        <div class="response-text">${escapeHTML(resp.response_text).replace(/\n/g, '<br>')}</div>
                    </div>
                `;
            });
        } else {
            html += '<p>No responses yet. Check back later!</p>';
        }

        // Teacher response form
        if (Utils.isTeacher() && doubt.status !== 'resolved') {
            html += `
                <hr>
                <h3>Add Your Response</h3>
                <form id="teacherResponseForm" onsubmit="submitTeacherResponse(event, ${doubtId})">
                    <textarea id="teacherResponseText" rows="4" placeholder="Type your response..." required></textarea>
                    <button type="submit" class="btn btn-primary">Submit Response</button>
                </form>
            `;
        }

        openModal(html);
    } catch (error) {
        console.error('Failed to load doubt:', error);
        Utils.showSuccess('Could not load doubt details');
    }
}

/**
 * Submit teacher response
 */
async function submitTeacherResponse(e, doubtId) {
    e.preventDefault();
    const text = document.getElementById('teacherResponseText').value.trim();
    if (!text) return;

    try {
        await API.doubts.respond(doubtId, text);
        Utils.showSuccess('Response submitted successfully!');
        closeModal();
        loadDoubts();
    } catch (error) {
        console.error('Failed to submit response:', error);
        Utils.showSuccess('Failed to submit response');
    }
}

/**
 * Create new doubt
 */
async function createDoubt(e) {
    e.preventDefault();

    const user = Utils.getCurrentUser();
    if (!user) return;

    const subject = document.getElementById('doubtSubject').value;
    const question = document.getElementById('doubtQuestion').value.trim();

    if (!subject || !question) {
        Utils.showSuccess('Please fill all fields');
        return;
    }

    const btn = document.getElementById('submitDoubtBtn');
    btn.disabled = true;
    btn.textContent = 'Asking AI Tutor...';

    try {
        const response = await API.doubts.create(question, '', subject, user.gradeLevel);

        if (response.ai_response) {
            Utils.showSuccess('AI responded! Check your doubts list.');
        } else {
            Utils.showSuccess('Doubt submitted! Teacher will respond soon.');
        }

        document.getElementById('doubtForm').reset();
        loadDoubts();
    } catch (error) {
        console.error('Failed to create doubt:', error);
        if (!navigator.onLine) {
            await offlineDB.saveDraftDoubt({ subject, questionText: question, gradeLevel: user.gradeLevel });
            Utils.showSuccess('Doubt saved offline. Will be submitted when online.');
        } else {
            Utils.showSuccess('Failed to submit doubt');
        }
    } finally {
        btn.disabled = false;
        btn.textContent = 'Ask AI Tutor';
    }
}

/**
 * HTML escape helper
 */
function escapeHTML(str) {
    if (!str) return '';
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}

/**
 * Modal helpers
 */
function openModal(content) {
    document.getElementById('modalBody').innerHTML = content;
    document.getElementById('modalContainer').classList.remove('hidden');
}

function closeModal() {
    document.getElementById('modalContainer').classList.add('hidden');
}

/**
 * Setup event listeners
 */
document.addEventListener('DOMContentLoaded', () => {
    const doubtsBtn = document.getElementById('doubtsBtn');
    if (doubtsBtn) {
        doubtsBtn.addEventListener('click', () => {
            switchPanel('doubtsPanel', doubtsBtn);

            // Show/hide ask form based on role
            const askSection = document.getElementById('askDoubtSection');
            if (askSection) {
                if (Utils.isStudent()) {
                    askSection.classList.remove('hidden');
                } else {
                    askSection.classList.add('hidden');
                }
            }

            checkAiStatus();
            loadDoubts();
        });
    }

    const doubtForm = document.getElementById('doubtForm');
    if (doubtForm) {
        doubtForm.addEventListener('submit', createDoubt);
    }

    // Close modal on click outside
    document.getElementById('modalContainer')?.addEventListener('click', (e) => {
        if (e.target.id === 'modalContainer') {
            closeModal();
        }
    });
});

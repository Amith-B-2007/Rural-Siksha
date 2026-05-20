/**
 * Progress dashboard handlers
 */

async function loadProgress() {
    const user = Utils.getCurrentUser();
    if (!user) return;

    try {
        const progress = await API.progress.summary();
        await offlineDB.cache('/progress', progress);
        displayProgress(progress);
    } catch (error) {
        console.error('Failed to load progress:', error);
        const cached = await offlineDB.getCached('/progress');
        if (cached) displayProgress(cached);
    }
}

function displayProgress(progress) {
    const container = document.getElementById('progressSummary');
    const user = Utils.getCurrentUser();

    if (!progress) {
        container.innerHTML = '<p>No progress data available yet.</p>';
        return;
    }

    let html = '';

    if (user.role === 'student') {
        html = `
            <div class="progress-card">
                <h3>Overall Statistics</h3>
                <div class="progress-stat">
                    <label>Quizzes Completed:</label>
                    <strong>${progress.quizzes_completed || 0}</strong>
                </div>
                <div class="progress-stat">
                    <label>Average Score:</label>
                    <strong>${progress.average_score ? progress.average_score + '%' : 'N/A'}</strong>
                </div>
                <div class="progress-stat">
                    <label>Total Questions:</label>
                    <strong>${progress.total_questions_answered || 0}</strong>
                </div>
                <div class="progress-stat">
                    <label>Correct Answers:</label>
                    <strong>${progress.correct_answers || 0}</strong>
                </div>
                <div class="progress-stat">
                    <label>Doubts Resolved:</label>
                    <strong>${progress.doubts_resolved || 0}</strong>
                </div>
                <div class="progress-stat">
                    <label>Resources Viewed:</label>
                    <strong>${progress.resources_viewed || 0}</strong>
                </div>
            </div>
        `;

        if (progress.by_subject && progress.by_subject.length > 0) {
            progress.by_subject.forEach(subject => {
                html += `
                    <div class="progress-card">
                        <h3>${subject.name}</h3>
                        <div class="progress-stat">
                            <label>Questions:</label>
                            <strong>${subject.total || 0}</strong>
                        </div>
                        <div class="progress-stat">
                            <label>Correct:</label>
                            <strong>${subject.correct || 0}</strong>
                        </div>
                        <div class="progress-stat">
                            <label>Accuracy:</label>
                            <strong>${subject.accuracy}%</strong>
                        </div>
                        <div class="progress-stat">
                            <label>Quizzes:</label>
                            <strong>${subject.quizzes_completed || 0}</strong>
                        </div>
                    </div>
                `;
            });
        }

        if (progress.recent_attempts && progress.recent_attempts.length > 0) {
            html += '<div class="progress-card"><h3>Recent Attempts</h3>';
            progress.recent_attempts.forEach(att => {
                html += `
                    <div class="progress-stat">
                        <label>${att.quiz_title}:</label>
                        <strong>${att.percentage ? att.percentage.toFixed(1) + '%' : 'In Progress'}</strong>
                    </div>
                `;
            });
            html += '</div>';
        }
    } else {
        // Teacher dashboard
        html = `
            <div class="progress-card">
                <h3>Teacher Dashboard</h3>
                <div class="progress-stat">
                    <label>Open Doubts:</label>
                    <strong>${progress.open_doubts || 0}</strong>
                </div>
                <div class="progress-stat">
                    <label>Resolved Doubts:</label>
                    <strong>${progress.resolved_doubts || 0}</strong>
                </div>
                <div class="progress-stat">
                    <label>Total Students:</label>
                    <strong>${progress.total_students || 0}</strong>
                </div>
                <div class="progress-stat">
                    <label>Quiz Attempts:</label>
                    <strong>${progress.total_quiz_attempts || 0}</strong>
                </div>
            </div>
        `;
    }

    container.innerHTML = html;
}

document.addEventListener('DOMContentLoaded', () => {
    const progressBtn = document.getElementById('progressBtn');
    if (progressBtn) {
        progressBtn.addEventListener('click', () => {
            switchPanel('progressPanel', progressBtn);
            loadProgress();
        });
    }
});

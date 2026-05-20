/**
 * Question Papers Panel - Browse and view previous year papers
 */

let currentPapers = [];

/**
 * Load papers based on filters
 */
async function loadPapers() {
    const user = Utils.getCurrentUser();
    if (!user) return;

    try {
        const subject = document.getElementById('paperSubjectFilter')?.value || null;
        const year = document.getElementById('paperYearFilter')?.value || null;
        const examType = document.getElementById('paperTypeFilter')?.value || null;
        const grade = typeof getCurrentViewingGrade === 'function' ? getCurrentViewingGrade() : user.gradeLevel;

        const params = new URLSearchParams();
        if (grade) params.append('grade', grade);
        if (subject) params.append('subject', subject);
        if (year) params.append('year', year);
        if (examType) params.append('exam_type', examType);

        const endpoint = '/question-papers' + (params.toString() ? '?' + params : '');
        const papers = await API.request('GET', endpoint);

        if (papers.length) {
            await offlineDB.cache('/papers', papers);
        }

        currentPapers = papers;
        displayPapers(papers);
    } catch (error) {
        console.error('Failed to load papers:', error);
        const cached = await offlineDB.getCached('/papers');
        if (cached) displayPapers(cached);
        else displayPapers([]);
    }
}

/**
 * Display papers in UI
 */
function displayPapers(papers) {
    const container = document.getElementById('papersList');
    if (!container) return;

    if (!papers || papers.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <div class="empty-icon">📄</div>
                <p>No question papers found. Try changing filters!</p>
            </div>
        `;
        return;
    }

    container.innerHTML = papers.map(paper => `
        <div class="paper-card">
            <div class="paper-header">
                <span class="paper-year">${paper.year}</span>
                <span class="paper-type">${formatExamType(paper.exam_type)}</span>
            </div>
            <h3>${paper.title}</h3>
            <p>${paper.description || ''}</p>
            <div class="resource-meta">
                <span>📐 ${paper.subject}</span>
                <span>🎓 Grade ${paper.grade_level}</span>
                ${paper.duration_minutes ? `<span>⏱️ ${paper.duration_minutes} min</span>` : ''}
                ${paper.total_marks ? `<span>💯 ${paper.total_marks} marks</span>` : ''}
            </div>
            <div class="resource-actions">
                <button onclick="viewPaper(${paper.id})">📖 View Paper</button>
                <button onclick="downloadPaper(${paper.id})">⬇️ Download</button>
            </div>
        </div>
    `).join('');
}

/**
 * Format exam type for display
 */
function formatExamType(type) {
    const types = {
        'annual': '📅 Annual',
        'half_yearly': '📊 Half Yearly',
        'board': '🎯 Board Exam',
        'unit_test': '✏️ Unit Test'
    };
    return types[type] || type;
}

/**
 * View paper in modal - now shows PDF
 */
function viewPaper(paperId) {
    const paper = currentPapers.find(p => p.id === paperId);
    if (!paper) return;

    const pdfUrl = `/api/question-papers/${paperId}/download`;

    const html = `
        <div class="pdf-viewer-modal">
            <div class="pdf-viewer-header">
                <div>
                    <h2>${paper.title}</h2>
                    <div class="paper-meta-display">
                        <span>📐 ${paper.subject}</span>
                        <span>🎓 Grade ${paper.grade_level}</span>
                        <span>📅 Year ${paper.year}</span>
                        ${paper.duration_minutes ? `<span>⏱️ ${paper.duration_minutes} min</span>` : ''}
                        ${paper.total_marks ? `<span>💯 ${paper.total_marks} marks</span>` : ''}
                    </div>
                </div>
            </div>
            <iframe src="${pdfUrl}" class="pdf-iframe"></iframe>
            <div class="form-actions">
                <button onclick="downloadPaper(${paperId})" class="btn btn-primary">⬇️ Download</button>
                <button onclick="closeModal()" class="btn btn-secondary">Close</button>
            </div>
        </div>
    `;

    openModal(html);
}

/**
 * Download paper file
 */
function downloadPaper(paperId) {
    const paper = currentPapers.find(p => p.id === paperId);
    if (!paper) return;

    const link = document.createElement('a');
    link.href = `/api/question-papers/${paperId}/download?download=1`;
    link.download = `${paper.title}.${paper.content_type || 'pdf'}`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    Utils.showSuccess(`Downloading: ${paper.title}`);
}

/**
 * HTML escape for paper content
 */
function escapePaperHTML(str) {
    if (!str) return '';
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}

/**
 * Setup event listeners
 */
document.addEventListener('DOMContentLoaded', () => {
    const papersBtn = document.getElementById('papersBtn');
    if (papersBtn) {
        papersBtn.addEventListener('click', () => {
            switchPanel('papersPanel', papersBtn);
            loadPapers();
        });
    }

    document.getElementById('paperSubjectFilter')?.addEventListener('change', loadPapers);
    document.getElementById('paperYearFilter')?.addEventListener('change', loadPapers);
    document.getElementById('paperTypeFilter')?.addEventListener('change', loadPapers);
    document.getElementById('refreshPapers')?.addEventListener('click', loadPapers);
});

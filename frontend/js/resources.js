/**
 * Resources panel handlers
 */

let currentResources = [];

/**
 * Load and display resources
 */
async function loadResources() {
    const user = Utils.getCurrentUser();
    if (!user) return;

    try {
        const subject = document.getElementById('subjectFilter')?.value || null;
        const grade = typeof getCurrentViewingGrade === 'function' ? getCurrentViewingGrade() : (user.role === 'student' ? user.gradeLevel : null);
        const resources = await API.resources.list(grade, subject);

        if (resources.length) {
            await offlineDB.cache('/resources', resources);
        }

        currentResources = resources;
        displayResources(resources);
    } catch (error) {
        console.error('Failed to load resources:', error);
        const cached = await offlineDB.getCached('/resources');
        if (cached) displayResources(cached);
    }
}

/**
 * Display resources in the UI
 */
function displayResources(resources) {
    const container = document.getElementById('resourcesList');

    if (!resources || resources.length === 0) {
        container.innerHTML = '<p class="loading-text">No resources available yet. ' +
            (Utils.isTeacher() ? 'Click "Upload Resource" to add one!' : 'Ask your teacher to upload some!') + '</p>';
        return;
    }

    container.innerHTML = resources.map(resource => {
        const subjectClass = resource.subject.toLowerCase().replace(' ', '-');
        const subjectIcon = getSubjectIcon(resource.subject);
        const pdfBadge = resource.content_type === 'pdf' ? '<span class="pdf-badge">📄 PDF</span>' : '';
        const ytBadge = resource.youtube_url ? '<span class="yt-badge">▶ Video</span>' : '';
        const ncertBadge = resource.ncert_url ? '<span class="ncert-badge">📚 NCERT</span>' : '';

        const isOnline = navigator.onLine;
        const offlineIcon = isOnline ? '' : ' 📡';

        const youtubeBtn = resource.youtube_url ? `
            <button onclick="watchYoutube('${resource.youtube_url.replace(/'/g, "\\'")}', '${(resource.youtube_channel || 'YouTube').replace(/'/g, "\\'")}')" class="btn-youtube" ${!isOnline ? 'disabled title="Needs Internet"' : ''}>
                ▶ Watch on YouTube${offlineIcon}
            </button>
        ` : '';

        const ncertBtn = resource.ncert_url ? `
            <button onclick="openNcert('${resource.ncert_url.replace(/'/g, "\\'")}', '${(resource.ncert_chapter || 'NCERT').replace(/'/g, "\\'")}')" class="btn-ncert" ${!isOnline ? 'disabled title="Needs Internet"' : ''}>
                📚 Open NCERT Book${offlineIcon}
            </button>
        ` : '';

        return `
        <div class="resource-card" data-subject="${resource.subject}">
            <div class="card-top-meta">
                <span class="subject-badge ${subjectClass.split('-')[0]}">${subjectIcon} ${resource.subject}</span>
                <div class="badge-group">
                    ${pdfBadge}
                    ${ytBadge}
                    ${ncertBadge}
                </div>
            </div>
            <h3>${resource.title}</h3>
            <p>${resource.description || 'No description'}</p>
            ${resource.ncert_chapter ? `<p class="ncert-chapter-info">📖 ${resource.ncert_chapter}</p>` : ''}
            <div class="resource-meta">
                <span>🎓 Grade ${resource.grade_level}</span>
                <span>💾 ${Utils.formatFileSize(resource.file_size || 0)}</span>
                ${resource.youtube_channel ? `<span>📺 ${resource.youtube_channel}</span>` : ''}
            </div>
            <div class="resource-actions">
                <button onclick="viewResource(${resource.id})" class="btn-view">📖 View PDF</button>
                <button onclick="downloadResource(${resource.id})" class="btn-download">⬇️ Download</button>
            </div>
            ${ncertBtn ? `<div class="resource-actions" style="margin-top:8px;">${ncertBtn}</div>` : ''}
            ${youtubeBtn ? `<div class="resource-actions" style="margin-top:8px;">${youtubeBtn}</div>` : ''}
        </div>
    `;}).join('');
}

/**
 * Open NCERT book in new tab
 */
function openNcert(url, chapter) {
    if (!url) return;

    if (!navigator.onLine) {
        Utils.showSuccess('NCERT website needs internet. Use the built-in PDF instead!');
        return;
    }

    window.open(url, '_blank');
    Utils.showSuccess(`Opening NCERT: ${chapter}`);
}

/**
 * Pre-cache all visible PDFs for offline use
 */
async function saveAllForOffline() {
    if (!currentResources.length) {
        Utils.showSuccess('No resources to save');
        return;
    }

    const btn = document.getElementById('saveOfflineBtn');
    if (btn) {
        btn.disabled = true;
        btn.textContent = '⏳ Saving...';
    }

    let saved = 0;
    let failed = 0;

    for (const resource of currentResources) {
        try {
            // Fetch PDF - this will be cached by Service Worker
            const response = await fetch(`/api/resources/${resource.id}/download`, {
                credentials: 'include'
            });
            if (response.ok) {
                saved++;
            } else {
                failed++;
            }
        } catch (e) {
            failed++;
        }

        // Update progress
        if (btn) {
            btn.textContent = `⏳ Saving ${saved}/${currentResources.length}...`;
        }
    }

    if (btn) {
        btn.disabled = false;
        btn.textContent = '💾 Save All for Offline';
    }

    Utils.showSuccess(`Saved ${saved} PDFs for offline use! ${failed > 0 ? `(${failed} failed)` : ''}`);
}

/**
 * Watch video on YouTube
 */
function watchYoutube(url, channel) {
    if (!url) return;

    // Open in new tab
    window.open(url, '_blank');
    Utils.showSuccess(`Opening ${channel} video on YouTube...`);
}

/**
 * Get subject icon
 */
function getSubjectIcon(subject) {
    const icons = {
        'Mathematics': '📐',
        'Science': '🔬',
        'English': '📖',
        'Social Studies': '🌍',
        'Hindi': '🇮🇳',
        'Kannada': '🅺'
    };
    return icons[subject] || '📚';
}

/**
 * View resource in modal with PDF viewer
 */
function viewResource(resourceId) {
    const resource = currentResources.find(r => r.id === resourceId);
    if (!resource) return;

    const pdfUrl = `/api/resources/${resourceId}/download`;

    if (resource.content_type === 'pdf') {
        // Show PDF in embedded iframe
        const html = `
            <div class="pdf-viewer-modal">
                <div class="pdf-viewer-header">
                    <div>
                        <h2>${resource.title}</h2>
                        <div class="paper-meta-display">
                            <span>${getSubjectIcon(resource.subject)} ${resource.subject}</span>
                            <span>🎓 Grade ${resource.grade_level}</span>
                            <span>📄 PDF</span>
                        </div>
                    </div>
                </div>
                <iframe src="${pdfUrl}" class="pdf-iframe"></iframe>
                <div class="form-actions">
                    <button onclick="downloadResource(${resourceId})" class="btn btn-primary">⬇️ Download</button>
                    <button onclick="closeModal()" class="btn btn-secondary">Close</button>
                </div>
            </div>
        `;
        openModal(html);
    } else {
        // Fallback: download
        downloadResource(resourceId);
    }
}

/**
 * Download resource
 */
function downloadResource(resourceId) {
    const resource = currentResources.find(r => r.id === resourceId);
    if (!resource) return;

    const link = document.createElement('a');
    link.href = `/api/resources/${resourceId}/download?download=1`;
    link.download = `${resource.title}.${resource.content_type}`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    Utils.showSuccess(`Downloading: ${resource.title}`);
}

/**
 * Show/hide upload form
 */
function showUploadForm() {
    document.getElementById('uploadResourceForm').classList.remove('hidden');
}

function hideUploadForm() {
    document.getElementById('uploadResourceForm').classList.add('hidden');
    document.getElementById('resourceUploadForm').reset();
}

/**
 * Handle resource upload
 */
async function handleResourceUpload(e) {
    e.preventDefault();

    const title = document.getElementById('uploadTitle').value.trim();
    const description = document.getElementById('uploadDescription').value.trim();
    const subject = document.getElementById('uploadSubject').value;
    const grade = document.getElementById('uploadGrade').value;
    const file = document.getElementById('uploadFile').files[0];

    if (!title || !subject || !grade || !file) {
        Utils.showSuccess('Please fill all fields');
        return;
    }

    const formData = new FormData();
    formData.append('title', title);
    formData.append('description', description);
    formData.append('subject', subject);
    formData.append('grade_level', grade);
    formData.append('file', file);

    try {
        const result = await API.resources.upload(formData);
        if (result.resource_id) {
            Utils.showSuccess('Resource uploaded! Publishing...');
            await fetch(`/api/resources/${result.resource_id}/publish`, {
                method: 'POST',
                credentials: 'include'
            });
            Utils.showSuccess('Resource published!');
        }
        hideUploadForm();
        loadResources();
    } catch (error) {
        console.error('Upload failed:', error);
        Utils.showSuccess('Upload failed: ' + (error.message || 'Unknown error'));
    }
}

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('subjectFilter')?.addEventListener('change', loadResources);
    document.getElementById('refreshResources')?.addEventListener('click', loadResources);
    document.getElementById('uploadResourceBtn')?.addEventListener('click', showUploadForm);
    document.getElementById('cancelUpload')?.addEventListener('click', hideUploadForm);
    document.getElementById('resourceUploadForm')?.addEventListener('submit', handleResourceUpload);
});

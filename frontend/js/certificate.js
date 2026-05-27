/**
 * Certificate Generator - Creates downloadable certificates
 */

function showCertificates() {
    const user = Utils.getCurrentUser();
    if (!user) return;

    const userData = typeof getGameData === 'function' ? getGameData() : {xp: 0, level: 1, streak: 0, badges: []};

    // Determine eligible certificates
    const certificates = [];

    if (userData.quizzesCompleted >= 1) {
        certificates.push({
            id: 'quiz_starter',
            title: 'Quiz Starter Certificate',
            desc: 'Completed first quiz',
            icon: '🎯'
        });
    }

    if (userData.quizzesPassed >= 5) {
        certificates.push({
            id: 'quiz_master',
            title: 'Quiz Master Certificate',
            desc: 'Passed 5+ quizzes',
            icon: '🏆'
        });
    }

    if (userData.streak >= 7) {
        certificates.push({
            id: 'week_warrior',
            title: 'Week Warrior Certificate',
            desc: 'Maintained 7-day streak',
            icon: '🔥'
        });
    }

    if (userData.resourcesViewed >= 10) {
        certificates.push({
            id: 'avid_reader',
            title: 'Avid Reader Certificate',
            desc: 'Read 10+ resources',
            icon: '📚'
        });
    }

    if (userData.level >= 5) {
        certificates.push({
            id: 'level_5',
            title: 'Level 5 Achievement',
            desc: 'Reached Level 5',
            icon: '⭐'
        });
    }

    if (userData.badges && userData.badges.length >= 5) {
        certificates.push({
            id: 'badge_collector',
            title: 'Badge Collector Certificate',
            desc: 'Earned 5+ badges',
            icon: '🏅'
        });
    }

    // Always available
    certificates.push({
        id: 'participation',
        title: 'Participation Certificate',
        desc: 'For your dedication to learning',
        icon: '🎓'
    });

    const html = `
        <div class="certificates-container">
            <h2>📜 Your Certificates</h2>
            <p class="section-info">Download certificates for your achievements!</p>

            <div class="certificates-grid">
                ${certificates.map(cert => `
                    <div class="certificate-card">
                        <div class="cert-icon">${cert.icon}</div>
                        <h3>${cert.title}</h3>
                        <p>${cert.desc}</p>
                        <button onclick="downloadCertificate('${cert.id}', '${cert.title.replace(/'/g, "\\'")}', '${cert.desc.replace(/'/g, "\\'")}', '${cert.icon}')" class="btn btn-primary">
                            📥 Download Certificate
                        </button>
                    </div>
                `).join('')}
            </div>

            <button onclick="closeModal()" class="btn btn-secondary" style="margin-top:20px">Close</button>
        </div>
    `;

    openModal(html);
}

function downloadCertificate(id, title, desc, icon) {
    const user = Utils.getCurrentUser();
    if (!user) return;

    const today = new Date().toLocaleDateString('en-IN', {
        day: 'numeric', month: 'long', year: 'numeric'
    });

    // Create certificate HTML
    const certHtml = `
        <!DOCTYPE html>
        <html>
        <head>
            <title>${title}</title>
            <style>
                @page { size: A4 landscape; margin: 0; }
                * { box-sizing: border-box; margin: 0; padding: 0; }
                body {
                    font-family: 'Georgia', serif;
                    padding: 40px;
                    background: #f8f8f8;
                }
                .certificate {
                    background: white;
                    padding: 60px;
                    border: 8px double #4f46e5;
                    text-align: center;
                    min-height: 500px;
                    position: relative;
                    box-shadow: 0 0 50px rgba(0,0,0,0.1);
                }
                .cert-header {
                    color: #4f46e5;
                    font-size: 14px;
                    letter-spacing: 8px;
                    margin-bottom: 20px;
                }
                .cert-title {
                    font-size: 48px;
                    color: #1e293b;
                    margin: 20px 0;
                    font-weight: bold;
                    font-style: italic;
                }
                .cert-presented {
                    font-size: 18px;
                    color: #64748b;
                    margin: 20px 0;
                }
                .cert-name {
                    font-size: 42px;
                    color: #4f46e5;
                    margin: 30px 0;
                    font-weight: bold;
                    border-bottom: 2px solid #4f46e5;
                    display: inline-block;
                    padding-bottom: 10px;
                }
                .cert-desc {
                    font-size: 18px;
                    color: #475569;
                    margin: 20px 0;
                    line-height: 1.6;
                }
                .cert-icon {
                    font-size: 80px;
                    margin: 20px 0;
                }
                .cert-footer {
                    margin-top: 40px;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding-top: 20px;
                    border-top: 2px solid #e2e8f0;
                }
                .footer-item {
                    text-align: center;
                    flex: 1;
                }
                .footer-label {
                    font-size: 11px;
                    color: #94a3b8;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                    margin-top: 5px;
                }
                .signature {
                    border-top: 1px solid #1e293b;
                    padding-top: 5px;
                    font-style: italic;
                    color: #1e293b;
                }
                .cert-stamp {
                    position: absolute;
                    top: 20px;
                    right: 30px;
                    background: linear-gradient(135deg, #4f46e5, #ec4899);
                    color: white;
                    padding: 15px 25px;
                    border-radius: 50px;
                    font-weight: bold;
                    font-size: 12px;
                }
                @media print {
                    body { padding: 0; }
                    .no-print { display: none !important; }
                }
            </style>
        </head>
        <body>
            <div class="certificate">
                <div class="cert-stamp">RURAL SIKSHA</div>
                <div class="cert-header">~ CERTIFICATE OF ACHIEVEMENT ~</div>
                <div class="cert-icon">${icon}</div>
                <div class="cert-title">${title}</div>
                <div class="cert-presented">This certificate is proudly presented to</div>
                <div class="cert-name">${user.fullName}</div>
                <div class="cert-desc">in recognition of <strong>${desc}</strong></div>
                <div class="cert-desc" style="font-size:14px; color:#94a3b8;">For dedication to learning through the Rural Siksha educational platform</div>

                <div class="cert-footer">
                    <div class="footer-item">
                        <div class="signature">Rural Siksha</div>
                        <div class="footer-label">Issued By</div>
                    </div>
                    <div class="footer-item">
                        <div class="signature">${today}</div>
                        <div class="footer-label">Date Issued</div>
                    </div>
                    <div class="footer-item">
                        <div class="signature">RS-${user.id}-${Date.now().toString().slice(-6)}</div>
                        <div class="footer-label">Certificate ID</div>
                    </div>
                </div>
            </div>
            <div class="no-print" style="text-align:center; margin-top:30px;">
                <button onclick="window.print()" style="padding:12px 24px; font-size:16px; background:#4f46e5; color:white; border:none; border-radius:8px; cursor:pointer;">
                    🖨️ Print Certificate
                </button>
            </div>
        </body>
        </html>
    `;

    // Open in new window for printing/saving
    const newWindow = window.open('', '_blank');
    newWindow.document.write(certHtml);
    newWindow.document.close();

    Utils.showSuccess('Certificate opened in new window! You can print or save as PDF.');
}

/**
 * Career Guidance and Skills Development
 */

const CAREER_PATHS = [
    {
        id: 'science',
        icon: '🔬',
        title: 'Science Stream',
        description: 'Become a doctor, engineer, scientist, researcher',
        subjects: ['Physics', 'Chemistry', 'Mathematics/Biology'],
        afterClass10: 'Take Science stream in 11th-12th',
        careers: [
            { name: 'Doctor (MBBS)', exam: 'NEET', duration: '5.5 years', salary: '₹6-50 LPA' },
            { name: 'Engineer (B.Tech)', exam: 'JEE', duration: '4 years', salary: '₹4-30 LPA' },
            { name: 'Pharmacist (B.Pharm)', exam: 'State entrance', duration: '4 years', salary: '₹3-10 LPA' },
            { name: 'Scientist (B.Sc + M.Sc + PhD)', exam: 'JAM, CSIR-NET', duration: '9-11 years', salary: '₹6-25 LPA' },
            { name: 'Nurse (B.Sc Nursing)', exam: 'Various entrance', duration: '4 years', salary: '₹3-8 LPA' },
            { name: 'Agriculture Scientist', exam: 'ICAR exams', duration: '4-7 years', salary: '₹4-15 LPA' },
            { name: 'Data Scientist', exam: 'Various', duration: '4-6 years', salary: '₹6-40 LPA' },
        ]
    },
    {
        id: 'commerce',
        icon: '💼',
        title: 'Commerce Stream',
        description: 'Business, finance, accounting, management careers',
        subjects: ['Accounts', 'Economics', 'Business Studies'],
        afterClass10: 'Take Commerce stream in 11th-12th',
        careers: [
            { name: 'Chartered Accountant (CA)', exam: 'CA Foundation', duration: '4-5 years', salary: '₹7-30 LPA' },
            { name: 'Company Secretary (CS)', exam: 'CS Foundation', duration: '3-4 years', salary: '₹5-20 LPA' },
            { name: 'MBA (Manager)', exam: 'CAT, MAT', duration: '5 years', salary: '₹8-40 LPA' },
            { name: 'Bank Officer', exam: 'IBPS, SBI', duration: '3 years', salary: '₹5-15 LPA' },
            { name: 'Economist', exam: 'Various', duration: '5 years', salary: '₹5-30 LPA' },
            { name: 'Stock Broker', exam: 'NISM', duration: '3 years', salary: '₹4-20 LPA' },
            { name: 'Cost Accountant', exam: 'ICMAI', duration: '4-5 years', salary: '₹5-20 LPA' },
        ]
    },
    {
        id: 'arts',
        icon: '🎨',
        title: 'Arts/Humanities',
        description: 'Teaching, civil services, law, journalism, social work',
        subjects: ['History', 'Geography', 'Political Science', 'Sociology'],
        afterClass10: 'Take Arts stream in 11th-12th',
        careers: [
            { name: 'Civil Servant (IAS/IPS)', exam: 'UPSC CSE', duration: '5+ years', salary: '₹7-25 LPA + perks' },
            { name: 'Lawyer (LLB)', exam: 'CLAT', duration: '5 years', salary: '₹3-50 LPA' },
            { name: 'Teacher (B.Ed)', exam: 'TET, CTET', duration: '4 years', salary: '₹3-10 LPA' },
            { name: 'Journalist', exam: 'IIMC, various', duration: '3 years', salary: '₹3-15 LPA' },
            { name: 'Social Worker (MSW)', exam: 'TISSNET', duration: '5 years', salary: '₹3-10 LPA' },
            { name: 'Psychologist', exam: 'Various', duration: '5-7 years', salary: '₹4-20 LPA' },
            { name: 'Historian/Archaeologist', exam: 'UGC NET', duration: '6-8 years', salary: '₹4-12 LPA' },
        ]
    },
    {
        id: 'vocational',
        icon: '🔧',
        title: 'Vocational/Skill-Based',
        description: 'Direct skill training, ITI, polytechnic, no need for college',
        subjects: ['Any after Class 10'],
        afterClass10: 'ITI, Polytechnic, Skill courses',
        careers: [
            { name: 'Electrician', exam: 'ITI entrance', duration: '1-2 years', salary: '₹2-8 LPA' },
            { name: 'Plumber', exam: 'ITI entrance', duration: '1 year', salary: '₹2-6 LPA' },
            { name: 'Mechanic', exam: 'ITI/Diploma', duration: '1-3 years', salary: '₹2-10 LPA' },
            { name: 'Welder', exam: 'ITI entrance', duration: '1 year', salary: '₹2-7 LPA' },
            { name: 'Tailor/Fashion Designer', exam: 'NIFT', duration: '1-4 years', salary: '₹2-15 LPA' },
            { name: 'Beautician', exam: 'Skill courses', duration: '6 months', salary: '₹2-8 LPA' },
            { name: 'Computer Operator', exam: 'CCC, DOEACC', duration: '6 months', salary: '₹2-5 LPA' },
            { name: 'Photography', exam: 'Various', duration: '1-2 years', salary: '₹2-15 LPA' },
        ]
    },
    {
        id: 'government',
        icon: '🏛️',
        title: 'Government Jobs',
        description: 'Direct government employment after Class 10/12',
        subjects: ['General Knowledge, Math, English'],
        afterClass10: 'Various exams after Class 10/12',
        careers: [
            { name: 'Indian Army (Soldier)', exam: 'Army Open Bharti', duration: 'Direct', salary: '₹3-7 LPA' },
            { name: 'Indian Railways', exam: 'RRB NTPC, Group D', duration: 'Direct', salary: '₹2-8 LPA' },
            { name: 'SSC MTS', exam: 'SSC MTS', duration: 'Direct', salary: '₹2-6 LPA' },
            { name: 'Police Constable', exam: 'State Police', duration: 'Direct', salary: '₹3-7 LPA' },
            { name: 'Postal Department', exam: 'GDS, MTS', duration: 'Direct', salary: '₹2-5 LPA' },
            { name: 'Anganwadi Worker', exam: 'State exam', duration: 'Direct', salary: '₹1-3 LPA' },
            { name: 'Bank Clerk', exam: 'IBPS Clerk', duration: 'Direct', salary: '₹3-7 LPA' },
        ]
    },
    {
        id: 'agriculture',
        icon: '🌾',
        title: 'Agriculture & Rural Skills',
        description: 'Modern farming, dairy, fisheries - perfect for rural areas!',
        subjects: ['Agriculture, Science'],
        afterClass10: 'Agricultural diploma, B.Sc Agriculture',
        careers: [
            { name: 'Modern Farmer', exam: 'Agri courses', duration: 'Continuous', salary: '₹1-20 LPA' },
            { name: 'Dairy Owner', exam: 'Dairy courses', duration: 'Direct', salary: '₹2-15 LPA' },
            { name: 'Poultry Farming', exam: 'Direct', duration: 'Direct', salary: '₹1-10 LPA' },
            { name: 'Mushroom Farming', exam: 'Direct', duration: '3-6 months', salary: '₹1-8 LPA' },
            { name: 'Beekeeping', exam: 'Direct', duration: '3-6 months', salary: '₹1-5 LPA' },
            { name: 'Fisheries Officer', exam: 'B.F.Sc', duration: '4 years', salary: '₹3-10 LPA' },
            { name: 'Organic Farming', exam: 'Direct/Courses', duration: 'Continuous', salary: '₹2-15 LPA' },
            { name: 'Agri Extension Officer', exam: 'State exam', duration: '3-4 years', salary: '₹3-8 LPA' },
        ]
    }
];

const SCHOLARSHIPS = [
    {
        title: 'National Means-cum-Merit Scholarship (NMMS)',
        eligibility: 'Class 9-12, family income < ₹3.5 lakh',
        amount: '₹12,000 per year',
        website: 'https://scholarships.gov.in/'
    },
    {
        title: 'PM Yashasvi Scholarship',
        eligibility: 'Class 9-12, OBC/EBC/SC/ST/General poor students',
        amount: '₹75,000 - ₹1,25,000 per year',
        website: 'https://scholarships.gov.in/'
    },
    {
        title: 'Post Matric Scholarship',
        eligibility: 'Class 11 onwards SC/ST/OBC students',
        amount: 'Tuition fees + ₹230-1,200/month',
        website: 'https://scholarships.gov.in/'
    },
    {
        title: 'Inspire Scholarship',
        eligibility: 'Class 12 Science with 80%+ marks',
        amount: '₹80,000 per year',
        website: 'https://www.online-inspire.gov.in/'
    },
    {
        title: 'Kishore Vaigyanik Protsahan Yojana (KVPY)',
        eligibility: 'Class 11-12 Science students',
        amount: '₹5,000-7,000/month',
        website: 'http://www.kvpy.iisc.ernet.in/'
    },
    {
        title: 'Begum Hazrat Mahal Scholarship',
        eligibility: 'Class 9-12 Minority girls',
        amount: '₹5,000-12,000 per year',
        website: 'https://scholarships.gov.in/'
    },
    {
        title: 'Beti Bachao Beti Padhao',
        eligibility: 'Girl students from poor families',
        amount: 'Various',
        website: 'https://wcd.nic.in/'
    },
    {
        title: 'Rajya Puraskar Scholarship',
        eligibility: 'Top scorers in state board',
        amount: 'Varies by state',
        website: 'State education boards'
    }
];

const SKILLS = [
    {
        category: '💻 Computer Skills',
        skills: [
            { name: 'Basic Computer (MS Office)', time: '3 months', source: 'CCC, NIELIT' },
            { name: 'Tally for Accounting', time: '2 months', source: 'Tally institutes' },
            { name: 'Web Designing (HTML/CSS)', time: '3-6 months', source: 'Free online' },
            { name: 'Digital Marketing', time: '3-6 months', source: 'Google Free courses' },
            { name: 'Data Entry', time: '1-2 months', source: 'Online tutorials' },
            { name: 'Mobile App Development', time: '6-12 months', source: 'Online courses' },
        ]
    },
    {
        category: '💰 Financial Skills',
        skills: [
            { name: 'Banking Basics', time: '1 month', source: 'Bank training' },
            { name: 'GST Knowledge', time: '1-2 months', source: 'Online courses' },
            { name: 'Stock Market Basics', time: '2-3 months', source: 'NSE Academy' },
            { name: 'Personal Finance', time: '1 month', source: 'Free online' },
            { name: 'Mutual Funds', time: '1 month', source: 'AMFI' },
        ]
    },
    {
        category: '🌾 Agriculture Skills',
        skills: [
            { name: 'Modern Farming Techniques', time: '3-6 months', source: 'KVK, IGNOU' },
            { name: 'Drip Irrigation', time: '1 month', source: 'State Agri Dept' },
            { name: 'Organic Farming', time: '3 months', source: 'NCONF' },
            { name: 'Soil Testing', time: '1 month', source: 'Local KVK' },
            { name: 'Pest Management', time: '1-2 months', source: 'Agri University' },
            { name: 'Food Processing', time: '3-6 months', source: 'NIFTEM' },
        ]
    },
    {
        category: '🎨 Creative Skills',
        skills: [
            { name: 'Photography', time: '3-6 months', source: 'Online tutorials' },
            { name: 'Video Editing', time: '3-6 months', source: 'YouTube tutorials' },
            { name: 'Graphic Design', time: '6 months', source: 'Free online' },
            { name: 'Handicrafts', time: '3-6 months', source: 'Local artisans' },
            { name: 'Tailoring/Stitching', time: '3-6 months', source: 'Skill India' },
            { name: 'Beautician Course', time: '3-6 months', source: 'PMKVY' },
        ]
    },
    {
        category: '🗣️ Communication Skills',
        skills: [
            { name: 'English Speaking', time: '6 months', source: 'British Council' },
            { name: 'Public Speaking', time: '3 months', source: 'Toastmasters' },
            { name: 'Hindi-English Translation', time: '6 months', source: 'Self-study' },
            { name: 'Writing Skills', time: '3-6 months', source: 'Free online' },
        ]
    },
];

/**
 * Show career paths
 */
function showCareerPaths() {
    const container = document.getElementById('careerContent');
    container.innerHTML = `
        <div class="career-intro">
            <h2>🎯 Explore Career Options</h2>
            <p>Choose a path that matches your interests and abilities</p>
        </div>
        <div class="career-grid">
            ${CAREER_PATHS.map(path => `
                <div class="career-card" onclick="showCareerDetail('${path.id}')">
                    <div class="career-icon">${path.icon}</div>
                    <h3>${path.title}</h3>
                    <p>${path.description}</p>
                    <div class="career-info">
                        <p><strong>${path.careers.length}+</strong> career options</p>
                    </div>
                </div>
            `).join('')}
        </div>
    `;
}

function showCareerDetail(careerId) {
    const career = CAREER_PATHS.find(c => c.id === careerId);
    if (!career) return;

    const html = `
        <div class="career-detail">
            <div class="career-detail-header">
                <span class="career-icon-big">${career.icon}</span>
                <h2>${career.title}</h2>
            </div>
            <p class="career-desc">${career.description}</p>

            <h3>📚 Required Subjects:</h3>
            <p>${career.subjects.join(', ')}</p>

            <h3>📋 After Class 10:</h3>
            <p>${career.afterClass10}</p>

            <h3>💼 Career Options:</h3>
            <div class="career-options">
                ${career.careers.map(c => `
                    <div class="career-option">
                        <h4>${c.name}</h4>
                        <div class="option-meta">
                            <span>📝 Exam: ${c.exam}</span>
                            <span>⏱️ Duration: ${c.duration}</span>
                            <span>💰 Salary: ${c.salary}</span>
                        </div>
                    </div>
                `).join('')}
            </div>

            <button onclick="closeModal()" class="btn btn-primary">Close</button>
        </div>
    `;

    openModal(html);
}

/**
 * Show scholarships
 */
function showScholarships() {
    const container = document.getElementById('careerContent');
    container.innerHTML = `
        <div class="career-intro">
            <h2>💰 Scholarships for Students</h2>
            <p>Financial help is available! Don't let money stop your education.</p>
        </div>
        <div class="scholarship-list">
            ${SCHOLARSHIPS.map(s => `
                <div class="scholarship-card">
                    <h3>🏆 ${s.title}</h3>
                    <p><strong>Eligibility:</strong> ${s.eligibility}</p>
                    <p><strong>Amount:</strong> <span class="amount">${s.amount}</span></p>
                    <p><strong>Website:</strong> <a href="${s.website}" target="_blank" rel="noopener">${s.website}</a></p>
                </div>
            `).join('')}
        </div>
        <div class="info-tip">
            💡 <strong>Pro Tip:</strong> Visit your school office or local DEO for help applying for scholarships!
        </div>
    `;
}

/**
 * Show skills
 */
function showSkills() {
    const container = document.getElementById('careerContent');
    container.innerHTML = `
        <div class="career-intro">
            <h2>🛠️ Practical Skills Training</h2>
            <p>Learn skills to earn money - even without college degree</p>
        </div>
        <div class="skills-container">
            ${SKILLS.map(cat => `
                <div class="skill-category">
                    <h3>${cat.category}</h3>
                    <div class="skill-list">
                        ${cat.skills.map(s => `
                            <div class="skill-item">
                                <h4>${s.name}</h4>
                                <p>⏱️ Time: ${s.time}</p>
                                <p>📍 Source: ${s.source}</p>
                            </div>
                        `).join('')}
                    </div>
                </div>
            `).join('')}
        </div>
        <div class="info-tip">
            💡 <strong>PMKVY (Pradhan Mantri Kaushal Vikas Yojana):</strong> Government provides FREE skill training. Visit pmkvyofficial.org
        </div>
    `;
}

function switchCareerTab(tab) {
    document.querySelectorAll('.career-tab-btn').forEach(b => b.classList.remove('active'));
    document.getElementById(`career-${tab}-btn`).classList.add('active');

    switch (tab) {
        case 'paths': showCareerPaths(); break;
        case 'scholarships': showScholarships(); break;
        case 'skills': showSkills(); break;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const careerBtn = document.getElementById('careerBtn');
    if (careerBtn) {
        careerBtn.addEventListener('click', () => {
            switchPanel('careerPanel', careerBtn);
            showCareerPaths();
        });
    }
});

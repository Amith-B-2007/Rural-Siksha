/**
 * Career Guidance - PRO VERSION
 * Comprehensive career planning with AI counselor, quiz, roadmap, colleges, exams
 */

// ==================== CAREER PATHS ====================
const CAREER_PATHS = [
    {
        id: 'science',
        icon: '🔬',
        title: 'Science Stream',
        description: 'Become a doctor, engineer, scientist, researcher',
        subjects: ['Physics', 'Chemistry', 'Mathematics/Biology'],
        afterClass10: 'Take Science stream in 11th-12th',
        demand: 'Very High',
        avgSalary: '₹4-50 LPA',
        careers: [
            { name: 'Doctor (MBBS)', exam: 'NEET', duration: '5.5 years', salary: '₹6-50 LPA', growth: '📈 High' },
            { name: 'Engineer (B.Tech)', exam: 'JEE', duration: '4 years', salary: '₹4-30 LPA', growth: '📈 Very High' },
            { name: 'Software Engineer', exam: 'JEE/Private', duration: '4 years', salary: '₹6-50 LPA', growth: '📈 Very High' },
            { name: 'Pharmacist', exam: 'GPAT', duration: '4 years', salary: '₹3-10 LPA', growth: '📊 Stable' },
            { name: 'Scientist (B.Sc + M.Sc + PhD)', exam: 'JAM, CSIR-NET', duration: '9-11 years', salary: '₹6-25 LPA', growth: '📈 High' },
            { name: 'Nurse (B.Sc Nursing)', exam: 'Various entrance', duration: '4 years', salary: '₹3-8 LPA', growth: '📈 High' },
            { name: 'Agriculture Scientist', exam: 'ICAR exams', duration: '4-7 years', salary: '₹4-15 LPA', growth: '📈 High' },
            { name: 'Data Scientist', exam: 'Various', duration: '4-6 years', salary: '₹6-40 LPA', growth: '🚀 Booming' },
            { name: 'AI/ML Engineer', exam: 'JEE + Specialization', duration: '5 years', salary: '₹8-60 LPA', growth: '🚀 Booming' },
        ]
    },
    {
        id: 'commerce',
        icon: '💼',
        title: 'Commerce Stream',
        description: 'Business, finance, accounting, management',
        subjects: ['Accounts', 'Economics', 'Business Studies'],
        afterClass10: 'Take Commerce stream in 11th-12th',
        demand: 'High',
        avgSalary: '₹5-40 LPA',
        careers: [
            { name: 'Chartered Accountant (CA)', exam: 'CA Foundation', duration: '4-5 years', salary: '₹7-30 LPA', growth: '📈 High' },
            { name: 'Company Secretary (CS)', exam: 'CS Foundation', duration: '3-4 years', salary: '₹5-20 LPA', growth: '📊 Stable' },
            { name: 'MBA (Manager)', exam: 'CAT, MAT', duration: '5 years', salary: '₹8-40 LPA', growth: '📈 High' },
            { name: 'Bank Officer', exam: 'IBPS, SBI', duration: '3 years', salary: '₹5-15 LPA', growth: '📊 Stable' },
            { name: 'Economist', exam: 'Various', duration: '5 years', salary: '₹5-30 LPA', growth: '📈 High' },
            { name: 'Investment Banker', exam: 'CAT + Experience', duration: '5+ years', salary: '₹10-60 LPA', growth: '🚀 Booming' },
            { name: 'Financial Analyst', exam: 'CFA', duration: '4-5 years', salary: '₹6-25 LPA', growth: '📈 High' },
        ]
    },
    {
        id: 'arts',
        icon: '🎨',
        title: 'Arts/Humanities',
        description: 'Teaching, civil services, law, journalism',
        subjects: ['History', 'Geography', 'Political Science', 'Sociology'],
        afterClass10: 'Take Arts stream in 11th-12th',
        demand: 'Medium-High',
        avgSalary: '₹3-50 LPA',
        careers: [
            { name: 'IAS/IPS Officer', exam: 'UPSC CSE', duration: '5+ years', salary: '₹7-25 LPA + perks', growth: '🏆 Prestigious' },
            { name: 'Lawyer', exam: 'CLAT', duration: '5 years', salary: '₹3-50 LPA', growth: '📈 High' },
            { name: 'Teacher (B.Ed)', exam: 'TET, CTET', duration: '4 years', salary: '₹3-10 LPA', growth: '📊 Stable' },
            { name: 'Journalist', exam: 'IIMC, Mass Comm', duration: '3 years', salary: '₹3-15 LPA', growth: '📊 Stable' },
            { name: 'Psychologist', exam: 'Various', duration: '5-7 years', salary: '₹4-20 LPA', growth: '🚀 Booming' },
            { name: 'UPSC Officer (IFS, IRS)', exam: 'UPSC CSE', duration: '5+ years', salary: '₹8-25 LPA + perks', growth: '🏆 Prestigious' },
            { name: 'Civil Judge', exam: 'PCS-J', duration: '5-6 years', salary: '₹5-15 LPA', growth: '🏆 Prestigious' },
        ]
    },
    {
        id: 'vocational',
        icon: '🔧',
        title: 'Vocational/Skill-Based',
        description: 'Direct skill training - no college needed',
        subjects: ['Any after Class 10'],
        afterClass10: 'ITI, Polytechnic, Skill courses',
        demand: 'Very High',
        avgSalary: '₹2-15 LPA',
        careers: [
            { name: 'Electrician', exam: 'ITI entrance', duration: '1-2 years', salary: '₹2-8 LPA', growth: '📈 High' },
            { name: 'Plumber', exam: 'ITI entrance', duration: '1 year', salary: '₹2-6 LPA', growth: '📈 High' },
            { name: 'Mechanic', exam: 'ITI/Diploma', duration: '1-3 years', salary: '₹2-10 LPA', growth: '📊 Stable' },
            { name: 'Welder', exam: 'ITI entrance', duration: '1 year', salary: '₹2-7 LPA', growth: '📈 High' },
            { name: 'Fashion Designer', exam: 'NIFT', duration: '1-4 years', salary: '₹2-15 LPA', growth: '📈 High' },
            { name: 'Beautician', exam: 'Skill courses', duration: '6 months', salary: '₹2-8 LPA', growth: '🚀 Booming' },
            { name: 'Computer Operator', exam: 'CCC, DOEACC', duration: '6 months', salary: '₹2-5 LPA', growth: '📈 High' },
            { name: 'Photographer', exam: 'Various', duration: '1-2 years', salary: '₹2-15 LPA', growth: '📈 High' },
        ]
    },
    {
        id: 'government',
        icon: '🏛️',
        title: 'Government Jobs',
        description: 'Stable government employment',
        subjects: ['General Knowledge, Math, English'],
        afterClass10: 'Various exams after Class 10/12',
        demand: 'Very High',
        avgSalary: '₹3-15 LPA + perks',
        careers: [
            { name: 'Indian Army (Soldier)', exam: 'Army Open Bharti', duration: 'Direct', salary: '₹3-7 LPA + perks', growth: '🏆 Honor' },
            { name: 'Indian Railways', exam: 'RRB NTPC, Group D', duration: 'Direct', salary: '₹2-8 LPA + perks', growth: '📊 Stable' },
            { name: 'SSC MTS/CGL', exam: 'SSC', duration: 'Direct', salary: '₹3-8 LPA + perks', growth: '📊 Stable' },
            { name: 'Police Constable', exam: 'State Police', duration: 'Direct', salary: '₹3-7 LPA + perks', growth: '🏆 Honor' },
            { name: 'Postal Department', exam: 'GDS, MTS', duration: 'Direct', salary: '₹2-5 LPA + perks', growth: '📊 Stable' },
            { name: 'Bank PO', exam: 'IBPS PO', duration: 'Direct', salary: '₹5-12 LPA + perks', growth: '📈 High' },
            { name: 'Income Tax Officer', exam: 'SSC CGL', duration: 'Direct', salary: '₹5-15 LPA + perks', growth: '🏆 Prestigious' },
        ]
    },
    {
        id: 'agriculture',
        icon: '🌾',
        title: 'Agriculture & Rural Skills',
        description: 'Modern farming, dairy, fisheries - perfect for rural!',
        subjects: ['Agriculture, Science'],
        afterClass10: 'Agricultural diploma, B.Sc Agriculture',
        demand: 'Very High',
        avgSalary: '₹2-20 LPA',
        careers: [
            { name: 'Modern Farmer', exam: 'Agri courses', duration: 'Continuous', salary: '₹2-20 LPA', growth: '📈 High' },
            { name: 'Dairy Owner', exam: 'Dairy courses', duration: 'Direct', salary: '₹3-15 LPA', growth: '🚀 Booming' },
            { name: 'Poultry Farming', exam: 'Direct', duration: 'Direct', salary: '₹2-10 LPA', growth: '📈 High' },
            { name: 'Mushroom Farming', exam: 'Direct', duration: '3-6 months', salary: '₹2-8 LPA', growth: '🚀 Booming' },
            { name: 'Organic Farming', exam: 'Direct/Courses', duration: 'Continuous', salary: '₹3-15 LPA', growth: '🚀 Booming' },
            { name: 'Agri Extension Officer', exam: 'State exam', duration: '3-4 years', salary: '₹3-8 LPA', growth: '📊 Stable' },
            { name: 'Food Processing', exam: 'NIFTEM', duration: '3-4 years', salary: '₹3-15 LPA', growth: '📈 High' },
        ]
    }
];

// ==================== SCHOLARSHIPS ====================
const SCHOLARSHIPS = [
    {title: 'National Means-cum-Merit Scholarship (NMMS)', eligibility: 'Class 9-12, family income < ₹3.5 lakh', amount: '₹12,000/year', website: 'https://scholarships.gov.in/'},
    {title: 'PM Yashasvi Scholarship', eligibility: 'Class 9-12, OBC/EBC/SC/ST', amount: '₹75,000-₹1,25,000/year', website: 'https://scholarships.gov.in/'},
    {title: 'Post Matric Scholarship', eligibility: 'Class 11+ SC/ST/OBC', amount: '₹230-1,200/month + fees', website: 'https://scholarships.gov.in/'},
    {title: 'Inspire Scholarship', eligibility: 'Class 12 Science with 80%+', amount: '₹80,000/year', website: 'https://www.online-inspire.gov.in/'},
    {title: 'KVPY', eligibility: 'Class 11-12 Science', amount: '₹5,000-7,000/month', website: 'http://www.kvpy.iisc.ernet.in/'},
    {title: 'Begum Hazrat Mahal', eligibility: 'Class 9-12 Minority girls', amount: '₹5,000-12,000/year', website: 'https://scholarships.gov.in/'},
    {title: 'Pragati Scholarship (AICTE)', eligibility: 'Girl students in Engineering', amount: '₹50,000/year', website: 'https://www.aicte-india.org/'},
    {title: 'Saksham Scholarship (AICTE)', eligibility: 'Disabled students', amount: '₹50,000/year', website: 'https://www.aicte-india.org/'},
    {title: 'Central Sector Scholarship', eligibility: 'Top 80% in Class 12', amount: '₹10,000-20,000/year', website: 'https://scholarships.gov.in/'},
    {title: 'CBSE Merit Scholarship for Girls', eligibility: 'Class 10 CBSE toppers (girls)', amount: '₹500/month', website: 'https://www.cbse.gov.in/'},
];

// ==================== TOP COLLEGES ====================
const TOP_COLLEGES = {
    engineering: [
        {name: 'IIT Bombay', city: 'Mumbai', exam: 'JEE Advanced', fees: '₹2 lakh/year', ranking: 1, type: 'Engineering'},
        {name: 'IIT Delhi', city: 'Delhi', exam: 'JEE Advanced', fees: '₹2 lakh/year', ranking: 2, type: 'Engineering'},
        {name: 'IIT Madras', city: 'Chennai', exam: 'JEE Advanced', fees: '₹2 lakh/year', ranking: 3, type: 'Engineering'},
        {name: 'IIT Kanpur', city: 'Kanpur', exam: 'JEE Advanced', fees: '₹2 lakh/year', ranking: 4, type: 'Engineering'},
        {name: 'NIT Trichy', city: 'Tiruchirappalli', exam: 'JEE Main', fees: '₹1.5 lakh/year', ranking: 5, type: 'Engineering'},
        {name: 'BITS Pilani', city: 'Pilani', exam: 'BITSAT', fees: '₹4 lakh/year', ranking: 6, type: 'Engineering'},
    ],
    medical: [
        {name: 'AIIMS Delhi', city: 'Delhi', exam: 'NEET', fees: '₹6,000/year', ranking: 1, type: 'Medical'},
        {name: 'CMC Vellore', city: 'Vellore', exam: 'NEET', fees: '₹50,000/year', ranking: 2, type: 'Medical'},
        {name: 'KGMU', city: 'Lucknow', exam: 'NEET', fees: '₹54,000/year', ranking: 3, type: 'Medical'},
        {name: 'JIPMER', city: 'Puducherry', exam: 'NEET', fees: '₹15,000/year', ranking: 4, type: 'Medical'},
        {name: 'AIIMS Bhopal/Patna', city: 'Various', exam: 'NEET', fees: '₹6,000/year', ranking: 5, type: 'Medical'},
    ],
    commerce: [
        {name: 'Shri Ram College (DU)', city: 'Delhi', exam: 'CUET', fees: '₹50,000/year', ranking: 1, type: 'Commerce'},
        {name: 'Hindu College (DU)', city: 'Delhi', exam: 'CUET', fees: '₹40,000/year', ranking: 2, type: 'Commerce'},
        {name: 'Loyola College', city: 'Chennai', exam: 'Various', fees: '₹30,000/year', ranking: 3, type: 'Commerce'},
        {name: 'St. Xavier\'s', city: 'Mumbai', exam: 'Various', fees: '₹40,000/year', ranking: 4, type: 'Commerce'},
    ],
    arts: [
        {name: 'JNU', city: 'Delhi', exam: 'CUET', fees: '₹500/year', ranking: 1, type: 'Arts'},
        {name: 'St. Stephen\'s (DU)', city: 'Delhi', exam: 'CUET', fees: '₹30,000/year', ranking: 2, type: 'Arts'},
        {name: 'Presidency University', city: 'Kolkata', exam: 'PUBDET', fees: '₹15,000/year', ranking: 3, type: 'Arts'},
        {name: 'Lady Shri Ram College', city: 'Delhi', exam: 'CUET', fees: '₹40,000/year', ranking: 4, type: 'Arts'},
    ],
    management: [
        {name: 'IIM Ahmedabad', city: 'Ahmedabad', exam: 'CAT', fees: '₹25 lakh', ranking: 1, type: 'MBA'},
        {name: 'IIM Bangalore', city: 'Bangalore', exam: 'CAT', fees: '₹24 lakh', ranking: 2, type: 'MBA'},
        {name: 'IIM Calcutta', city: 'Kolkata', exam: 'CAT', fees: '₹25 lakh', ranking: 3, type: 'MBA'},
        {name: 'XLRI Jamshedpur', city: 'Jamshedpur', exam: 'XAT', fees: '₹25 lakh', ranking: 4, type: 'MBA'},
    ],
};

// ==================== ENTRANCE EXAMS CALENDAR ====================
const ENTRANCE_EXAMS = [
    {name: 'JEE Main', month: 'Jan & April', for: 'Engineering', conducted: 'NTA', age: 'Class 12 pass'},
    {name: 'JEE Advanced', month: 'May', for: 'IITs', conducted: 'IIT', age: 'Top 2.5 lakh JEE Main'},
    {name: 'NEET UG', month: 'May', for: 'Medical (MBBS)', conducted: 'NTA', age: '17+'},
    {name: 'CUET UG', month: 'May-June', for: 'Central Univ', conducted: 'NTA', age: 'Class 12'},
    {name: 'CAT', month: 'November', for: 'MBA (IIMs)', conducted: 'IIMs', age: 'Graduate'},
    {name: 'CLAT', month: 'May', for: 'Law', conducted: 'NLU', age: 'Class 12'},
    {name: 'UPSC Civil Services', month: 'May', for: 'IAS/IPS/IFS', conducted: 'UPSC', age: '21-32'},
    {name: 'GATE', month: 'February', for: 'M.Tech/PSU', conducted: 'IIT/IISc', age: 'Engineering grad'},
    {name: 'NDA', month: 'April & September', for: 'Armed Forces', conducted: 'UPSC', age: '16.5-19.5'},
    {name: 'SSC CGL', month: 'July', for: 'Govt Jobs', conducted: 'SSC', age: 'Graduate'},
    {name: 'IBPS PO', month: 'September', for: 'Bank Officer', conducted: 'IBPS', age: 'Graduate'},
    {name: 'BITSAT', month: 'May-June', for: 'BITS Pilani', conducted: 'BITS', age: 'Class 12'},
];

// ==================== SUCCESS STORIES ====================
const SUCCESS_STORIES = [
    {
        name: 'Dr. APJ Abdul Kalam',
        from: 'Rameswaram, Tamil Nadu (small town)',
        became: 'Missile Man of India, 11th President',
        story: 'Born to a boat owner, sold newspapers to fund education. Became aerospace scientist, led India\'s missile program, and became President of India.',
        icon: '🚀'
    },
    {
        name: 'Sundar Pichai',
        from: 'Madurai, Tamil Nadu',
        became: 'CEO of Google & Alphabet',
        story: 'Family didn\'t have a phone until he was 12. Studied at IIT Kharagpur with scholarship, then Stanford. Now leads one of world\'s largest companies.',
        icon: '💻'
    },
    {
        name: 'Anand Kumar (Super 30)',
        from: 'Patna, Bihar',
        became: 'Founder of Super 30 (IIT coaching)',
        story: 'From poor family, couldn\'t afford Cambridge admission. Started teaching 30 poor students for free for IIT-JEE. Most succeeded - now world-famous.',
        icon: '🎓'
    },
    {
        name: 'Tina Dabi',
        from: 'Bhopal, MP',
        became: 'IAS Officer (Rank 1 in UPSC 2015)',
        story: 'Born to ordinary family, cracked UPSC at age 22. Became youngest IAS officer. Inspiration to lakhs of students from non-metro cities.',
        icon: '🏛️'
    },
    {
        name: 'Mary Kom',
        from: 'Manipur (rural area)',
        became: 'Olympic Boxer, 6x World Champion',
        story: 'Daughter of poor farmers. Started boxing at 18 against family wishes. Won 6 World Championships and Olympic medal. Member of Parliament.',
        icon: '🥊'
    },
    {
        name: 'Manoj Kumar Sharma',
        from: 'Bilgaon village, MP',
        became: 'IPS Officer (Real-life 12th Fail)',
        story: 'Failed Class 12. Worked as auto driver, did petty jobs. Studied hard, cleared UPSC in 4th attempt. Now IPS officer. Story in movie "12th Fail".',
        icon: '👮'
    },
];

// ==================== SKILLS ====================
const SKILLS = [
    {category: '💻 Computer Skills', skills: [
        {name: 'Basic Computer (MS Office)', time: '3 months', source: 'CCC, NIELIT', salary: '₹2-4 LPA'},
        {name: 'Tally for Accounting', time: '2 months', source: 'Tally institutes', salary: '₹2-5 LPA'},
        {name: 'Web Designing (HTML/CSS)', time: '3-6 months', source: 'Free online', salary: '₹3-8 LPA'},
        {name: 'Digital Marketing', time: '3-6 months', source: 'Google Free', salary: '₹3-12 LPA'},
        {name: 'Python Programming', time: '6 months', source: 'YouTube/Coursera', salary: '₹5-15 LPA'},
        {name: 'Mobile App Development', time: '6-12 months', source: 'Online courses', salary: '₹5-20 LPA'},
    ]},
    {category: '💰 Financial Skills', skills: [
        {name: 'Banking Basics', time: '1 month', source: 'Bank training', salary: '₹2-5 LPA'},
        {name: 'GST Knowledge', time: '1-2 months', source: 'Online courses', salary: '₹3-6 LPA'},
        {name: 'Stock Market Basics', time: '2-3 months', source: 'NSE Academy', salary: '₹3-10 LPA'},
        {name: 'Personal Finance', time: '1 month', source: 'Free online', salary: '-'},
    ]},
    {category: '🌾 Agriculture Skills', skills: [
        {name: 'Modern Farming', time: '3-6 months', source: 'KVK, IGNOU', salary: '₹2-10 LPA'},
        {name: 'Drip Irrigation', time: '1 month', source: 'State Agri Dept', salary: '-'},
        {name: 'Organic Farming', time: '3 months', source: 'NCONF', salary: '₹3-15 LPA'},
        {name: 'Soil Testing', time: '1 month', source: 'Local KVK', salary: '-'},
        {name: 'Food Processing', time: '3-6 months', source: 'NIFTEM', salary: '₹3-10 LPA'},
    ]},
    {category: '🎨 Creative Skills', skills: [
        {name: 'Photography', time: '3-6 months', source: 'YouTube tutorials', salary: '₹2-15 LPA'},
        {name: 'Video Editing', time: '3-6 months', source: 'YouTube tutorials', salary: '₹3-15 LPA'},
        {name: 'Graphic Design', time: '6 months', source: 'Free online', salary: '₹3-12 LPA'},
        {name: 'Tailoring', time: '3-6 months', source: 'Skill India', salary: '₹2-6 LPA'},
        {name: 'Beautician', time: '3-6 months', source: 'PMKVY', salary: '₹2-8 LPA'},
    ]},
];

// ==================== CAREER QUIZ ====================
const CAREER_QUIZ = [
    {q: 'What interests you most?', options: [
        {text: 'Solving math problems', career: 'science'},
        {text: 'Reading stories and writing', career: 'arts'},
        {text: 'Managing money and business', career: 'commerce'},
        {text: 'Working with hands/tools', career: 'vocational'},
        {text: 'Growing plants or farming', career: 'agriculture'}
    ]},
    {q: 'What do you enjoy doing in free time?', options: [
        {text: 'Conducting experiments', career: 'science'},
        {text: 'Writing or debating', career: 'arts'},
        {text: 'Trading or business games', career: 'commerce'},
        {text: 'Fixing things at home', career: 'vocational'},
        {text: 'Visiting farms/gardens', career: 'agriculture'}
    ]},
    {q: 'Which subject is your favorite?', options: [
        {text: 'Mathematics/Physics/Chemistry', career: 'science'},
        {text: 'History/Geography/Literature', career: 'arts'},
        {text: 'Economics/Accounts', career: 'commerce'},
        {text: 'I prefer practical work', career: 'vocational'},
        {text: 'Biology/Agriculture', career: 'agriculture'}
    ]},
    {q: 'What kind of work environment do you prefer?', options: [
        {text: 'Lab/Hospital/Research', career: 'science'},
        {text: 'Office/Government/Schools', career: 'arts'},
        {text: 'Banks/Corporate offices', career: 'commerce'},
        {text: 'Workshop/Site work', career: 'vocational'},
        {text: 'Outdoors/Fields', career: 'agriculture'}
    ]},
    {q: 'What is your main goal?', options: [
        {text: 'Make scientific discoveries', career: 'science'},
        {text: 'Serve society/Govt service', career: 'arts'},
        {text: 'Build wealth/Be entrepreneur', career: 'commerce'},
        {text: 'Independent skilled work', career: 'vocational'},
        {text: 'Modernize farming/Rural growth', career: 'agriculture'}
    ]},
    {q: 'How much do you like studying for long hours?', options: [
        {text: 'Love it - I can study 8+ hours', career: 'science'},
        {text: 'Yes, reading and writing daily', career: 'arts'},
        {text: 'Yes, with numbers/cases', career: 'commerce'},
        {text: 'Prefer hands-on learning', career: 'vocational'},
        {text: 'Mix of theory and practical', career: 'agriculture'}
    ]},
    {q: 'Where do you see yourself in 10 years?', options: [
        {text: 'In a lab/hospital saving lives', career: 'science'},
        {text: 'Govt officer/Teacher/Lawyer', career: 'arts'},
        {text: 'CEO/Manager/Business owner', career: 'commerce'},
        {text: 'Skilled professional/Shop owner', career: 'vocational'},
        {text: 'Successful farmer/Agri-business', career: 'agriculture'}
    ]},
    {q: 'What kind of impact do you want to make?', options: [
        {text: 'Discover new things', career: 'science'},
        {text: 'Help society/Change laws', career: 'arts'},
        {text: 'Create wealth/Jobs', career: 'commerce'},
        {text: 'Provide essential services', career: 'vocational'},
        {text: 'Feed the nation/Sustainability', career: 'agriculture'}
    ]},
    {q: 'How comfortable are you with risks?', options: [
        {text: 'Open to research challenges', career: 'science'},
        {text: 'Prefer stable career', career: 'arts'},
        {text: 'Love calculated risks', career: 'commerce'},
        {text: 'Steady, hands-on work', career: 'vocational'},
        {text: 'Some risk for big rewards', career: 'agriculture'}
    ]},
    {q: 'Your dream salary range?', options: [
        {text: '₹15+ LPA (top doctor/engineer)', career: 'science'},
        {text: '₹8-25 LPA + Govt benefits', career: 'arts'},
        {text: '₹15-50+ LPA (CA/MBA/Banker)', career: 'commerce'},
        {text: '₹3-10 LPA (Steady job)', career: 'vocational'},
        {text: '₹5-20 LPA (Modern farming)', career: 'agriculture'}
    ]},
];

let quizAnswers = [];
let quizCurrentQ = 0;

function showCareerPaths() {
    console.log('Loading career paths...');
    const container = document.getElementById('careerContent');
    if (!container) {
        console.error('careerContent container not found!');
        return;
    }
    // Reset active tab to paths
    document.querySelectorAll('.career-tab-btn').forEach(b => b.classList.remove('active'));
    const pathsBtn = document.getElementById('career-paths-btn');
    if (pathsBtn) pathsBtn.classList.add('active');

    container.innerHTML = `
        <div class="career-intro">
            <h2>🎯 Explore Career Options</h2>
            <p>Click any career stream to see detailed paths, exams, and salaries</p>
            <div class="career-banner-stats">
                <div><strong>${CAREER_PATHS.length}</strong> Streams</div>
                <div><strong>${CAREER_PATHS.reduce((s,p) => s + p.careers.length, 0)}+</strong> Careers</div>
                <div><strong>₹2-60</strong> LPA Range</div>
            </div>
        </div>
        <div class="career-grid">
            ${CAREER_PATHS.map(path => `
                <div class="career-card" onclick="showCareerDetail('${path.id}')">
                    <div class="career-icon">${path.icon}</div>
                    <h3>${path.title}</h3>
                    <p>${path.description}</p>
                    <div class="career-meta">
                        <span class="meta-badge demand">📊 ${path.demand}</span>
                        <span class="meta-badge salary">💰 ${path.avgSalary}</span>
                    </div>
                    <div class="career-info">
                        <p><strong>${path.careers.length}+</strong> career options available</p>
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

            <div class="career-quick-info">
                <div class="quick-info-item"><strong>📊 Demand:</strong> ${career.demand}</div>
                <div class="quick-info-item"><strong>💰 Salary Range:</strong> ${career.avgSalary}</div>
                <div class="quick-info-item"><strong>📚 Subjects:</strong> ${career.subjects.join(', ')}</div>
                <div class="quick-info-item"><strong>📋 After Class 10:</strong> ${career.afterClass10}</div>
            </div>

            <h3>💼 Career Options (${career.careers.length}):</h3>
            <div class="career-options">
                ${career.careers.map(c => `
                    <div class="career-option">
                        <div class="option-header">
                            <h4>${c.name}</h4>
                            <span class="growth-badge">${c.growth}</span>
                        </div>
                        <div class="option-meta">
                            <span>📝 ${c.exam}</span>
                            <span>⏱️ ${c.duration}</span>
                            <span class="salary-tag">💰 ${c.salary}</span>
                        </div>
                    </div>
                `).join('')}
            </div>

            <div class="career-actions" style="margin-top:20px; display:flex; gap:10px; flex-wrap:wrap;">
                <button onclick="askAICareerAdvice('${career.id}')" class="btn btn-primary">🤖 Get AI Advice</button>
                <button onclick="closeModal()" class="btn btn-secondary">Close</button>
            </div>
        </div>
    `;
    openModal(html);
}

async function askAICareerAdvice(careerId) {
    const career = CAREER_PATHS.find(c => c.id === careerId);
    if (!career) return;

    closeModal();
    if (typeof toast !== 'undefined') toast.info('🤖 Getting personalized career advice from AI...');

    try {
        const user = Utils.getCurrentUser();
        const grade = user?.gradeLevel || 10;
        const prompt = `I am a Class ${grade} student interested in ${career.title}. Give me 5 practical tips for success in this career, including study tips, exam preparation, and skill development. Keep it concise and helpful for a rural Indian student.`;

        const response = await API.doubts.create(prompt, '', 'Career Guidance', grade);

        if (response.ai_response) {
            openModal(`
                <div class="ai-advice">
                    <h2>🤖 AI Career Advice: ${career.title}</h2>
                    <div class="ai-response-box">
                        <pre style="white-space:pre-wrap; font-family:inherit; line-height:1.7;">${response.ai_response}</pre>
                    </div>
                    <button onclick="closeModal(); showCareerDetail('${careerId}');" class="btn btn-secondary">← Back</button>
                    <button onclick="closeModal()" class="btn btn-primary">Close</button>
                </div>
            `);
        }
    } catch (e) {
        if (typeof toast !== 'undefined') toast.error('AI is unavailable. Please try again.');
    }
}

function showScholarships() {
    const container = document.getElementById('careerContent');
    container.innerHTML = `
        <div class="career-intro">
            <h2>💰 Scholarships for Students</h2>
            <p>${SCHOLARSHIPS.length}+ scholarships available. Don't let money stop your education!</p>
        </div>
        <div class="scholarship-list">
            ${SCHOLARSHIPS.map(s => `
                <div class="scholarship-card">
                    <h3>🏆 ${s.title}</h3>
                    <p><strong>Eligibility:</strong> ${s.eligibility}</p>
                    <p><strong>Amount:</strong> <span class="amount">${s.amount}</span></p>
                    <p><strong>Apply at:</strong> <a href="${s.website}" target="_blank" rel="noopener">${s.website}</a></p>
                </div>
            `).join('')}
        </div>
        <div class="info-tip">
            💡 <strong>Pro Tip:</strong> Apply for multiple scholarships! Visit your school office or local DEO for help applying.
        </div>
    `;
}

function showSkills() {
    const container = document.getElementById('careerContent');
    container.innerHTML = `
        <div class="career-intro">
            <h2>🛠️ Practical Skills Training</h2>
            <p>Learn skills to earn money - even without college degree!</p>
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
                                <p>💰 Salary: <span style="color:var(--success);font-weight:600">${s.salary}</span></p>
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

function showColleges() {
    const container = document.getElementById('careerContent');
    container.innerHTML = `
        <div class="career-intro">
            <h2>🏛️ Top Colleges in India</h2>
            <p>Premier institutions for your career path</p>
        </div>
        <div class="colleges-tabs">
            <button onclick="renderColleges('engineering')" class="college-tab-btn active">🔧 Engineering (IITs/NITs)</button>
            <button onclick="renderColleges('medical')" class="college-tab-btn">⚕️ Medical (AIIMS)</button>
            <button onclick="renderColleges('commerce')" class="college-tab-btn">💼 Commerce</button>
            <button onclick="renderColleges('arts')" class="college-tab-btn">🎨 Arts</button>
            <button onclick="renderColleges('management')" class="college-tab-btn">📊 Management (IIMs)</button>
        </div>
        <div id="collegesGrid"></div>
        <div class="info-tip">
            💡 <strong>Reservation:</strong> SC/ST/OBC/EWS students get reserved seats in central institutions!
        </div>
    `;
    renderColleges('engineering');
}

function renderColleges(category) {
    document.querySelectorAll('.college-tab-btn').forEach(b => b.classList.remove('active'));
    event && event.target && event.target.classList.add('active');

    const colleges = TOP_COLLEGES[category] || [];
    const html = colleges.map(c => `
        <div class="college-card">
            <div class="college-rank">#${c.ranking}</div>
            <h3>${c.name}</h3>
            <div class="college-info">
                <span>📍 ${c.city}</span>
                <span>📝 ${c.exam}</span>
                <span>💰 ${c.fees}</span>
            </div>
        </div>
    `).join('');
    document.getElementById('collegesGrid').innerHTML = `<div class="colleges-grid">${html}</div>`;
}

function showExams() {
    const container = document.getElementById('careerContent');
    container.innerHTML = `
        <div class="career-intro">
            <h2>📅 Entrance Exam Calendar</h2>
            <p>Important exams and when they happen</p>
        </div>
        <div class="exams-grid">
            ${ENTRANCE_EXAMS.map(e => `
                <div class="exam-card">
                    <div class="exam-month">${e.month}</div>
                    <h3>${e.name}</h3>
                    <div class="exam-details">
                        <div><strong>For:</strong> ${e.for}</div>
                        <div><strong>Conducted by:</strong> ${e.conducted}</div>
                        <div><strong>Eligibility:</strong> ${e.age}</div>
                    </div>
                </div>
            `).join('')}
        </div>
        <div class="info-tip">
            💡 <strong>Start Early!</strong> Most students start preparing 2-3 years before their target exam.
        </div>
    `;
}

function showSuccessStories() {
    const container = document.getElementById('careerContent');
    container.innerHTML = `
        <div class="career-intro">
            <h2>🌟 Inspirational Success Stories</h2>
            <p>Real people from humble backgrounds who achieved greatness</p>
        </div>
        <div class="stories-grid">
            ${SUCCESS_STORIES.map(s => `
                <div class="story-card">
                    <div class="story-icon">${s.icon}</div>
                    <h3>${s.name}</h3>
                    <p class="story-from"><strong>From:</strong> ${s.from}</p>
                    <p class="story-became"><strong>Became:</strong> ${s.became}</p>
                    <p class="story-text">${s.story}</p>
                </div>
            `).join('')}
        </div>
        <div class="info-tip">
            💪 <strong>Remember:</strong> Your background doesn't determine your future. Hard work and dedication do!
        </div>
    `;
}

function startCareerQuiz() {
    quizAnswers = [];
    quizCurrentQ = 0;
    showQuizQuestion();
}

function showQuizQuestion() {
    if (quizCurrentQ >= CAREER_QUIZ.length) {
        showQuizResult();
        return;
    }

    const q = CAREER_QUIZ[quizCurrentQ];
    const html = `
        <div class="career-quiz">
            <h2>🧠 Career Aptitude Quiz</h2>
            <div class="quiz-progress">
                <div class="quiz-progress-bar">
                    <div class="quiz-progress-fill" style="width: ${((quizCurrentQ + 1) / CAREER_QUIZ.length) * 100}%"></div>
                </div>
                <p>Question ${quizCurrentQ + 1} of ${CAREER_QUIZ.length}</p>
            </div>
            <h3 class="quiz-q">${q.q}</h3>
            <div class="quiz-quiz-options">
                ${q.options.map((opt, idx) => `
                    <button onclick="answerCareerQ('${opt.career}')" class="quiz-quiz-option">
                        ${opt.text}
                    </button>
                `).join('')}
            </div>
            ${quizCurrentQ > 0 ? '<button onclick="prevQuizQ()" class="btn btn-secondary">← Previous</button>' : ''}
            <button onclick="closeModal()" class="btn-skip-quiz">Cancel</button>
        </div>
    `;
    openModal(html);
}

function answerCareerQ(careerId) {
    quizAnswers.push(careerId);
    quizCurrentQ++;
    showQuizQuestion();
}

function prevQuizQ() {
    if (quizCurrentQ > 0) {
        quizCurrentQ--;
        quizAnswers.pop();
        showQuizQuestion();
    }
}

function showQuizResult() {
    // Count votes
    const counts = {};
    quizAnswers.forEach(c => counts[c] = (counts[c] || 0) + 1);

    // Find top career
    let topCareer = quizAnswers[0];
    let maxCount = 0;
    for (const [c, count] of Object.entries(counts)) {
        if (count > maxCount) {
            maxCount = count;
            topCareer = c;
        }
    }

    const recommended = CAREER_PATHS.find(p => p.id === topCareer);
    if (!recommended) return;

    const html = `
        <div class="quiz-result">
            <h2>🎉 Quiz Complete!</h2>
            <p class="section-info">Based on your answers, here's your best career match:</p>

            <div class="result-card">
                <div class="result-icon-big">${recommended.icon}</div>
                <h2>${recommended.title}</h2>
                <p>${recommended.description}</p>
                <div class="match-percent">${Math.round((maxCount / CAREER_QUIZ.length) * 100)}% Match</div>
            </div>

            <div class="other-matches">
                <h3>📊 Your Other Interests:</h3>
                ${Object.entries(counts)
                    .sort((a, b) => b[1] - a[1])
                    .slice(0, 4)
                    .map(([c, count]) => {
                        const career = CAREER_PATHS.find(p => p.id === c);
                        return career ? `
                            <div class="match-item">
                                <span>${career.icon} ${career.title}</span>
                                <span>${Math.round(count / CAREER_QUIZ.length * 100)}%</span>
                            </div>
                        ` : '';
                    }).join('')}
            </div>

            <div class="quiz-actions">
                <button onclick="closeModal(); showCareerDetail('${topCareer}');" class="btn btn-primary">📚 Explore ${recommended.title}</button>
                <button onclick="startCareerQuiz()" class="btn btn-secondary">🔄 Retake Quiz</button>
                <button onclick="closeModal()" class="btn-skip-quiz">Close</button>
            </div>
        </div>
    `;
    openModal(html);
}

function switchCareerTab(tab) {
    document.querySelectorAll('.career-tab-btn').forEach(b => b.classList.remove('active'));
    const btn = document.getElementById(`career-${tab}-btn`);
    if (btn) btn.classList.add('active');

    switch (tab) {
        case 'paths': showCareerPaths(); break;
        case 'quiz':
            startCareerQuiz();
            // Show career paths in background
            showCareerPaths();
            break;
        case 'colleges': showColleges(); break;
        case 'exams': showExams(); break;
        case 'scholarships': showScholarships(); break;
        case 'skills': showSkills(); break;
        case 'stories': showSuccessStories(); break;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    // Multiple ways to access career section
    const careerBtn = document.getElementById('careerBtn');
    if (careerBtn) {
        careerBtn.addEventListener('click', () => {
            if (typeof switchPanel === 'function') {
                switchPanel('careerPanel', careerBtn);
            }
            showCareerPaths();
        });
    }

    // Auto-init when career panel becomes visible (via MutationObserver)
    const careerPanel = document.getElementById('careerPanel');
    if (careerPanel) {
        const observer = new MutationObserver((mutations) => {
            mutations.forEach((m) => {
                if (m.attributeName === 'class') {
                    if (careerPanel.classList.contains('active')) {
                        // Check if content is still showing loading text
                        const content = document.getElementById('careerContent');
                        if (content && (content.innerHTML.includes('Loading career info') || content.innerHTML.trim() === '')) {
                            console.log('Career panel activated, loading paths...');
                            setTimeout(() => showCareerPaths(), 100);
                        }
                    }
                }
            });
        });
        observer.observe(careerPanel, {attributes: true});
    }
});

// Global init function for external calls
window.initCareer = function() {
    showCareerPaths();
};

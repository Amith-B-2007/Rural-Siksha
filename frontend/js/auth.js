/**
 * Authentication handlers
 */

document.addEventListener('DOMContentLoaded', () => {
    // Tab switching
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.auth-tab').forEach(t => t.classList.remove('active'));
            e.target.classList.add('active');
            const tab = e.target.dataset.tab;
            document.getElementById(tab + 'Tab').classList.add('active');
        });
    });

    // Role selector
    document.querySelectorAll('.role-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            // Use currentTarget to always get the button (not inner span)
            const targetBtn = e.currentTarget;
            document.querySelectorAll('.role-btn').forEach(b => b.classList.remove('active'));
            targetBtn.classList.add('active');
            const role = targetBtn.dataset.role;
            updateRegisterForm(role);
        });
    });

    // Login form
    document.getElementById('loginForm').addEventListener('submit', handleLogin);

    // Register form
    document.getElementById('registerForm').addEventListener('submit', handleRegister);

    // Check if already logged in
    checkAuthStatus();
});

/**
 * Update register form based on role
 */
function updateRegisterForm(role) {
    const studentFields = document.getElementById('studentFields');
    const teacherFields = document.getElementById('teacherFields');

    if (role === 'student') {
        studentFields.classList.remove('hidden');
        teacherFields.classList.add('hidden');
    } else if (role === 'teacher') {
        studentFields.classList.add('hidden');
        teacherFields.classList.remove('hidden');
    } else if (role === 'parent') {
        // Parents don't need grade or subject
        studentFields.classList.add('hidden');
        teacherFields.classList.add('hidden');
    }
}

/**
 * Handle login
 */
async function handleLogin(e) {
    e.preventDefault();

    const email = document.getElementById('loginEmail').value.trim();
    const password = document.getElementById('loginPassword').value;
    const errorEl = document.getElementById('loginError');

    Utils.clearError('loginError');

    if (!email || !password) {
        Utils.showError('loginError', 'Email and password are required');
        return;
    }

    try {
        console.log('Logging in:', email);
        const response = await API.auth.login(email, password);
        console.log('Login response:', response);

        // Store user info
        Utils.setCurrentUser({
            id: response.user_id,
            email: response.email,
            fullName: response.full_name,
            role: response.role,
            gradeLevel: response.grade_level,
            subject: response.subject
        });

        // Switch to dashboard
        document.getElementById('authScreen').classList.remove('active');
        document.getElementById('dashboardScreen').classList.add('active');

        // Load initial data (errors here shouldn't fail login)
        try {
            await loadDashboard();
        } catch (dashErr) {
            console.error('Dashboard load error (not blocking):', dashErr);
        }

        console.log('Login successful!');
    } catch (error) {
        console.error('Login error:', error);
        Utils.showError('loginError', error.message || 'Login failed');
    }
}

/**
 * Handle registration
 */
async function handleRegister(e) {
    e.preventDefault();

    const email = document.getElementById('regEmail').value.trim();
    const fullName = document.getElementById('regFullName').value.trim();
    const password = document.getElementById('regPassword').value;
    const role = document.querySelector('.role-btn.active').dataset.role;
    const errorEl = document.getElementById('regError');

    Utils.clearError('regError');

    if (!email || !fullName || !password) {
        Utils.showError('regError', 'All fields are required');
        return;
    }

    const extraData = {};
    if (role === 'student') {
        const gradeLevel = document.getElementById('regGrade').value;
        if (!gradeLevel) {
            Utils.showError('regError', 'Please select a grade');
            return;
        }
        extraData.grade_level = parseInt(gradeLevel);
    } else if (role === 'teacher') {
        const subject = document.getElementById('regSubject').value;
        if (!subject) {
            Utils.showError('regError', 'Please select a subject');
            return;
        }
        extraData.subject = subject;
    }
    // For 'parent' role, no extra data needed

    try {
        const response = await API.auth.register(email, password, fullName, role, extraData);

        // Store user info
        Utils.setCurrentUser({
            id: response.user_id,
            email: response.email,
            fullName,
            role,
            gradeLevel: extraData.grade_level,
            subject: extraData.subject
        });

        Utils.showSuccess('Account created successfully!');

        // Switch to dashboard
        document.getElementById('authScreen').classList.remove('active');
        document.getElementById('dashboardScreen').classList.add('active');

        // Load initial data
        await loadDashboard();
    } catch (error) {
        Utils.showError('regError', error.message || 'Registration failed');
    }
}

/**
 * Check if user is already logged in
 */
async function checkAuthStatus() {
    const user = Utils.getCurrentUser();
    if (user) {
        try {
            // Verify session is still valid
            await API.auth.me();
            document.getElementById('authScreen').classList.remove('active');
            document.getElementById('dashboardScreen').classList.add('active');
            await loadDashboard();
        } catch (error) {
            // Session expired
            Utils.clearCurrentUser();
        }
    }
}

/**
 * Handle logout
 */
async function handleLogout() {
    console.log('Logging out...');

    // Try server logout first
    try {
        await API.auth.logout();
    } catch (error) {
        console.error('Server logout error (continuing anyway):', error);
    }

    // Clear local data regardless of server response
    try {
        Utils.clearCurrentUser();
    } catch (e) {
        console.error('Error clearing user:', e);
        localStorage.removeItem('currentUser');
    }

    try {
        if (typeof offlineDB !== 'undefined' && offlineDB.clear) {
            await offlineDB.clear();
        }
    } catch (e) {
        console.error('Error clearing offline DB:', e);
    }

    // Reset navbar visibility for next login
    const allNavBtns = ['homeBtn', 'resourcesBtn', 'quizzesBtn', 'aiTutorBtn',
                        'papersBtn', 'toolsBtn', 'careerBtn', 'doubtsBtn', 'progressBtn'];
    allNavBtns.forEach(id => {
        const btn = document.getElementById(id);
        if (btn) btn.style.display = '';
    });

    // Hide parent and teacher dashboard buttons
    const parentDashBtn = document.getElementById('parentDashBtn');
    if (parentDashBtn) parentDashBtn.style.display = 'none';
    const teacherDashBtn = document.getElementById('teacherDashBtn');
    if (teacherDashBtn) teacherDashBtn.style.display = 'none';

    // Reset active panel
    document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
    const homePanel = document.getElementById('homePanel');
    if (homePanel) homePanel.classList.add('active');

    // Reset active nav button
    document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
    const homeBtn = document.getElementById('homeBtn');
    if (homeBtn) homeBtn.classList.add('active');

    // Return to auth screen
    document.getElementById('dashboardScreen')?.classList.remove('active');
    document.getElementById('authScreen')?.classList.add('active');

    // Reset forms
    document.getElementById('loginForm')?.reset();
    document.getElementById('registerForm')?.reset();

    // Reset auth tabs to Login
    document.querySelectorAll('.tab-btn').forEach((btn, idx) => {
        btn.classList.toggle('active', idx === 0);
    });
    document.querySelectorAll('.auth-tab').forEach((tab, idx) => {
        tab.classList.toggle('active', idx === 0);
    });

    console.log('Logout complete');
}

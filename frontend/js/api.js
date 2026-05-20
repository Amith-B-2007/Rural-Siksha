/**
 * API wrapper for all backend calls
 * Handles offline caching and sync queue
 */

const API = {
    baseURL: '/api',
    timeout: 10000,

    /**
     * Generic fetch wrapper
     */
    async request(method, endpoint, data = null, options = {}) {
        const url = `${this.baseURL}${endpoint}`;
        const headers = {
            'Content-Type': 'application/json',
            ...options.headers
        };

        const config = {
            method,
            headers,
            credentials: 'include', // Include cookies
        };

        if (data && (method === 'POST' || method === 'PUT')) {
            config.body = JSON.stringify(data);
        }

        try {
            const response = await Promise.race([
                fetch(url, config),
                new Promise((_, reject) =>
                    setTimeout(() => reject(new Error('Request timeout')), this.timeout)
                )
            ]);

            const result = await response.json().catch(() => ({}));

            if (!response.ok) {
                throw {
                    status: response.status,
                    message: result.error || 'Request failed'
                };
            }

            return result;
        } catch (error) {
            console.error(`API Error: ${method} ${endpoint}`, error);

            // For offline scenarios, try to use cached data
            if (!navigator.onLine && method === 'GET') {
                const cached = await offlineDB.getCached(endpoint);
                if (cached) {
                    return cached;
                }
            }

            // Queue failed POST/PUT requests for later sync
            if (!navigator.onLine && (method === 'POST' || method === 'PUT')) {
                await offlineDB.addToSyncQueue({
                    method,
                    endpoint,
                    data,
                    timestamp: Date.now()
                });
                return { queued: true };
            }

            throw error;
        }
    },

    // Auth endpoints
    auth: {
        register: (email, password, fullName, role, extraData = {}) =>
            API.request('POST', '/auth/register', {
                email, password, full_name: fullName, role, ...extraData
            }),
        login: (email, password) =>
            API.request('POST', '/auth/login', { email, password }),
        logout: () =>
            API.request('POST', '/auth/logout'),
        me: () =>
            API.request('GET', '/auth/me')
    },

    // Resource endpoints
    resources: {
        list: (grade = null, subject = null) => {
            let endpoint = '/resources';
            const params = new URLSearchParams();
            if (grade) params.append('grade', grade);
            if (subject) params.append('subject', subject);
            if (params.toString()) endpoint += '?' + params;
            return API.request('GET', endpoint);
        },
        get: (id) =>
            API.request('GET', `/resources/${id}`),
        download: (id) =>
            `${API.baseURL}/resources/${id}/download`,
        upload: async (formData) => {
            const url = `${API.baseURL}/resources/upload`;
            try {
                const response = await fetch(url, {
                    method: 'POST',
                    body: formData,
                    credentials: 'include'
                });
                return await response.json();
            } catch (error) {
                console.error('Upload failed:', error);
                throw error;
            }
        }
    },

    // Quiz endpoints
    quizzes: {
        list: (grade = null, subject = null) => {
            let endpoint = '/quizzes';
            const params = new URLSearchParams();
            if (grade) params.append('grade', grade);
            if (subject) params.append('subject', subject);
            if (params.toString()) endpoint += '?' + params;
            return API.request('GET', endpoint);
        },
        get: (id) =>
            API.request('GET', `/quizzes/${id}`),
        startAttempt: (id) =>
            API.request('POST', `/quizzes/${id}/start`),
        submit: (id, attemptId, answers) =>
            API.request('POST', `/quizzes/${id}/submit`, {
                attempt_id: attemptId,
                answers
            }),
        results: (id, attemptId) =>
            API.request('GET', `/quizzes/${id}/results/${attemptId}`),
        create: (data) =>
            API.request('POST', '/quizzes/create', data),
        myAttempts: () =>
            API.request('GET', '/quizzes/my-attempts')
    },

    // Doubt endpoints
    doubts: {
        create: (questionText, questionDetail, subject, gradeLevel) =>
            API.request('POST', '/doubts', {
                question_text: questionText,
                question_detail: questionDetail,
                subject,
                grade_level: gradeLevel
            }),
        list: (status = null) => {
            let endpoint = '/doubts';
            if (status) endpoint += `?status=${status}`;
            return API.request('GET', endpoint);
        },
        get: (id) =>
            API.request('GET', `/doubts/${id}`),
        respond: (id, responseText) =>
            API.request('POST', `/doubts/${id}/respond`, {
                response_text: responseText
            }),
        markHelpful: (id, responseId, isHelpful) =>
            API.request('POST', `/doubts/${id}/helpful`, {
                response_id: responseId,
                is_helpful: isHelpful
            }),
        aiStatus: () =>
            API.request('GET', '/doubts/ai-status')
    },

    // Progress endpoints
    progress: {
        summary: () =>
            API.request('GET', '/progress'),
        bySubject: (subject) =>
            API.request('GET', `/progress/subject/${subject}`),
        classProgress: (gradeLevel) =>
            API.request('GET', `/progress/class/${gradeLevel}`)
    },

    // Settings endpoints
    settings: {
        getOnlineStatus: () => navigator.onLine
    },

    // Health endpoints
    health: {
        check: () =>
            API.request('GET', '/health')
    }
};

// Handle offline/online status
window.addEventListener('online', () => {
    console.log('Back online, syncing pending changes...');
    offlineDB.syncPending();
});

window.addEventListener('offline', () => {
    console.log('Offline mode activated');
});

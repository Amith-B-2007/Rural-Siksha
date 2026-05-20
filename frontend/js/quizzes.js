/**
 * Quiz panel handlers - taking quizzes, viewing results, creating quizzes
 */

let currentQuizzes = [];
let currentQuiz = null;
let currentAttempt = null;
let quizAnswers = {};
let questionCounter = 0;

/**
 * Load and display quizzes
 */
async function loadQuizzes() {
    const user = Utils.getCurrentUser();
    if (!user) return;

    try {
        const subject = document.getElementById('quizSubjectFilter')?.value || null;
        // Use grade selector for students
        const grade = typeof getCurrentViewingGrade === 'function' ? getCurrentViewingGrade() : (user.role === 'student' ? user.gradeLevel : null);

        const quizzes = await API.quizzes.list(grade, subject);

        if (quizzes.length) {
            await offlineDB.cache('/quizzes', quizzes);
        }

        currentQuizzes = quizzes;
        displayQuizzes(quizzes);
    } catch (error) {
        console.error('Failed to load quizzes:', error);
        const cached = await offlineDB.getCached('/quizzes');
        if (cached) displayQuizzes(cached);
    }
}

/**
 * Display quizzes
 */
function displayQuizzes(quizzes) {
    const container = document.getElementById('quizList');

    if (!quizzes || quizzes.length === 0) {
        container.innerHTML = '<p>No quizzes available. ' +
            (Utils.isTeacher() ? 'Click "Create Quiz" to add one!' : 'Check back later!') + '</p>';
        return;
    }

    container.innerHTML = quizzes.map(quiz => `
        <div class="resource-card">
            <h3>${quiz.title}</h3>
            <p>${quiz.description || 'No description'}</p>
            <div class="resource-meta">
                <span>${quiz.subject}</span>
                <span>Grade ${quiz.grade_level}</span>
                <span>${quiz.total_questions} questions</span>
            </div>
            ${quiz.time_limit_minutes ? `<p><strong>Time Limit:</strong> ${quiz.time_limit_minutes} min</p>` : ''}
            <div class="resource-actions">
                ${Utils.isStudent()
                    ? `<button onclick="startQuiz(${quiz.id})">Start Quiz</button>`
                    : `<button onclick="viewQuizDetails(${quiz.id})">View Details</button>`
                }
            </div>
        </div>
    `).join('');
}

/**
 * Start taking a quiz
 */
async function startQuiz(quizId) {
    try {
        // Get quiz details
        currentQuiz = await API.quizzes.get(quizId);

        // Start attempt
        const attempt = await API.quizzes.startAttempt(quizId);
        currentAttempt = attempt;
        quizAnswers = {};

        // Show quiz taking view
        document.getElementById('quizListView').classList.add('hidden');
        document.getElementById('quizTakingView').classList.remove('hidden');
        document.getElementById('quizCreateView').classList.add('hidden');
        document.getElementById('quizResultsView').classList.add('hidden');

        document.getElementById('quizTitle').textContent = currentQuiz.title;
        document.getElementById('quizProgress').textContent =
            `0/${currentQuiz.questions.length} answered`;

        renderQuestions(currentQuiz.questions);
    } catch (error) {
        console.error('Failed to start quiz:', error);
        Utils.showSuccess('Failed to start quiz: ' + (error.message || 'Unknown error'));
    }
}

/**
 * Render quiz questions
 */
function renderQuestions(questions) {
    const container = document.getElementById('quizQuestions');
    container.innerHTML = questions.map((q, idx) => `
        <div class="quiz-question" data-question-id="${q.id}">
            <h4>Q${idx + 1}. ${q.question_text}</h4>
            ${q.question_type === 'mcq' ? `
                <div class="quiz-options">
                    ${q.option_a ? `
                        <label class="quiz-option">
                            <input type="radio" name="q${q.id}" value="A" onchange="updateAnswer(${q.id}, 'A')">
                            <span><strong>A.</strong> ${q.option_a}</span>
                        </label>
                    ` : ''}
                    ${q.option_b ? `
                        <label class="quiz-option">
                            <input type="radio" name="q${q.id}" value="B" onchange="updateAnswer(${q.id}, 'B')">
                            <span><strong>B.</strong> ${q.option_b}</span>
                        </label>
                    ` : ''}
                    ${q.option_c ? `
                        <label class="quiz-option">
                            <input type="radio" name="q${q.id}" value="C" onchange="updateAnswer(${q.id}, 'C')">
                            <span><strong>C.</strong> ${q.option_c}</span>
                        </label>
                    ` : ''}
                    ${q.option_d ? `
                        <label class="quiz-option">
                            <input type="radio" name="q${q.id}" value="D" onchange="updateAnswer(${q.id}, 'D')">
                            <span><strong>D.</strong> ${q.option_d}</span>
                        </label>
                    ` : ''}
                </div>
            ` : q.question_type === 'short_answer' ? `
                <input type="text" placeholder="Your answer..."
                    onchange="updateAnswer(${q.id}, this.value)"
                    class="quiz-text-input">
            ` : `
                <textarea rows="4" placeholder="Write your answer..."
                    onchange="updateAnswer(${q.id}, this.value)"
                    class="quiz-text-input"></textarea>
            `}
        </div>
    `).join('');
}

/**
 * Update answer for a question
 */
function updateAnswer(questionId, value) {
    quizAnswers[questionId] = value;
    const answered = Object.keys(quizAnswers).length;
    const total = currentQuiz.questions.length;
    document.getElementById('quizProgress').textContent = `${answered}/${total} answered`;
}

/**
 * Submit quiz
 */
async function submitQuiz() {
    if (!currentQuiz || !currentAttempt) return;

    const answersList = Object.entries(quizAnswers).map(([qid, ans]) => ({
        question_id: parseInt(qid),
        answer: ans
    }));

    if (answersList.length === 0) {
        if (!confirm('You have not answered any questions. Submit anyway?')) {
            return;
        }
    }

    try {
        const result = await API.quizzes.submit(currentQuiz.id, currentAttempt.attempt_id, answersList);
        displayQuizResults(result);
    } catch (error) {
        console.error('Failed to submit quiz:', error);
        // Try to save offline
        if (!navigator.onLine) {
            await offlineDB.saveQuizAnswers(currentQuiz.id, {
                attempt_id: currentAttempt.attempt_id,
                answers: answersList
            });
            Utils.showSuccess('Quiz saved offline. Will be submitted when online.');
        } else {
            Utils.showSuccess('Failed to submit: ' + (error.message || 'Unknown error'));
        }
    }
}

/**
 * Display quiz results
 */
async function displayQuizResults(result) {
    document.getElementById('quizTakingView').classList.add('hidden');
    document.getElementById('quizResultsView').classList.remove('hidden');

    // Get detailed results
    let details = null;
    try {
        details = await API.quizzes.results(currentQuiz.id, result.attempt_id);
    } catch (e) {
        console.error('Failed to load detailed results:', e);
    }

    const container = document.getElementById('quizResults');
    const passClass = result.passed ? 'pass' : 'fail';

    let html = `
        <div class="quiz-result-summary ${passClass}">
            <h2>${result.passed ? 'Well Done!' : 'Keep Practicing!'}</h2>
            <div class="score-display">
                <span class="score-percentage">${result.percentage.toFixed(1)}%</span>
                <span class="score-fraction">${result.score} / ${result.total_marks}</span>
            </div>
            <p>${result.passed ? 'You passed!' : 'You can do better next time.'}</p>
            ${result.needs_review ? '<p>Some answers need teacher review.</p>' : ''}
        </div>
    `;

    if (details && details.answers) {
        html += '<h3>Detailed Results</h3>';
        details.answers.forEach((ans, idx) => {
            const correctClass = ans.is_correct === true ? 'correct' :
                                 ans.is_correct === false ? 'incorrect' : 'pending';
            html += `
                <div class="answer-review ${correctClass}">
                    <h4>Q${idx + 1}. ${ans.question_text}</h4>
                    <p><strong>Your answer:</strong> ${ans.student_answer || '(no answer)'}</p>
                    ${ans.question_type === 'mcq' && ans.correct_answer ?
                        `<p><strong>Correct answer:</strong> ${ans.correct_answer}</p>` : ''}
                    <p><strong>Marks:</strong> ${ans.marks_awarded} / ${ans.max_marks}</p>
                    ${ans.explanation ? `<p class="explanation"><strong>Explanation:</strong> ${ans.explanation}</p>` : ''}
                </div>
            `;
        });
    }

    container.innerHTML = html;
}

/**
 * Back to quiz list
 */
function backToQuizList() {
    document.getElementById('quizListView').classList.remove('hidden');
    document.getElementById('quizTakingView').classList.add('hidden');
    document.getElementById('quizResultsView').classList.add('hidden');
    document.getElementById('quizCreateView').classList.add('hidden');
    currentQuiz = null;
    currentAttempt = null;
    quizAnswers = {};
    loadQuizzes();
}

/**
 * Show quiz creation form (teacher only)
 */
function showCreateQuizForm() {
    document.getElementById('quizListView').classList.add('hidden');
    document.getElementById('quizCreateView').classList.remove('hidden');
    questionCounter = 0;
    document.getElementById('questionsContainer').innerHTML = '';
    addQuestion();
}

/**
 * Add a question to the create quiz form
 */
function addQuestion() {
    questionCounter++;
    const container = document.getElementById('questionsContainer');
    const qDiv = document.createElement('div');
    qDiv.className = 'create-question';
    qDiv.dataset.qid = questionCounter;
    qDiv.innerHTML = `
        <h4>Question ${questionCounter}</h4>
        <textarea placeholder="Question text" class="q-text" rows="2" required></textarea>
        <select class="q-type" onchange="toggleOptions(this)">
            <option value="mcq">Multiple Choice</option>
            <option value="short_answer">Short Answer</option>
            <option value="essay">Essay</option>
        </select>
        <div class="mcq-options">
            <input type="text" placeholder="Option A" class="q-opt-a">
            <input type="text" placeholder="Option B" class="q-opt-b">
            <input type="text" placeholder="Option C" class="q-opt-c">
            <input type="text" placeholder="Option D" class="q-opt-d">
            <select class="q-correct">
                <option value="">Correct Option</option>
                <option value="A">A</option>
                <option value="B">B</option>
                <option value="C">C</option>
                <option value="D">D</option>
            </select>
        </div>
        <input type="text" placeholder="Expected answer (for short answer)" class="q-expected hidden">
        <textarea placeholder="Explanation (optional)" class="q-explanation" rows="2"></textarea>
        <button type="button" onclick="removeQuestion(${questionCounter})" class="btn btn-danger btn-small">Remove</button>
        <hr>
    `;
    container.appendChild(qDiv);
}

/**
 * Toggle options visibility based on question type
 */
function toggleOptions(select) {
    const parent = select.closest('.create-question');
    const mcqOpts = parent.querySelector('.mcq-options');
    const expected = parent.querySelector('.q-expected');

    if (select.value === 'mcq') {
        mcqOpts.classList.remove('hidden');
        expected.classList.add('hidden');
    } else if (select.value === 'short_answer') {
        mcqOpts.classList.add('hidden');
        expected.classList.remove('hidden');
    } else {
        mcqOpts.classList.add('hidden');
        expected.classList.add('hidden');
    }
}

/**
 * Remove a question
 */
function removeQuestion(qid) {
    const el = document.querySelector(`[data-qid="${qid}"]`);
    if (el) el.remove();
}

/**
 * Create the quiz
 */
async function createQuiz(e) {
    e.preventDefault();

    const title = document.getElementById('quizTitleInput').value.trim();
    const description = document.getElementById('quizDescriptionInput').value.trim();
    const subject = document.getElementById('quizSubjectInput').value;
    const grade = parseInt(document.getElementById('quizGradeInput').value);
    const timeLimit = document.getElementById('quizTimeLimitInput').value;

    // Collect questions
    const questionEls = document.querySelectorAll('.create-question');
    const questions = [];

    for (const qEl of questionEls) {
        const qText = qEl.querySelector('.q-text').value.trim();
        const qType = qEl.querySelector('.q-type').value;

        if (!qText) continue;

        const q = {
            question_text: qText,
            question_type: qType,
            explanation: qEl.querySelector('.q-explanation').value.trim()
        };

        if (qType === 'mcq') {
            q.option_a = qEl.querySelector('.q-opt-a').value.trim();
            q.option_b = qEl.querySelector('.q-opt-b').value.trim();
            q.option_c = qEl.querySelector('.q-opt-c').value.trim();
            q.option_d = qEl.querySelector('.q-opt-d').value.trim();
            q.correct_option = qEl.querySelector('.q-correct').value;

            if (!q.correct_option) {
                Utils.showSuccess('Please select correct option for all MCQ questions');
                return;
            }
        } else if (qType === 'short_answer') {
            q.expected_answer = qEl.querySelector('.q-expected').value.trim();
        }

        questions.push(q);
    }

    if (questions.length === 0) {
        Utils.showSuccess('Please add at least one question');
        return;
    }

    try {
        const result = await API.quizzes.create({
            title, description, subject,
            grade_level: grade,
            time_limit_minutes: timeLimit ? parseInt(timeLimit) : null,
            questions
        });

        Utils.showSuccess('Quiz created successfully!');
        document.getElementById('createQuizForm').reset();
        backToQuizList();
    } catch (error) {
        console.error('Failed to create quiz:', error);
        Utils.showSuccess('Failed to create quiz: ' + (error.message || 'Unknown error'));
    }
}

/**
 * Setup event listeners
 */
document.addEventListener('DOMContentLoaded', () => {
    const quizzesBtn = document.getElementById('quizzesBtn');
    if (quizzesBtn) {
        quizzesBtn.addEventListener('click', () => {
            switchPanel('quizzesPanel', quizzesBtn);
            backToQuizList();

            // Show create button for teachers
            if (Utils.isTeacher()) {
                document.getElementById('createQuizBtn').classList.remove('hidden');
            }
        });
    }

    document.getElementById('quizSubjectFilter')?.addEventListener('change', loadQuizzes);
    document.getElementById('refreshQuizzes')?.addEventListener('click', loadQuizzes);
    document.getElementById('createQuizBtn')?.addEventListener('click', showCreateQuizForm);
    document.getElementById('submitQuizBtn')?.addEventListener('click', submitQuiz);
    document.getElementById('cancelQuizBtn')?.addEventListener('click', backToQuizList);
    document.getElementById('backToQuizzesBtn')?.addEventListener('click', backToQuizList);
    document.getElementById('cancelCreateQuizBtn')?.addEventListener('click', backToQuizList);
    document.getElementById('addQuestionBtn')?.addEventListener('click', addQuestion);
    document.getElementById('createQuizForm')?.addEventListener('submit', createQuiz);
});

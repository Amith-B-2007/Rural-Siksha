/**
 * Quick Practice Mode and Educational Games
 */

let practiceQuestion = null;
let practiceStreak = 0;

/**
 * Quick Practice Mode
 */
async function startQuickPractice() {
    const user = Utils.getCurrentUser();
    if (!user) return;

    try {
        const grade = typeof getCurrentViewingGrade === 'function' ? getCurrentViewingGrade() : user.gradeLevel;
        const quizzes = await API.quizzes.list(grade);

        if (!quizzes || quizzes.length === 0) {
            Utils.showSuccess('No quizzes available for practice');
            return;
        }

        // Pick a random quiz
        const randomQuiz = quizzes[Math.floor(Math.random() * quizzes.length)];
        const quiz = await API.quizzes.get(randomQuiz.id);

        if (!quiz.questions || quiz.questions.length === 0) {
            Utils.showSuccess('No questions in this quiz');
            return;
        }

        // Pick a random question
        const randomQ = quiz.questions[Math.floor(Math.random() * quiz.questions.length)];
        practiceQuestion = randomQ;

        showPracticeQuestion(quiz.subject, randomQ);
    } catch (error) {
        console.error('Practice error:', error);
        Utils.showSuccess('Could not load practice question');
    }
}

function showPracticeQuestion(subject, q) {
    const html = `
        <div class="practice-mode">
            <h2>🎲 Quick Practice</h2>
            <div class="practice-meta">
                <span>📚 ${subject}</span>
                <span>🔥 Streak: ${practiceStreak}</span>
            </div>

            <div class="practice-question">
                <h3>${q.question_text}</h3>

                ${q.question_type === 'mcq' ? `
                    <div class="practice-options">
                        ${q.option_a ? `<button onclick="checkPracticeAnswer('A')" class="practice-option" data-option="A">A. ${q.option_a}</button>` : ''}
                        ${q.option_b ? `<button onclick="checkPracticeAnswer('B')" class="practice-option" data-option="B">B. ${q.option_b}</button>` : ''}
                        ${q.option_c ? `<button onclick="checkPracticeAnswer('C')" class="practice-option" data-option="C">C. ${q.option_c}</button>` : ''}
                        ${q.option_d ? `<button onclick="checkPracticeAnswer('D')" class="practice-option" data-option="D">D. ${q.option_d}</button>` : ''}
                    </div>
                ` : `
                    <div class="practice-text-input">
                        <input type="text" id="practiceAnswer" placeholder="Type your answer">
                        <button onclick="checkPracticeAnswer(document.getElementById('practiceAnswer').value)" class="btn btn-primary">Check</button>
                    </div>
                `}
            </div>

            <div id="practiceResult" style="display:none"></div>

            <div class="practice-actions" id="practiceActions" style="display:none">
                <button onclick="startQuickPractice()" class="btn btn-primary">➡️ Next Question</button>
                <button onclick="closeModal()" class="btn btn-secondary">Stop</button>
            </div>
        </div>
    `;
    openModal(html);
}

function checkPracticeAnswer(answer) {
    if (!practiceQuestion) return;

    const isCorrect = practiceQuestion.question_type === 'mcq' ?
        answer.toUpperCase() === practiceQuestion.correct_option :
        answer.trim().toLowerCase() === (practiceQuestion.expected_answer || '').trim().toLowerCase();

    const resultDiv = document.getElementById('practiceResult');
    const actionsDiv = document.getElementById('practiceActions');

    if (isCorrect) {
        practiceStreak++;
        resultDiv.innerHTML = `
            <div class="practice-result correct">
                <div class="result-icon">✅</div>
                <h3>Correct!</h3>
                <p>Great job! Streak: ${practiceStreak}</p>
                ${practiceQuestion.explanation ? `<p><em>${practiceQuestion.explanation}</em></p>` : ''}
            </div>
        `;
        // Award XP
        if (typeof awardXP === 'function') awardXP('quiz_passed', 10);
    } else {
        practiceStreak = 0;
        const correct = practiceQuestion.question_type === 'mcq' ?
            practiceQuestion.correct_option :
            practiceQuestion.expected_answer;
        resultDiv.innerHTML = `
            <div class="practice-result incorrect">
                <div class="result-icon">❌</div>
                <h3>Not Quite!</h3>
                <p>The correct answer was: <strong>${correct}</strong></p>
                ${practiceQuestion.explanation ? `<p><em>${practiceQuestion.explanation}</em></p>` : ''}
            </div>
        `;
    }

    // Disable options
    document.querySelectorAll('.practice-option').forEach(b => {
        b.disabled = true;
        if (b.dataset.option === practiceQuestion.correct_option) {
            b.classList.add('correct-option');
        }
    });

    resultDiv.style.display = 'block';
    actionsDiv.style.display = 'flex';
}

/**
 * ============================================
 * EDUCATIONAL GAMES
 * ============================================
 */

function showGamesMenu() {
    const html = `
        <div class="games-menu">
            <h2>🎮 Educational Games</h2>
            <p class="section-info">Learn while having fun!</p>

            <div class="games-grid">
                <div class="game-card" onclick="startMathGame()">
                    <div class="game-icon">🧮</div>
                    <h3>Math Sprint</h3>
                    <p>Solve 10 problems in 60 seconds</p>
                </div>

                <div class="game-card" onclick="startMemoryGame()">
                    <div class="game-icon">🧠</div>
                    <h3>Memory Match</h3>
                    <p>Match pairs of cards</p>
                </div>

                <div class="game-card" onclick="startSpellingGame()">
                    <div class="game-icon">🔤</div>
                    <h3>Spelling Bee</h3>
                    <p>Spell words correctly</p>
                </div>

                <div class="game-card" onclick="startQuizGame()">
                    <div class="game-icon">🎲</div>
                    <h3>Quick Practice</h3>
                    <p>Random questions</p>
                </div>
            </div>

            <button onclick="closeModal()" class="btn btn-secondary" style="margin-top:20px">Close</button>
        </div>
    `;
    openModal(html);
}

/**
 * Math Sprint Game
 */
let mathScore = 0;
let mathQuestionsAnswered = 0;
let mathTimer = null;
let mathTimeLeft = 60;
let currentMathProblem = null;

function startMathGame() {
    mathScore = 0;
    mathQuestionsAnswered = 0;
    mathTimeLeft = 60;

    const html = `
        <div class="math-game">
            <h2>🧮 Math Sprint!</h2>
            <div class="math-game-stats">
                <span>⏱️ Time: <strong id="mathTime">60s</strong></span>
                <span>📊 Score: <strong id="mathScore">0</strong></span>
                <span>📝 Q#: <strong id="mathQNum">0</strong></span>
            </div>

            <div id="mathProblem" class="math-problem">
                Click START to begin!
            </div>

            <input type="number" id="mathInput" placeholder="Your answer" style="display:none; padding:15px; font-size:24px; text-align:center; width:200px; margin:20px auto; display:block" onkeyup="if(event.key==='Enter') checkMathAnswer()">

            <div id="mathFeedback" class="math-feedback"></div>

            <div class="math-buttons">
                <button id="mathStartBtn" onclick="beginMathGame()" class="btn btn-primary btn-large">▶️ Start Game</button>
                <button onclick="closeModal()" class="btn btn-secondary">Close</button>
            </div>
        </div>
    `;
    openModal(html);
}

function beginMathGame() {
    document.getElementById('mathStartBtn').style.display = 'none';
    document.getElementById('mathInput').style.display = 'block';

    nextMathProblem();

    mathTimer = setInterval(() => {
        mathTimeLeft--;
        document.getElementById('mathTime').textContent = mathTimeLeft + 's';
        if (mathTimeLeft <= 0) {
            endMathGame();
        }
    }, 1000);
}

function nextMathProblem() {
    const operations = ['+', '-', '×'];
    const op = operations[Math.floor(Math.random() * operations.length)];
    let a, b, answer;

    if (op === '+') {
        a = Math.floor(Math.random() * 50) + 1;
        b = Math.floor(Math.random() * 50) + 1;
        answer = a + b;
    } else if (op === '-') {
        a = Math.floor(Math.random() * 50) + 20;
        b = Math.floor(Math.random() * 20) + 1;
        answer = a - b;
    } else {
        a = Math.floor(Math.random() * 12) + 1;
        b = Math.floor(Math.random() * 12) + 1;
        answer = a * b;
    }

    currentMathProblem = {a, b, op, answer};
    document.getElementById('mathProblem').innerHTML = `${a} ${op} ${b} = ?`;
    document.getElementById('mathInput').value = '';
    document.getElementById('mathInput').focus();
}

function checkMathAnswer() {
    const userAnswer = parseInt(document.getElementById('mathInput').value);
    const feedback = document.getElementById('mathFeedback');

    mathQuestionsAnswered++;
    document.getElementById('mathQNum').textContent = mathQuestionsAnswered;

    if (userAnswer === currentMathProblem.answer) {
        mathScore++;
        document.getElementById('mathScore').textContent = mathScore;
        feedback.innerHTML = '<span style="color:var(--success); font-size:18px;">✅ Correct!</span>';
    } else {
        feedback.innerHTML = `<span style="color:var(--danger); font-size:18px;">❌ Wrong! Answer was ${currentMathProblem.answer}</span>`;
    }

    setTimeout(() => {
        feedback.innerHTML = '';
        nextMathProblem();
    }, 800);
}

function endMathGame() {
    clearInterval(mathTimer);
    const html = `
        <div class="math-game">
            <h2>🏁 Game Over!</h2>
            <div class="game-result">
                <div class="result-icon">${mathScore >= 10 ? '🏆' : mathScore >= 5 ? '🎯' : '💪'}</div>
                <h3>Final Score: ${mathScore} / ${mathQuestionsAnswered}</h3>
                <p>Accuracy: ${mathQuestionsAnswered > 0 ? Math.round(mathScore / mathQuestionsAnswered * 100) : 0}%</p>
                ${mathScore >= 10 ? '<p>🎉 Excellent! You are a math champion!</p>' :
                  mathScore >= 5 ? '<p>👍 Great job! Keep practicing!</p>' :
                  '<p>💪 Good try! Practice makes perfect.</p>'}
            </div>

            <div class="math-buttons">
                <button onclick="startMathGame()" class="btn btn-primary">🔄 Play Again</button>
                <button onclick="closeModal()" class="btn btn-secondary">Close</button>
            </div>
        </div>
    `;
    document.getElementById('modalBody').innerHTML = html;

    // Award XP
    if (typeof awardXP === 'function') {
        awardXP('quiz_completed', mathScore * 5);
    }
}

/**
 * Memory Match Game
 */
let memoryCards = [];
let flippedCards = [];
let matchedPairs = 0;

function startMemoryGame() {
    const emojis = ['🍎', '🌟', '🎓', '📚', '🎯', '🏆', '🎮', '🎨'];
    memoryCards = [...emojis, ...emojis].sort(() => Math.random() - 0.5);
    flippedCards = [];
    matchedPairs = 0;

    const html = `
        <div class="memory-game">
            <h2>🧠 Memory Match</h2>
            <p class="section-info">Find all 8 matching pairs!</p>
            <div class="memory-stats">
                <span>🎯 Matched: <strong id="matchedCount">0</strong> / 8</span>
            </div>

            <div class="memory-grid">
                ${memoryCards.map((emoji, idx) => `
                    <div class="memory-card" data-index="${idx}" data-emoji="${emoji}" onclick="flipCard(${idx})">
                        <div class="card-front">?</div>
                        <div class="card-back">${emoji}</div>
                    </div>
                `).join('')}
            </div>

            <button onclick="closeModal()" class="btn btn-secondary" style="margin-top:15px">Close</button>
        </div>
    `;
    openModal(html);
}

function flipCard(idx) {
    if (flippedCards.length >= 2) return;

    const card = document.querySelector(`.memory-card[data-index="${idx}"]`);
    if (card.classList.contains('flipped') || card.classList.contains('matched')) return;

    card.classList.add('flipped');
    flippedCards.push({idx, emoji: memoryCards[idx], card});

    if (flippedCards.length === 2) {
        setTimeout(checkMatch, 800);
    }
}

function checkMatch() {
    const [a, b] = flippedCards;
    if (a.emoji === b.emoji) {
        a.card.classList.add('matched');
        b.card.classList.add('matched');
        matchedPairs++;
        document.getElementById('matchedCount').textContent = matchedPairs;

        if (matchedPairs === 8) {
            setTimeout(() => {
                Utils.showSuccess('🎉 You won! All matches found!');
                if (typeof awardXP === 'function') awardXP('quiz_completed', 30);
            }, 500);
        }
    } else {
        a.card.classList.remove('flipped');
        b.card.classList.remove('flipped');
    }
    flippedCards = [];
}

/**
 * Spelling Bee Game
 */
const SPELLING_WORDS = [
    {word: 'BEAUTIFUL', hint: 'Pleasing to look at'},
    {word: 'ELEPHANT', hint: 'Largest land animal'},
    {word: 'KNOWLEDGE', hint: 'Information and understanding'},
    {word: 'NECESSARY', hint: 'Something needed'},
    {word: 'EDUCATION', hint: 'Process of learning'},
    {word: 'INDIA', hint: 'A South Asian country'},
    {word: 'COMPUTER', hint: 'Electronic device'},
    {word: 'STUDENT', hint: 'One who studies'},
    {word: 'TEACHER', hint: 'One who teaches'},
    {word: 'INTELLIGENCE', hint: 'Ability to think'},
];

let spellingIndex = 0;
let spellingScore = 0;

function startSpellingGame() {
    spellingIndex = 0;
    spellingScore = 0;
    showSpellingWord();
}

function showSpellingWord() {
    if (spellingIndex >= SPELLING_WORDS.length) {
        endSpellingGame();
        return;
    }

    const word = SPELLING_WORDS[spellingIndex];

    const html = `
        <div class="spelling-game">
            <h2>🔤 Spelling Bee</h2>
            <div class="spelling-stats">
                <span>📝 Word ${spellingIndex + 1} / ${SPELLING_WORDS.length}</span>
                <span>📊 Score: ${spellingScore}</span>
            </div>

            <div class="spelling-content">
                <p class="spelling-hint">💡 Hint: <strong>${word.hint}</strong></p>
                <button onclick="speakWord('${word.word}')" class="btn btn-primary">🔊 Listen to Word</button>

                <div class="form-group" style="margin-top:20px">
                    <label>Type the word you heard:</label>
                    <input type="text" id="spellingInput" placeholder="Type here..." style="font-size:20px; text-align:center" onkeyup="if(event.key==='Enter') checkSpelling()">
                </div>

                <button onclick="checkSpelling()" class="btn btn-primary btn-large">✓ Check Spelling</button>
                <button onclick="closeModal()" class="btn btn-secondary">Stop</button>
            </div>
        </div>
    `;
    openModal(html);
}

function speakWord(word) {
    if ('speechSynthesis' in window) {
        const utterance = new SpeechSynthesisUtterance(word);
        utterance.rate = 0.8;
        utterance.lang = 'en-IN';
        window.speechSynthesis.speak(utterance);
    } else {
        Utils.showSuccess('Speech not supported. Hint: ' + word);
    }
}

function checkSpelling() {
    const input = document.getElementById('spellingInput').value.trim().toUpperCase();
    const correct = SPELLING_WORDS[spellingIndex].word;

    if (input === correct) {
        spellingScore++;
        Utils.showSuccess('✅ Correct!');
    } else {
        Utils.showSuccess(`❌ Wrong. Correct: ${correct}`);
    }

    spellingIndex++;
    setTimeout(showSpellingWord, 1500);
}

function endSpellingGame() {
    const html = `
        <div class="spelling-game">
            <h2>🏁 Spelling Bee Complete!</h2>
            <div class="game-result">
                <div class="result-icon">${spellingScore >= 8 ? '🏆' : spellingScore >= 5 ? '🌟' : '💪'}</div>
                <h3>Score: ${spellingScore} / ${SPELLING_WORDS.length}</h3>
                ${spellingScore >= 8 ? '<p>🎉 Excellent spelling skills!</p>' :
                  spellingScore >= 5 ? '<p>👍 Good job!</p>' :
                  '<p>💪 Keep practicing!</p>'}
            </div>
            <button onclick="startSpellingGame()" class="btn btn-primary">🔄 Play Again</button>
            <button onclick="closeModal()" class="btn btn-secondary">Close</button>
        </div>
    `;
    document.getElementById('modalBody').innerHTML = html;

    if (typeof awardXP === 'function') awardXP('quiz_completed', spellingScore * 5);
}

function startQuizGame() {
    closeModal();
    startQuickPractice();
}

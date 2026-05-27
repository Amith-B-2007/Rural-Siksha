/**
 * Voice Chat with AI + Photo Math Scanner
 */

let recognition = null;
let isRecording = false;

/**
 * Check browser support for Speech Recognition
 */
function isVoiceSupported() {
    return 'webkitSpeechRecognition' in window || 'SpeechRecognition' in window;
}

/**
 * Initialize speech recognition
 */
function initVoiceRecognition() {
    if (!isVoiceSupported()) return null;

    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    recognition = new SpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    return recognition;
}

/**
 * Start voice input
 */
function startVoiceInput(language = 'en-IN') {
    if (!isVoiceSupported()) {
        Utils.showSuccess('Voice input not supported in your browser. Use Chrome or Edge.');
        return;
    }

    if (!recognition) {
        recognition = initVoiceRecognition();
    }

    recognition.lang = language;

    const btn = document.getElementById('voiceBtn');
    const indicator = document.getElementById('voiceIndicator');

    recognition.onstart = () => {
        isRecording = true;
        if (btn) {
            btn.innerHTML = '🔴 Listening...';
            btn.classList.add('recording');
        }
        if (indicator) indicator.style.display = 'block';
    };

    recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        console.log('Voice input:', transcript);

        // Put transcript in the AI input field
        const input = document.getElementById('aiQuestion');
        if (input) {
            input.value = transcript;
            // Auto-submit
            document.getElementById('aiTutorForm').dispatchEvent(new Event('submit'));
        }
    };

    recognition.onerror = (event) => {
        console.error('Speech error:', event.error);
        Utils.showSuccess('Voice input error: ' + event.error);
        stopVoiceInput();
    };

    recognition.onend = () => {
        stopVoiceInput();
    };

    try {
        recognition.start();
    } catch (e) {
        console.error('Recognition start failed:', e);
        stopVoiceInput();
    }
}

/**
 * Stop voice input
 */
function stopVoiceInput() {
    isRecording = false;
    const btn = document.getElementById('voiceBtn');
    const indicator = document.getElementById('voiceIndicator');

    if (btn) {
        btn.innerHTML = '🎤';
        btn.classList.remove('recording');
    }
    if (indicator) indicator.style.display = 'none';

    if (recognition) {
        try {
            recognition.stop();
        } catch (e) {}
    }
}

/**
 * Toggle voice input
 */
function toggleVoiceInput() {
    if (isRecording) {
        stopVoiceInput();
    } else {
        const lang = document.getElementById('aiVoiceLang')?.value || 'en-IN';
        startVoiceInput(lang);
    }
}

/**
 * ====== PHOTO MATH SCANNER ======
 */

function openMathScanner() {
    const html = `
        <div class="math-scanner">
            <h2>📷 Math Problem Scanner</h2>
            <p class="section-info">Take a photo of a math problem or type it for the AI to solve</p>

            <div id="scannerView">
                <div class="scanner-options">
                    <button onclick="captureMathPhoto()" class="btn btn-primary btn-large">
                        📸 Take Photo with Camera
                    </button>
                    <button onclick="uploadMathPhoto()" class="btn btn-secondary btn-large">
                        📁 Upload from Gallery
                    </button>
                </div>

                <input type="file" id="mathPhotoInput" accept="image/*" style="display:none" onchange="handlePhotoUpload(event)">
                <input type="file" id="mathCameraInput" accept="image/*" capture="environment" style="display:none" onchange="handlePhotoUpload(event)">

                <div class="divider">
                    <span>OR</span>
                </div>

                <div class="form-group">
                    <label>✍️ Type the math problem:</label>
                    <textarea id="mathProblemInput" rows="3" placeholder="Example: Solve for x: 2x + 5 = 15&#10;Or: What is 247 + 358?"></textarea>
                </div>

                <button onclick="solveMathProblem()" class="btn btn-primary btn-large">
                    🧠 Solve with AI
                </button>
            </div>

            <div id="scannerResult" style="display:none">
                <h3>🤖 AI Solution:</h3>
                <div id="mathSolution" class="math-solution"></div>
                <button onclick="resetScanner()" class="btn btn-secondary">↺ Try Another</button>
            </div>
        </div>
    `;
    openModal(html);
}

function captureMathPhoto() {
    document.getElementById('mathCameraInput').click();
}

function uploadMathPhoto() {
    document.getElementById('mathPhotoInput').click();
}

function handlePhotoUpload(event) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (e) => {
        const img = `<img src="${e.target.result}" style="max-width:100%; max-height:300px; border-radius:8px; margin: 15px 0;" alt="Math Problem">`;
        const inputDiv = document.querySelector('.form-group');
        if (inputDiv) {
            inputDiv.insertAdjacentHTML('beforebegin', `<div class="photo-preview">${img}<p style="text-align:center; color:var(--text-secondary); font-size:13px;">Photo captured! Now describe or type what you see below.</p></div>`);
        }
    };
    reader.readAsDataURL(file);
}

async function solveMathProblem() {
    const problem = document.getElementById('mathProblemInput').value.trim();
    if (!problem) {
        Utils.showSuccess('Please type the math problem or capture a photo');
        return;
    }

    const resultDiv = document.getElementById('mathSolution');
    const scannerView = document.getElementById('scannerView');
    const scannerResult = document.getElementById('scannerResult');

    scannerView.style.display = 'none';
    scannerResult.style.display = 'block';
    resultDiv.innerHTML = '<p>🤔 AI is thinking...</p>';

    try {
        const user = Utils.getCurrentUser();
        const response = await API.doubts.create(
            `Solve this math problem step by step: ${problem}`,
            '',
            'Mathematics',
            user.gradeLevel || 5
        );

        if (response.ai_response) {
            resultDiv.innerHTML = `<div class="solution-content">${escapeHTML(response.ai_response).replace(/\n/g, '<br>')}</div>`;

            // Track for gamification
            if (typeof trackAIQuestion === 'function') trackAIQuestion();
        } else {
            resultDiv.innerHTML = '<p>❌ AI could not solve this. Please try rephrasing.</p>';
        }
    } catch (error) {
        resultDiv.innerHTML = '<p>❌ Error: ' + error.message + '</p>';
    }
}

function resetScanner() {
    document.getElementById('scannerView').style.display = 'block';
    document.getElementById('scannerResult').style.display = 'none';
    document.getElementById('mathProblemInput').value = '';
}

function escapeHTML(str) {
    if (!str) return '';
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}

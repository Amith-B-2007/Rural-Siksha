/**
 * Text-to-Speech - Read aloud PDFs and content
 * Uses Web Speech API (works offline in browsers)
 */

let ttsUtterance = null;
let ttsIsPaused = false;
let ttsCurrentText = '';

/**
 * Check if browser supports TTS
 */
function isTTSSupported() {
    return 'speechSynthesis' in window;
}

/**
 * Get available voices
 */
function getVoices() {
    if (!isTTSSupported()) return [];
    return window.speechSynthesis.getVoices();
}

/**
 * Start reading aloud
 */
function readAloud(text, language = 'en-IN') {
    if (!isTTSSupported()) {
        Utils.showSuccess('Text-to-speech not supported in this browser');
        return;
    }

    // Stop any current speech
    window.speechSynthesis.cancel();

    ttsCurrentText = text;
    ttsUtterance = new SpeechSynthesisUtterance(text);
    ttsUtterance.lang = language;
    ttsUtterance.rate = parseFloat(document.getElementById('ttsRate')?.value || 1);
    ttsUtterance.pitch = 1;
    ttsUtterance.volume = 1;

    // Find appropriate voice
    const voices = getVoices();
    const voice = voices.find(v => v.lang.startsWith(language.split('-')[0])) ||
                  voices.find(v => v.lang.startsWith('en')) ||
                  voices[0];
    if (voice) {
        ttsUtterance.voice = voice;
    }

    ttsUtterance.onstart = () => {
        updateTTSButtons('playing');
    };

    ttsUtterance.onend = () => {
        updateTTSButtons('stopped');
        ttsIsPaused = false;
    };

    ttsUtterance.onerror = (e) => {
        console.error('TTS error:', e);
        updateTTSButtons('stopped');
    };

    window.speechSynthesis.speak(ttsUtterance);
    ttsIsPaused = false;
}

/**
 * Pause/Resume speech
 */
function toggleTTSPause() {
    if (!isTTSSupported()) return;

    if (ttsIsPaused) {
        window.speechSynthesis.resume();
        ttsIsPaused = false;
        updateTTSButtons('playing');
    } else {
        window.speechSynthesis.pause();
        ttsIsPaused = true;
        updateTTSButtons('paused');
    }
}

/**
 * Stop speech
 */
function stopTTS() {
    if (!isTTSSupported()) return;
    window.speechSynthesis.cancel();
    ttsIsPaused = false;
    updateTTSButtons('stopped');
}

/**
 * Update button states
 */
function updateTTSButtons(state) {
    const playBtn = document.getElementById('ttsPlayBtn');
    const pauseBtn = document.getElementById('ttsPauseBtn');
    const stopBtn = document.getElementById('ttsStopBtn');

    if (playBtn && pauseBtn && stopBtn) {
        if (state === 'playing') {
            playBtn.disabled = true;
            pauseBtn.disabled = false;
            stopBtn.disabled = false;
            pauseBtn.innerHTML = '⏸️ Pause';
        } else if (state === 'paused') {
            playBtn.disabled = false;
            pauseBtn.disabled = false;
            stopBtn.disabled = false;
            pauseBtn.innerHTML = '▶️ Resume';
        } else {
            playBtn.disabled = false;
            pauseBtn.disabled = true;
            stopBtn.disabled = true;
        }
    }
}

/**
 * Read a PDF resource by fetching its text
 */
async function readResourceAloud(resourceId, title) {
    try {
        // First, get the resource info
        const resource = currentResources.find(r => r.id === resourceId);
        if (!resource) {
            Utils.showSuccess('Resource not found');
            return;
        }

        // Try to fetch txt version
        const txtUrl = `/api/resources/${resourceId}/download`;
        const response = await fetch(txtUrl, {credentials: 'include'});

        // For PDFs, we need to extract text - use the .txt file if available
        // Use a simpler approach: read the title and description
        const ttsText = `${title}. ${resource.description || ''}. To listen to the full content, please read the PDF.`;

        openTTSPlayer(ttsText, title, getLanguageCode(resource.subject));
    } catch (error) {
        console.error('TTS error:', error);
        Utils.showSuccess('Could not read content');
    }
}

/**
 * Map subject to language code
 */
function getLanguageCode(subject) {
    const map = {
        'Hindi': 'hi-IN',
        'Kannada': 'kn-IN',
    };
    return map[subject] || 'en-IN';
}

/**
 * Open TTS player modal
 */
function openTTSPlayer(text, title, language = 'en-IN') {
    const voices = getVoices();
    const langOptions = [
        {code: 'en-IN', name: 'English (India)'},
        {code: 'en-US', name: 'English (US)'},
        {code: 'en-GB', name: 'English (UK)'},
        {code: 'hi-IN', name: 'Hindi'},
        {code: 'kn-IN', name: 'Kannada'},
        {code: 'ta-IN', name: 'Tamil'},
        {code: 'te-IN', name: 'Telugu'},
    ];

    const html = `
        <div class="tts-player">
            <h2>🔊 Text-to-Speech Player</h2>
            <p class="section-info"><strong>${title}</strong></p>

            <div class="tts-controls">
                <div class="form-group">
                    <label>🌐 Language:</label>
                    <select id="ttsLang" onchange="changeTTSLanguage()">
                        ${langOptions.map(l =>
                            `<option value="${l.code}" ${l.code === language ? 'selected' : ''}>${l.name}</option>`
                        ).join('')}
                    </select>
                </div>

                <div class="form-group">
                    <label>⚡ Speed: <span id="rateValue">1.0x</span></label>
                    <input type="range" id="ttsRate" min="0.5" max="2" step="0.1" value="1"
                           oninput="document.getElementById('rateValue').textContent = this.value + 'x'">
                </div>

                <div class="tts-buttons">
                    <button id="ttsPlayBtn" onclick="ttsStart()" class="btn btn-primary">▶️ Play</button>
                    <button id="ttsPauseBtn" onclick="toggleTTSPause()" class="btn btn-secondary" disabled>⏸️ Pause</button>
                    <button id="ttsStopBtn" onclick="stopTTS()" class="btn btn-danger" disabled>⏹️ Stop</button>
                </div>
            </div>

            <div class="tts-text-display">
                <h4>📝 Content:</h4>
                <textarea id="ttsTextArea" rows="15" style="width:100%; padding:10px; font-family:inherit; font-size:14px;">${escapeTTS(text)}</textarea>
            </div>

            <div class="tts-info">
                <p>💡 <strong>Tip:</strong> Click "Play" to hear the content read aloud. You can edit the text or paste any content above!</p>
            </div>

            <button onclick="stopTTS(); closeModal()" class="btn btn-primary">Close</button>
        </div>
    `;

    openModal(html);

    // Wait for voices to load
    if (speechSynthesis.getVoices().length === 0) {
        speechSynthesis.onvoiceschanged = () => {
            // Voices loaded
        };
    }
}

/**
 * Start TTS from text area
 */
function ttsStart() {
    const text = document.getElementById('ttsTextArea').value;
    const lang = document.getElementById('ttsLang').value;
    if (text) {
        readAloud(text, lang);
    }
}

/**
 * Change language
 */
function changeTTSLanguage() {
    // Stop and restart with new language if currently playing
    if (window.speechSynthesis.speaking) {
        stopTTS();
    }
}

/**
 * Escape HTML
 */
function escapeTTS(str) {
    if (!str) return '';
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}

/**
 * Quick read - read any selected text
 */
function readSelectedText() {
    const selection = window.getSelection().toString();
    if (selection) {
        readAloud(selection);
    } else {
        Utils.showSuccess('Please select some text first');
    }
}

// Load voices when ready
if (isTTSSupported()) {
    window.speechSynthesis.onvoiceschanged = () => {
        console.log('TTS voices loaded:', getVoices().length);
    };
}

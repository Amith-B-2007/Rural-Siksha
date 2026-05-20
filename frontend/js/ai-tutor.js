/**
 * AI Tutor - Real-time chat with AI
 * Ollama runs LOCALLY so it works without internet!
 * Built-in fallback for when Ollama is also unreachable
 */

let chatHistory = [];

// Offline fallback knowledge base (used only when Ollama is completely unreachable)
const OFFLINE_FALLBACKS = {
    'photosynthesis': 'Photosynthesis is how plants make their own food using sunlight, water, and carbon dioxide. The formula is: 6CO₂ + 6H₂O + Sunlight → C₆H₁₂O₆ + 6O₂. This happens in the chloroplasts of leaves which contain chlorophyll. The byproduct, oxygen, is what we breathe!',
    'multiplication': 'Multiplication is repeated addition. For example, 3 × 4 means adding 3 four times: 3+3+3+3 = 12. Or adding 4 three times: 4+4+4 = 12. The symbol × means "multiply" or "times". Tables 2-10 are very useful to memorize!',
    'noun': 'A noun is a word that names a person, place, animal, or thing. Examples: teacher (person), school (place), dog (animal), book (thing). Proper nouns are specific names like "Delhi" or "Ravi" and start with capital letters.',
    'verb': 'A verb is a word that shows action or being. Examples of action verbs: run, jump, eat, write, play. Examples of being verbs: is, am, are, was, were. Every sentence needs a verb!',
    'gravity': 'Gravity is the force that pulls objects towards each other. Earth\'s gravity pulls everything towards its center, which is why things fall down. Sir Isaac Newton discovered gravity after seeing an apple fall from a tree.',
    'fractions': 'Fractions show parts of a whole. Like 1/2 means 1 part out of 2 equal parts. The top number is the numerator, bottom is denominator. Examples: 1/2 (half), 1/4 (quarter), 3/4 (three quarters).',
    'india': 'India is a country in South Asia with a population of over 1.4 billion. Capital: New Delhi. National animal: Tiger. National bird: Peacock. India got independence on 15 August 1947 from British rule.',
    'water cycle': 'The water cycle has 4 main steps: 1) Evaporation - water from oceans/rivers becomes vapor when heated by sun, 2) Condensation - vapor cools and forms clouds, 3) Precipitation - rain or snow falls from clouds, 4) Collection - water collects back in rivers and oceans.',
    'planets': 'Our solar system has 8 planets in order from Sun: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune. Memory trick: "My Very Educated Mother Just Served Us Noodles". Jupiter is the largest. Earth is the only planet with life.',
    'addition': 'Addition is combining numbers to get a total. The symbol is +. Example: 5 + 3 = 8. When adding 2-digit numbers, add ones first, then tens.',
    'subtraction': 'Subtraction is taking away one number from another. The symbol is -. Example: 10 - 4 = 6. When the bottom digit is bigger, borrow 1 from the next column.',
    'algebra': 'Algebra uses letters (like x, y) to represent unknown numbers. Example: If 2x + 3 = 11, find x. Step 1: 2x = 11-3 = 8. Step 2: x = 8/2 = 4. So x=4.',
    'tenses': 'English has 3 main tenses: PAST (already happened), PRESENT (now), FUTURE (will happen). Examples: "I played" (past), "I play" (present), "I will play" (future).',
    'parts of plant': 'A plant has 5 main parts: ROOTS absorb water, STEM supports the plant, LEAVES make food through photosynthesis, FLOWERS are reproductive parts, FRUITS contain seeds.',
    'gandhi': 'Mahatma Gandhi (1869-1948) is called the "Father of the Nation" in India. He led India\'s freedom struggle using non-violence (ahimsa). Famous events: Salt March (1930), Quit India Movement (1942). India became independent on 15 August 1947.',
    'default': 'Hmm, I need a bit more information to answer that. Try asking about specific topics like math (addition, fractions, algebra), science (photosynthesis, gravity, water cycle), English (nouns, verbs, tenses), or social studies (India, planets, Gandhi).'
};

/**
 * Find a fallback answer for offline mode
 */
function findOfflineAnswer(question) {
    const q = question.toLowerCase();
    for (const [keyword, answer] of Object.entries(OFFLINE_FALLBACKS)) {
        if (keyword !== 'default' && q.includes(keyword)) {
            return answer;
        }
    }
    return OFFLINE_FALLBACKS.default;
}

/**
 * Check AI status for the AI Tutor tab
 */
async function checkAiTutorStatus() {
    const banner = document.getElementById('aiStatusBannerTutor');
    if (!banner) return;

    try {
        const status = await API.doubts.aiStatus();
        if (status.available) {
            banner.innerHTML = `<span>✅ Local AI Tutor is online and ready! (Model: ${status.model}) - Works offline too!</span>`;
            banner.className = 'ai-status-banner ok';
        } else {
            banner.innerHTML = '<span>⚠️ Ollama service is not running. Start Ollama on your computer to use AI Tutor.</span>';
            banner.className = 'ai-status-banner warn';
        }
    } catch (error) {
        // Even if status check fails, Ollama might still work
        banner.innerHTML = '<span>🤖 AI Tutor ready - Try asking a question!</span>';
        banner.className = 'ai-status-banner ok';
    }
}

/**
 * Add a message to chat area
 */
function addChatMessage(type, text, subject = '') {
    const chatArea = document.getElementById('aiChatArea');
    if (!chatArea) return;

    const messageDiv = document.createElement('div');
    messageDiv.className = `chat-message ${type}`;

    const avatar = type === 'user' ? '👨‍🎓' : '🤖';
    const sender = type === 'user' ? 'You' : 'AI Tutor';

    messageDiv.innerHTML = `
        <div class="chat-avatar">${avatar}</div>
        <div class="chat-bubble">
            <div class="chat-sender">${sender}${subject ? ` <span class="chat-subject">${subject}</span>` : ''}</div>
            <div class="chat-text">${escapeHTML(text).replace(/\n/g, '<br>')}</div>
        </div>
    `;

    chatArea.appendChild(messageDiv);
    chatArea.scrollTop = chatArea.scrollHeight;

    chatHistory.push({type, text, subject});
}

/**
 * Add loading indicator
 */
function addLoadingMessage() {
    const chatArea = document.getElementById('aiChatArea');
    const loadingDiv = document.createElement('div');
    loadingDiv.className = 'chat-message ai loading-message';
    loadingDiv.id = 'aiLoadingMessage';
    loadingDiv.innerHTML = `
        <div class="chat-avatar">🤖</div>
        <div class="chat-bubble">
            <div class="chat-sender">AI Tutor</div>
            <div class="chat-text">
                <span class="thinking-dots">
                    <span>.</span><span>.</span><span>.</span>
                </span>
                Thinking with Ollama AI...
            </div>
        </div>
    `;
    chatArea.appendChild(loadingDiv);
    chatArea.scrollTop = chatArea.scrollHeight;
}

/**
 * Remove loading indicator
 */
function removeLoadingMessage() {
    const loading = document.getElementById('aiLoadingMessage');
    if (loading) loading.remove();
}

/**
 * Try direct Ollama connection (bypasses Flask if needed)
 */
async function tryDirectOllama(question, subject, gradeLevel) {
    const systemPrompt = "You are a friendly, patient AI tutor helping rural school students in India (grades 1-10). Provide clear, simple, age-appropriate explanations. Use examples that are relatable. Keep responses concise but thorough.";

    const contextParts = [];
    if (subject) contextParts.push(`Subject: ${subject}`);
    if (gradeLevel) contextParts.push(`Grade Level: ${gradeLevel}`);
    const context = contextParts.join('\n');
    const fullPrompt = context ? `${context}\n\nStudent's Question: ${question}\n\nAnswer:` : `Student's Question: ${question}\n\nAnswer:`;

    try {
        const response = await fetch('http://localhost:11434/api/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                model: 'llama3:latest',
                prompt: fullPrompt,
                system: systemPrompt,
                stream: false,
                options: {
                    temperature: 0.7,
                    top_p: 0.9
                }
            })
        });

        if (response.ok) {
            const data = await response.json();
            return data.response ? data.response.trim() : null;
        }
    } catch (e) {
        console.log('Direct Ollama call failed:', e);
    }
    return null;
}

/**
 * Handle AI Tutor form submission
 * Ollama is LOCAL so always try it - don't check internet connectivity
 */
async function handleAiTutorSubmit(e) {
    e.preventDefault();

    const user = Utils.getCurrentUser();
    if (!user) return;

    const subject = document.getElementById('aiSubject').value;
    const question = document.getElementById('aiQuestion').value.trim();

    if (!question) return;

    // Hide welcome message
    const welcome = document.querySelector('.ai-welcome');
    if (welcome) welcome.style.display = 'none';

    // Add user message
    addChatMessage('user', question, subject);

    // Clear input
    document.getElementById('aiQuestion').value = '';

    // Show loading
    const btn = document.getElementById('aiSubmitBtn');
    btn.disabled = true;
    document.getElementById('aiSendIcon').textContent = '⏳ Thinking...';

    addLoadingMessage();

    const viewingGrade = getViewingGrade() || user.gradeLevel;
    const subj = subject || 'General';

    let aiResponse = null;
    let usedFallback = false;
    let lastError = null;

    // STRATEGY 1: Try Flask API (which calls local Ollama)
    // This works whether or not we have internet because Flask is also local
    try {
        const response = await API.doubts.create(question, '', subj, viewingGrade);
        if (response.ai_response) {
            aiResponse = response.ai_response;
        } else if (response.ai_error) {
            lastError = response.ai_error;
        }
    } catch (error) {
        console.log('Flask API failed, will try direct Ollama:', error);
        lastError = error.message;
    }

    // STRATEGY 2: If Flask API failed, try Ollama directly (bypass)
    if (!aiResponse) {
        console.log('Trying direct Ollama connection...');
        aiResponse = await tryDirectOllama(question, subj, viewingGrade);
        if (aiResponse) {
            console.log('Direct Ollama succeeded!');
        }
    }

    // STRATEGY 3: If both failed, use built-in fallback knowledge
    if (!aiResponse) {
        console.log('Using built-in fallback');
        aiResponse = `${findOfflineAnswer(question)}\n\n💡 (Built-in offline answer - Ollama is currently unreachable. Make sure Ollama is running on your computer.)`;
        usedFallback = true;
    }

    removeLoadingMessage();
    addChatMessage('ai', aiResponse, subj);

    btn.disabled = false;
    document.getElementById('aiSendIcon').textContent = '📨 Ask';
}

/**
 * Get currently selected viewing grade
 */
function getViewingGrade() {
    const selector = document.getElementById('viewingGrade');
    return selector ? parseInt(selector.value) : null;
}

/**
 * HTML escape helper
 */
function escapeHTML(str) {
    if (!str) return '';
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}

/**
 * Setup event listeners
 */
document.addEventListener('DOMContentLoaded', () => {
    const aiTutorBtn = document.getElementById('aiTutorBtn');
    if (aiTutorBtn) {
        aiTutorBtn.addEventListener('click', () => {
            switchPanel('aiTutorPanel', aiTutorBtn);
            checkAiTutorStatus();
        });
    }

    const aiTutorForm = document.getElementById('aiTutorForm');
    if (aiTutorForm) {
        aiTutorForm.addEventListener('submit', handleAiTutorSubmit);
    }
});

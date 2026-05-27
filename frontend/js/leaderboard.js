/**
 * Leaderboard System
 */

function showLeaderboard() {
    const user = Utils.getCurrentUser();
    if (!user) return;

    // Get current user's gamification data
    const userData = typeof getGameData === 'function' ? getGameData() : {xp: 0, level: 1, streak: 0, badges: []};

    // Mock leaderboard data (in production, this would come from backend)
    const mockStudents = [
        {name: 'Priya Sharma', xp: 2450, level: 25, streak: 42, badges: 11, school: 'ZP School A'},
        {name: 'Arjun Patel', xp: 2180, level: 22, streak: 28, badges: 10, school: 'Govt School B'},
        {name: 'Sneha Reddy', xp: 1980, level: 20, streak: 35, badges: 9, school: 'ZP School A'},
        {name: 'Rohit Kumar', xp: 1750, level: 18, streak: 21, badges: 8, school: 'Govt School C'},
        {name: 'Anjali Singh', xp: 1650, level: 17, streak: 15, badges: 8, school: 'ZP School B'},
        {name: user.fullName + ' (You)', xp: userData.xp, level: userData.level, streak: userData.streak, badges: userData.badges.length, school: 'Your School', isUser: true},
        {name: 'Karan Verma', xp: 1420, level: 15, streak: 12, badges: 7, school: 'Govt School A'},
        {name: 'Pooja Iyer', xp: 1280, level: 13, streak: 8, badges: 6, school: 'ZP School C'},
        {name: 'Suresh Babu', xp: 1100, level: 12, streak: 5, badges: 5, school: 'Govt School B'},
        {name: 'Meera Nair', xp: 950, level: 10, streak: 4, badges: 5, school: 'ZP School A'},
    ];

    // Sort by XP
    mockStudents.sort((a, b) => b.xp - a.xp);

    const userRank = mockStudents.findIndex(s => s.isUser) + 1;

    const html = `
        <div class="leaderboard-container">
            <h2>🏆 School Leaderboard</h2>
            <p class="section-info">See how you rank among students!</p>

            <div class="user-rank-card">
                <div class="rank-display">
                    <div class="rank-number">#${userRank}</div>
                    <div>Your Rank</div>
                </div>
                <div class="rank-stats">
                    <span>⚡ ${userData.xp} XP</span>
                    <span>📊 Level ${userData.level}</span>
                    <span>🔥 ${userData.streak} day streak</span>
                </div>
            </div>

            <div class="leaderboard-table">
                <div class="leaderboard-header">
                    <span>Rank</span>
                    <span>Student</span>
                    <span>XP</span>
                    <span>Level</span>
                    <span>Streak</span>
                    <span>Badges</span>
                </div>
                ${mockStudents.map((student, idx) => `
                    <div class="leaderboard-row ${student.isUser ? 'user-row' : ''} ${idx < 3 ? 'top-three' : ''}">
                        <span class="rank">
                            ${idx === 0 ? '🥇' : idx === 1 ? '🥈' : idx === 2 ? '🥉' : '#' + (idx + 1)}
                        </span>
                        <span class="student-name">${student.name}</span>
                        <span class="stat">${student.xp}</span>
                        <span class="stat">${student.level}</span>
                        <span class="stat">${student.streak}🔥</span>
                        <span class="stat">${student.badges}🏅</span>
                    </div>
                `).join('')}
            </div>

            <p class="leaderboard-tip">
                💡 <strong>Tip:</strong> Take more quizzes, read resources, and maintain your streak to climb the leaderboard!
            </p>

            <button onclick="closeModal()" class="btn btn-primary">Close</button>
        </div>
    `;

    openModal(html);
}

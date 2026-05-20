from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from extensions import db, login_manager


class User(UserMixin, db.Model):
    """User model for students and teachers"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    grade_level = db.Column(db.Integer)
    subject = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    resources = db.relationship('Resource', backref='creator', lazy=True, foreign_keys='Resource.created_by')
    progress = db.relationship('StudentProgress', backref='student', lazy=True)
    sessions = db.relationship('Session', backref='user', lazy=True)
    quizzes_created = db.relationship('Quiz', backref='creator', lazy=True, foreign_keys='Quiz.created_by')
    quiz_attempts = db.relationship('QuizAttempt', backref='student', lazy=True)
    doubts = db.relationship('Doubt', backref='student', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.email}>'


class Resource(db.Model):
    """Educational resources (PDFs, images, videos, etc.)"""
    __tablename__ = 'resources'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    subject = db.Column(db.String(100), nullable=False, index=True)
    grade_level = db.Column(db.Integer, nullable=False, index=True)
    content_type = db.Column(db.String(20), nullable=False)
    file_path = db.Column(db.String(255))
    file_size = db.Column(db.Integer)
    youtube_url = db.Column(db.String(500))
    youtube_channel = db.Column(db.String(100))
    ncert_url = db.Column(db.String(500))
    ncert_chapter = db.Column(db.String(200))
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_published = db.Column(db.Boolean, default=False)

    __table_args__ = (
        db.Index('idx_resources_grade_subject', 'grade_level', 'subject'),
    )

    def __repr__(self):
        return f'<Resource {self.title}>'


class Quiz(db.Model):
    """Quiz model"""
    __tablename__ = 'quizzes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    subject = db.Column(db.String(100), nullable=False, index=True)
    grade_level = db.Column(db.Integer, nullable=False, index=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    total_questions = db.Column(db.Integer, default=0)
    passing_score = db.Column(db.Float, default=60.0)
    time_limit_minutes = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_published = db.Column(db.Boolean, default=True)

    questions = db.relationship('QuizQuestion', backref='quiz', lazy=True, cascade='all, delete-orphan')
    attempts = db.relationship('QuizAttempt', backref='quiz', lazy=True)

    __table_args__ = (
        db.Index('idx_quizzes_grade_subject', 'grade_level', 'subject'),
    )

    def __repr__(self):
        return f'<Quiz {self.title}>'


class QuizQuestion(db.Model):
    """Individual quiz questions"""
    __tablename__ = 'quiz_questions'

    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id', ondelete='CASCADE'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    question_type = db.Column(db.String(20), nullable=False)  # 'mcq', 'short_answer', 'essay'
    option_a = db.Column(db.String(500))
    option_b = db.Column(db.String(500))
    option_c = db.Column(db.String(500))
    option_d = db.Column(db.String(500))
    correct_option = db.Column(db.String(1))  # 'A', 'B', 'C', 'D'
    expected_answer = db.Column(db.Text)
    explanation = db.Column(db.Text)
    question_order = db.Column(db.Integer, default=0)
    marks = db.Column(db.Float, default=1.0)

    def __repr__(self):
        return f'<QuizQuestion {self.id}>'


class QuizAttempt(db.Model):
    """Student quiz attempts"""
    __tablename__ = 'quiz_attempts'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'), nullable=False)
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    submitted_at = db.Column(db.DateTime)
    score = db.Column(db.Float)
    total_marks = db.Column(db.Float)
    percentage = db.Column(db.Float)
    status = db.Column(db.String(20), default='in_progress')  # 'in_progress', 'submitted', 'graded'

    answers = db.relationship('QuizAnswer', backref='attempt', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<QuizAttempt student={self.student_id} quiz={self.quiz_id}>'


class QuizAnswer(db.Model):
    """Individual quiz answers"""
    __tablename__ = 'quiz_answers'

    id = db.Column(db.Integer, primary_key=True)
    attempt_id = db.Column(db.Integer, db.ForeignKey('quiz_attempts.id', ondelete='CASCADE'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('quiz_questions.id'), nullable=False)
    student_answer = db.Column(db.Text)
    is_correct = db.Column(db.Boolean)
    marks_awarded = db.Column(db.Float, default=0.0)
    graded_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    graded_at = db.Column(db.DateTime)
    feedback = db.Column(db.Text)

    question = db.relationship('QuizQuestion', backref='answers', lazy=True)

    def __repr__(self):
        return f'<QuizAnswer attempt={self.attempt_id} q={self.question_id}>'


class Doubt(db.Model):
    """Student doubts/questions"""
    __tablename__ = 'doubts'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    grade_level = db.Column(db.Integer, nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    question_detail = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='open')  # 'open', 'in_progress', 'resolved', 'closed'
    resolved_at = db.Column(db.DateTime)

    responses = db.relationship('DoubtResponse', backref='doubt', lazy=True, cascade='all, delete-orphan')

    __table_args__ = (
        db.Index('idx_doubts_status_student', 'status', 'student_id'),
    )

    def __repr__(self):
        return f'<Doubt {self.id}>'


class DoubtResponse(db.Model):
    """AI and teacher responses to doubts"""
    __tablename__ = 'doubt_responses'

    id = db.Column(db.Integer, primary_key=True)
    doubt_id = db.Column(db.Integer, db.ForeignKey('doubts.id', ondelete='CASCADE'), nullable=False)
    response_type = db.Column(db.String(10), nullable=False)  # 'ai' or 'teacher'
    responder_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # NULL for AI
    response_text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_helpful = db.Column(db.Boolean)

    responder = db.relationship('User', foreign_keys=[responder_id])

    def __repr__(self):
        return f'<DoubtResponse {self.id} type={self.response_type}>'


class QuestionPaper(db.Model):
    """Previous year question papers"""
    __tablename__ = 'question_papers'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    subject = db.Column(db.String(100), nullable=False, index=True)
    grade_level = db.Column(db.Integer, nullable=False, index=True)
    year = db.Column(db.Integer, nullable=False)
    exam_type = db.Column(db.String(50))  # 'half_yearly', 'annual', 'board', 'unit_test'
    duration_minutes = db.Column(db.Integer)
    total_marks = db.Column(db.Integer)
    file_path = db.Column(db.String(255))
    content_type = db.Column(db.String(20), default='txt')
    file_size = db.Column(db.Integer)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_published = db.Column(db.Boolean, default=True)

    __table_args__ = (
        db.Index('idx_papers_grade_subject_year', 'grade_level', 'subject', 'year'),
    )

    def __repr__(self):
        return f'<QuestionPaper {self.title} {self.year}>'


class StudentProgress(db.Model):
    """Denormalized student progress tracking"""
    __tablename__ = 'student_progress'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    grade_level = db.Column(db.Integer, nullable=False)
    total_questions_answered = db.Column(db.Integer, default=0)
    correct_answers = db.Column(db.Integer, default=0)
    quizzes_completed = db.Column(db.Integer, default=0)
    total_score = db.Column(db.Float, default=0.0)
    doubts_resolved = db.Column(db.Integer, default=0)
    resources_viewed = db.Column(db.Integer, default=0)
    last_activity = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (
        db.UniqueConstraint('student_id', 'subject', name='uq_student_subject'),
    )

    def __repr__(self):
        return f'<StudentProgress {self.student_id} {self.subject}>'


class Session(db.Model):
    """Session tracking for offline awareness"""
    __tablename__ = 'sessions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    session_token = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_activity = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Session {self.user_id}>'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

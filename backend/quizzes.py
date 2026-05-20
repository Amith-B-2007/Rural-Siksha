"""
Quiz routes - list, take, submit, grade quizzes
"""

from datetime import datetime
from flask import Blueprint, request, jsonify
from flask_login import current_user
from extensions import db
from backend.models import Quiz, QuizQuestion, QuizAttempt, QuizAnswer, StudentProgress
from backend.utils import require_login

quizzes_bp = Blueprint('quizzes', __name__, url_prefix='/api/quizzes')


@quizzes_bp.route('', methods=['GET'])
@require_login
def list_quizzes():
    """List available quizzes by grade and subject"""
    grade = request.args.get('grade', type=int)
    subject = request.args.get('subject', type=str)

    query = Quiz.query.filter_by(is_published=True)

    if grade:
        query = query.filter_by(grade_level=grade)
    if subject:
        query = query.filter_by(subject=subject)

    quizzes = query.all()

    return jsonify([{
        'id': q.id,
        'title': q.title,
        'description': q.description,
        'subject': q.subject,
        'grade_level': q.grade_level,
        'total_questions': q.total_questions,
        'passing_score': q.passing_score,
        'time_limit_minutes': q.time_limit_minutes,
        'created_at': q.created_at.isoformat()
    } for q in quizzes]), 200


@quizzes_bp.route('/<int:quiz_id>', methods=['GET'])
@require_login
def get_quiz(quiz_id):
    """Get quiz with questions (without correct answers)"""
    quiz = Quiz.query.get_or_404(quiz_id)

    if not quiz.is_published:
        return jsonify({'error': 'Quiz not available'}), 403

    questions = sorted(quiz.questions, key=lambda q: q.question_order)

    return jsonify({
        'id': quiz.id,
        'title': quiz.title,
        'description': quiz.description,
        'subject': quiz.subject,
        'grade_level': quiz.grade_level,
        'total_questions': quiz.total_questions,
        'time_limit_minutes': quiz.time_limit_minutes,
        'questions': [{
            'id': q.id,
            'question_text': q.question_text,
            'question_type': q.question_type,
            'option_a': q.option_a,
            'option_b': q.option_b,
            'option_c': q.option_c,
            'option_d': q.option_d,
            'marks': q.marks,
            'order': q.question_order
        } for q in questions]
    }), 200


@quizzes_bp.route('/<int:quiz_id>/start', methods=['POST'])
@require_login
def start_quiz(quiz_id):
    """Start a new quiz attempt"""
    if current_user.role != 'student':
        return jsonify({'error': 'Only students can take quizzes'}), 403

    quiz = Quiz.query.get_or_404(quiz_id)

    # Check for in-progress attempt
    existing = QuizAttempt.query.filter_by(
        student_id=current_user.id,
        quiz_id=quiz_id,
        status='in_progress'
    ).first()

    if existing:
        return jsonify({
            'attempt_id': existing.id,
            'started_at': existing.started_at.isoformat(),
            'message': 'Resuming existing attempt'
        }), 200

    # Create new attempt
    attempt = QuizAttempt(
        student_id=current_user.id,
        quiz_id=quiz_id,
        status='in_progress'
    )
    db.session.add(attempt)
    db.session.commit()

    return jsonify({
        'attempt_id': attempt.id,
        'started_at': attempt.started_at.isoformat(),
        'time_limit_minutes': quiz.time_limit_minutes
    }), 201


@quizzes_bp.route('/<int:quiz_id>/submit', methods=['POST'])
@require_login
def submit_quiz(quiz_id):
    """Submit quiz answers and get graded"""
    if current_user.role != 'student':
        return jsonify({'error': 'Only students can submit quizzes'}), 403

    data = request.get_json()
    if not data or 'answers' not in data:
        return jsonify({'error': 'Missing answers'}), 400

    quiz = Quiz.query.get_or_404(quiz_id)
    attempt_id = data.get('attempt_id')

    # Get or create attempt
    if attempt_id:
        attempt = QuizAttempt.query.get(attempt_id)
        if not attempt or attempt.student_id != current_user.id:
            return jsonify({'error': 'Invalid attempt'}), 403
    else:
        attempt = QuizAttempt(
            student_id=current_user.id,
            quiz_id=quiz_id,
            status='in_progress'
        )
        db.session.add(attempt)
        db.session.flush()

    # Grade answers
    answers = data['answers']
    total_score = 0.0
    total_marks = 0.0
    questions_dict = {q.id: q for q in quiz.questions}
    needs_review = False

    for ans in answers:
        question_id = ans.get('question_id')
        student_answer = ans.get('answer', '').strip()

        if question_id not in questions_dict:
            continue

        question = questions_dict[question_id]
        total_marks += question.marks

        # Auto-grade MCQ
        if question.question_type == 'mcq':
            is_correct = (student_answer.upper() == question.correct_option)
            marks_awarded = question.marks if is_correct else 0.0
            total_score += marks_awarded

            answer_record = QuizAnswer(
                attempt_id=attempt.id,
                question_id=question_id,
                student_answer=student_answer,
                is_correct=is_correct,
                marks_awarded=marks_awarded,
                graded_at=datetime.utcnow()
            )
        # Auto-grade short answer (simple exact match)
        elif question.question_type == 'short_answer':
            expected = (question.expected_answer or '').strip().lower()
            given = student_answer.lower()
            is_correct = (expected == given) if expected else None
            marks_awarded = question.marks if is_correct else 0.0
            total_score += marks_awarded

            answer_record = QuizAnswer(
                attempt_id=attempt.id,
                question_id=question_id,
                student_answer=student_answer,
                is_correct=is_correct,
                marks_awarded=marks_awarded,
                graded_at=datetime.utcnow()
            )
        # Essay - needs teacher review
        else:
            needs_review = True
            answer_record = QuizAnswer(
                attempt_id=attempt.id,
                question_id=question_id,
                student_answer=student_answer,
                is_correct=None,
                marks_awarded=0.0
            )

        db.session.add(answer_record)

    # Update attempt
    attempt.score = total_score
    attempt.total_marks = total_marks
    attempt.percentage = (total_score / total_marks * 100) if total_marks > 0 else 0.0
    attempt.submitted_at = datetime.utcnow()
    attempt.status = 'graded' if not needs_review else 'submitted'

    # Update student progress
    update_student_progress(
        current_user.id,
        quiz.subject,
        quiz.grade_level,
        correct_count=sum(1 for a in answers if a.get('question_id') in questions_dict
                          and questions_dict[a['question_id']].question_type == 'mcq'
                          and a.get('answer', '').upper() == questions_dict[a['question_id']].correct_option),
        total_count=len([a for a in answers if a.get('question_id') in questions_dict
                         and questions_dict[a['question_id']].question_type == 'mcq']),
        quiz_score=attempt.percentage
    )

    db.session.commit()

    return jsonify({
        'attempt_id': attempt.id,
        'score': total_score,
        'total_marks': total_marks,
        'percentage': attempt.percentage,
        'status': attempt.status,
        'passed': attempt.percentage >= quiz.passing_score,
        'needs_review': needs_review
    }), 200


@quizzes_bp.route('/<int:quiz_id>/results/<int:attempt_id>', methods=['GET'])
@require_login
def get_results(quiz_id, attempt_id):
    """Get detailed quiz results"""
    attempt = QuizAttempt.query.get_or_404(attempt_id)

    if attempt.student_id != current_user.id and current_user.role != 'teacher':
        return jsonify({'error': 'Access denied'}), 403

    quiz = Quiz.query.get_or_404(quiz_id)
    answer_details = []

    for ans in attempt.answers:
        q = ans.question
        answer_details.append({
            'question_id': q.id,
            'question_text': q.question_text,
            'question_type': q.question_type,
            'student_answer': ans.student_answer,
            'correct_answer': q.correct_option if q.question_type == 'mcq' else q.expected_answer,
            'is_correct': ans.is_correct,
            'marks_awarded': ans.marks_awarded,
            'max_marks': q.marks,
            'explanation': q.explanation
        })

    return jsonify({
        'attempt_id': attempt.id,
        'quiz_title': quiz.title,
        'score': attempt.score,
        'total_marks': attempt.total_marks,
        'percentage': attempt.percentage,
        'status': attempt.status,
        'submitted_at': attempt.submitted_at.isoformat() if attempt.submitted_at else None,
        'answers': answer_details
    }), 200


@quizzes_bp.route('/create', methods=['POST'])
@require_login
def create_quiz():
    """Create a new quiz (teacher only)"""
    if current_user.role != 'teacher':
        return jsonify({'error': 'Only teachers can create quizzes'}), 403

    data = request.get_json()
    if not data:
        return jsonify({'error': 'Missing data'}), 400

    required = ['title', 'subject', 'grade_level', 'questions']
    for field in required:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400

    if not isinstance(data['questions'], list) or len(data['questions']) == 0:
        return jsonify({'error': 'Questions must be a non-empty list'}), 400

    try:
        quiz = Quiz(
            title=data['title'],
            description=data.get('description', ''),
            subject=data['subject'],
            grade_level=data['grade_level'],
            created_by=current_user.id,
            total_questions=len(data['questions']),
            passing_score=data.get('passing_score', 60.0),
            time_limit_minutes=data.get('time_limit_minutes'),
            is_published=True
        )
        db.session.add(quiz)
        db.session.flush()

        for idx, q_data in enumerate(data['questions']):
            question = QuizQuestion(
                quiz_id=quiz.id,
                question_text=q_data['question_text'],
                question_type=q_data.get('question_type', 'mcq'),
                option_a=q_data.get('option_a'),
                option_b=q_data.get('option_b'),
                option_c=q_data.get('option_c'),
                option_d=q_data.get('option_d'),
                correct_option=q_data.get('correct_option'),
                expected_answer=q_data.get('expected_answer'),
                explanation=q_data.get('explanation'),
                question_order=idx,
                marks=q_data.get('marks', 1.0)
            )
            db.session.add(question)

        db.session.commit()
        return jsonify({
            'message': 'Quiz created successfully',
            'quiz_id': quiz.id,
            'title': quiz.title
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to create quiz: {str(e)}'}), 500


@quizzes_bp.route('/my-attempts', methods=['GET'])
@require_login
def my_attempts():
    """Get student's quiz attempts"""
    attempts = QuizAttempt.query.filter_by(student_id=current_user.id).all()

    return jsonify([{
        'attempt_id': a.id,
        'quiz_id': a.quiz_id,
        'quiz_title': a.quiz.title,
        'subject': a.quiz.subject,
        'score': a.score,
        'percentage': a.percentage,
        'status': a.status,
        'submitted_at': a.submitted_at.isoformat() if a.submitted_at else None
    } for a in attempts]), 200


def update_student_progress(student_id, subject, grade_level, correct_count, total_count, quiz_score):
    """Update or create student progress record"""
    progress = StudentProgress.query.filter_by(
        student_id=student_id,
        subject=subject
    ).first()

    if not progress:
        progress = StudentProgress(
            student_id=student_id,
            subject=subject,
            grade_level=grade_level,
            total_questions_answered=0,
            correct_answers=0,
            quizzes_completed=0,
            total_score=0.0,
            doubts_resolved=0,
            resources_viewed=0
        )
        db.session.add(progress)
        db.session.flush()

    progress.total_questions_answered = (progress.total_questions_answered or 0) + total_count
    progress.correct_answers = (progress.correct_answers or 0) + correct_count
    progress.quizzes_completed = (progress.quizzes_completed or 0) + 1
    progress.total_score = (progress.total_score or 0.0) + (quiz_score or 0.0)
    progress.last_activity = datetime.utcnow()

"""
Progress tracking - student dashboard and analytics
"""

from flask import Blueprint, jsonify
from flask_login import current_user
from sqlalchemy import func
from extensions import db
from backend.models import StudentProgress, QuizAttempt, Doubt, User
from backend.utils import require_login

progress_bp = Blueprint('progress', __name__, url_prefix='/api/progress')


@progress_bp.route('', methods=['GET'])
@require_login
def get_progress():
    """Get student's overall progress dashboard"""
    if current_user.role == 'student':
        return get_student_progress(current_user.id)
    elif current_user.role == 'teacher':
        return get_teacher_overview()
    else:
        return jsonify({'error': 'Invalid role'}), 403


def get_student_progress(student_id):
    """Get detailed progress for a student"""
    progress_records = StudentProgress.query.filter_by(student_id=student_id).all()

    # Overall stats
    total_quizzes = sum(p.quizzes_completed for p in progress_records)
    total_correct = sum(p.correct_answers for p in progress_records)
    total_answered = sum(p.total_questions_answered for p in progress_records)
    total_resources = sum(p.resources_viewed for p in progress_records)

    # Calculate average score from quiz attempts
    attempts = QuizAttempt.query.filter_by(
        student_id=student_id,
        status='graded'
    ).all()
    avg_score = sum(a.percentage for a in attempts) / len(attempts) if attempts else 0

    # Count resolved doubts
    resolved_doubts = Doubt.query.filter_by(
        student_id=student_id,
        status='resolved'
    ).count()

    # By subject
    by_subject = []
    for p in progress_records:
        accuracy = (p.correct_answers / p.total_questions_answered * 100) if p.total_questions_answered > 0 else 0
        by_subject.append({
            'name': p.subject,
            'total': p.total_questions_answered,
            'correct': p.correct_answers,
            'accuracy': round(accuracy, 1),
            'quizzes_completed': p.quizzes_completed,
            'resources_viewed': p.resources_viewed
        })

    return jsonify({
        'quizzes_completed': total_quizzes,
        'total_questions_answered': total_answered,
        'correct_answers': total_correct,
        'average_score': round(avg_score, 1),
        'resources_viewed': total_resources,
        'doubts_resolved': resolved_doubts,
        'by_subject': by_subject,
        'recent_attempts': [{
            'attempt_id': a.id,
            'quiz_id': a.quiz_id,
            'quiz_title': a.quiz.title,
            'percentage': a.percentage,
            'submitted_at': a.submitted_at.isoformat() if a.submitted_at else None
        } for a in sorted(attempts, key=lambda x: x.submitted_at or x.started_at, reverse=True)[:5]]
    }), 200


def get_teacher_overview():
    """Get teacher dashboard overview"""
    open_doubts = Doubt.query.filter_by(status='open').count()
    resolved_doubts = Doubt.query.filter_by(status='resolved').count()
    total_students = User.query.filter_by(role='student').count()
    total_attempts = QuizAttempt.query.count()

    return jsonify({
        'open_doubts': open_doubts,
        'resolved_doubts': resolved_doubts,
        'total_students': total_students,
        'total_quiz_attempts': total_attempts
    }), 200


@progress_bp.route('/subject/<string:subject>', methods=['GET'])
@require_login
def subject_progress(subject):
    """Get student's progress for a specific subject"""
    if current_user.role != 'student':
        return jsonify({'error': 'Only students have subject progress'}), 403

    progress = StudentProgress.query.filter_by(
        student_id=current_user.id,
        subject=subject
    ).first()

    if not progress:
        return jsonify({
            'subject': subject,
            'total_questions_answered': 0,
            'correct_answers': 0,
            'accuracy': 0,
            'quizzes_completed': 0,
            'resources_viewed': 0
        }), 200

    accuracy = (progress.correct_answers / progress.total_questions_answered * 100) if progress.total_questions_answered > 0 else 0

    return jsonify({
        'subject': progress.subject,
        'grade_level': progress.grade_level,
        'total_questions_answered': progress.total_questions_answered,
        'correct_answers': progress.correct_answers,
        'accuracy': round(accuracy, 1),
        'quizzes_completed': progress.quizzes_completed,
        'resources_viewed': progress.resources_viewed,
        'last_activity': progress.last_activity.isoformat() if progress.last_activity else None
    }), 200


@progress_bp.route('/class/<int:grade_level>', methods=['GET'])
@require_login
def class_progress(grade_level):
    """Get class-level progress (teacher only)"""
    if current_user.role != 'teacher':
        return jsonify({'error': 'Teacher access required'}), 403

    students = User.query.filter_by(role='student', grade_level=grade_level).all()

    class_data = []
    for student in students:
        progress_records = StudentProgress.query.filter_by(student_id=student.id).all()
        total_answered = sum(p.total_questions_answered for p in progress_records)
        total_correct = sum(p.correct_answers for p in progress_records)
        accuracy = (total_correct / total_answered * 100) if total_answered > 0 else 0

        class_data.append({
            'student_id': student.id,
            'student_name': student.full_name,
            'email': student.email,
            'quizzes_completed': sum(p.quizzes_completed for p in progress_records),
            'accuracy': round(accuracy, 1),
            'resources_viewed': sum(p.resources_viewed for p in progress_records)
        })

    return jsonify({
        'grade_level': grade_level,
        'total_students': len(students),
        'students': class_data
    }), 200

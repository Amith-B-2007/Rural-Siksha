"""
Parent Dashboard routes
Allows parents to view child's progress, quiz attempts, doubts
"""

from flask import Blueprint, request, jsonify
from flask_login import current_user
from extensions import db
from backend.models import User, StudentProgress, QuizAttempt, Doubt, Quiz
from backend.utils import require_login

parent_bp = Blueprint('parent', __name__, url_prefix='/api/parent')


@parent_bp.route('/children', methods=['GET'])
@require_login
def list_children():
    """Get list of children linked to this parent"""
    if current_user.role != 'parent':
        return jsonify({'error': 'Parent access required'}), 403

    # For now, parents can search by student email
    # In production, you'd link via parent_id
    return jsonify({
        'message': 'Search children by email to view their progress',
        'parent': current_user.full_name
    }), 200


@parent_bp.route('/child/<string:email>/progress', methods=['GET'])
@require_login
def child_progress(email):
    """Get progress of a specific child by email"""
    if current_user.role != 'parent':
        return jsonify({'error': 'Parent access required'}), 403

    child = User.query.filter_by(email=email, role='student').first()
    if not child:
        return jsonify({'error': 'Student not found with this email'}), 404

    # Get progress records
    progress_records = StudentProgress.query.filter_by(student_id=child.id).all()

    total_quizzes = sum(p.quizzes_completed or 0 for p in progress_records)
    total_correct = sum(p.correct_answers or 0 for p in progress_records)
    total_answered = sum(p.total_questions_answered or 0 for p in progress_records)
    overall_accuracy = (total_correct / total_answered * 100) if total_answered > 0 else 0

    # Recent quiz attempts
    attempts = QuizAttempt.query.filter_by(student_id=child.id).order_by(QuizAttempt.started_at.desc()).limit(10).all()

    # Doubts
    open_doubts = Doubt.query.filter_by(student_id=child.id, status='open').count()
    resolved_doubts = Doubt.query.filter_by(student_id=child.id, status='resolved').count()

    return jsonify({
        'child': {
            'id': child.id,
            'name': child.full_name,
            'email': child.email,
            'grade': child.grade_level
        },
        'overall': {
            'quizzes_completed': total_quizzes,
            'total_questions': total_answered,
            'correct_answers': total_correct,
            'accuracy': round(overall_accuracy, 1),
            'open_doubts': open_doubts,
            'resolved_doubts': resolved_doubts
        },
        'by_subject': [{
            'subject': p.subject,
            'quizzes': p.quizzes_completed or 0,
            'questions': p.total_questions_answered or 0,
            'correct': p.correct_answers or 0,
            'accuracy': round((p.correct_answers or 0) / (p.total_questions_answered or 1) * 100, 1),
            'last_activity': p.last_activity.isoformat() if p.last_activity else None
        } for p in progress_records],
        'recent_attempts': [{
            'quiz_title': a.quiz.title if a.quiz else 'Unknown',
            'subject': a.quiz.subject if a.quiz else 'Unknown',
            'percentage': a.percentage,
            'status': a.status,
            'date': a.submitted_at.isoformat() if a.submitted_at else (a.started_at.isoformat() if a.started_at else None)
        } for a in attempts]
    }), 200


@parent_bp.route('/child/<string:email>/doubts', methods=['GET'])
@require_login
def child_doubts(email):
    """Get doubts of a specific child"""
    if current_user.role != 'parent':
        return jsonify({'error': 'Parent access required'}), 403

    child = User.query.filter_by(email=email, role='student').first()
    if not child:
        return jsonify({'error': 'Student not found'}), 404

    doubts = Doubt.query.filter_by(student_id=child.id).order_by(Doubt.created_at.desc()).all()

    return jsonify([{
        'id': d.id,
        'question': d.question_text,
        'subject': d.subject,
        'status': d.status,
        'created_at': d.created_at.isoformat(),
        'response_count': len(d.responses)
    } for d in doubts]), 200

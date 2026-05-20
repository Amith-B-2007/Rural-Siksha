"""
Doubt routes - student creates doubts, AI/teacher respond
"""

from datetime import datetime
from flask import Blueprint, request, jsonify
from flask_login import current_user
from extensions import db
from backend.models import Doubt, DoubtResponse
from backend.ollama_client import OllamaClient
from backend.utils import require_login

doubts_bp = Blueprint('doubts', __name__, url_prefix='/api/doubts')


@doubts_bp.route('', methods=['POST'])
@require_login
def create_doubt():
    """Create a new doubt and trigger AI response"""
    if current_user.role != 'student':
        return jsonify({'error': 'Only students can create doubts'}), 403

    data = request.get_json()
    if not data or 'question_text' not in data:
        return jsonify({'error': 'Missing question_text'}), 400

    question_text = data['question_text'].strip()
    subject = data.get('subject', '').strip()
    grade_level = data.get('grade_level') or current_user.grade_level

    if not question_text:
        return jsonify({'error': 'Question text cannot be empty'}), 400

    if not subject:
        return jsonify({'error': 'Subject is required'}), 400

    # Create doubt
    doubt = Doubt(
        student_id=current_user.id,
        subject=subject,
        grade_level=grade_level,
        question_text=question_text,
        question_detail=data.get('question_detail', ''),
        status='open'
    )
    db.session.add(doubt)
    db.session.commit()

    # Try to get AI response (don't fail if Ollama is down)
    # Ollama is local, so this should work even without internet
    ai_response_text = None
    ai_error = None
    try:
        ai_response_text, ai_error = OllamaClient.answer_doubt(
            question_text,
            subject=subject,
            grade_level=grade_level
        )

        if ai_response_text:
            ai_response = DoubtResponse(
                doubt_id=doubt.id,
                response_type='ai',
                response_text=ai_response_text
            )
            db.session.add(ai_response)
            db.session.commit()
            print(f"[AI] Generated response for doubt #{doubt.id}")
        else:
            print(f"[AI] No response. Error: {ai_error}")
    except Exception as e:
        ai_error = str(e)
        print(f"[AI] Exception: {e}")
        import traceback
        traceback.print_exc()

    return jsonify({
        'doubt_id': doubt.id,
        'question_text': doubt.question_text,
        'subject': doubt.subject,
        'status': doubt.status,
        'created_at': doubt.created_at.isoformat(),
        'ai_response': ai_response_text,
        'ai_error': ai_error if not ai_response_text else None
    }), 201


@doubts_bp.route('', methods=['GET'])
@require_login
def list_doubts():
    """List doubts (filtered by role and status)"""
    status_filter = request.args.get('status')

    if current_user.role == 'student':
        query = Doubt.query.filter_by(student_id=current_user.id)
    else:
        # Teachers see all doubts (filter by subject in Phase 3)
        query = Doubt.query

    if status_filter:
        query = query.filter_by(status=status_filter)

    doubts = query.order_by(Doubt.created_at.desc()).all()

    return jsonify([{
        'id': d.id,
        'question_text': d.question_text,
        'question_detail': d.question_detail,
        'subject': d.subject,
        'grade_level': d.grade_level,
        'status': d.status,
        'created_at': d.created_at.isoformat(),
        'response_count': len(d.responses),
        'student_name': d.student.full_name if current_user.role == 'teacher' else None
    } for d in doubts]), 200


@doubts_bp.route('/<int:doubt_id>', methods=['GET'])
@require_login
def get_doubt(doubt_id):
    """Get a specific doubt with all responses"""
    doubt = Doubt.query.get_or_404(doubt_id)

    # Authorization: student can only see own doubts, teachers see all
    if current_user.role == 'student' and doubt.student_id != current_user.id:
        return jsonify({'error': 'Access denied'}), 403

    responses = sorted(doubt.responses, key=lambda r: r.created_at)

    return jsonify({
        'id': doubt.id,
        'question_text': doubt.question_text,
        'question_detail': doubt.question_detail,
        'subject': doubt.subject,
        'grade_level': doubt.grade_level,
        'status': doubt.status,
        'created_at': doubt.created_at.isoformat(),
        'resolved_at': doubt.resolved_at.isoformat() if doubt.resolved_at else None,
        'student_name': doubt.student.full_name,
        'responses': [{
            'id': r.id,
            'response_type': r.response_type,
            'response_text': r.response_text,
            'responder_name': r.responder.full_name if r.responder else 'AI Tutor',
            'created_at': r.created_at.isoformat(),
            'is_helpful': r.is_helpful
        } for r in responses]
    }), 200


@doubts_bp.route('/<int:doubt_id>/respond', methods=['POST'])
@require_login
def respond_to_doubt(doubt_id):
    """Teacher responds to a doubt"""
    if current_user.role != 'teacher':
        return jsonify({'error': 'Only teachers can respond to doubts'}), 403

    data = request.get_json()
    if not data or 'response_text' not in data:
        return jsonify({'error': 'Missing response_text'}), 400

    doubt = Doubt.query.get_or_404(doubt_id)
    response_text = data['response_text'].strip()

    if not response_text:
        return jsonify({'error': 'Response text cannot be empty'}), 400

    response = DoubtResponse(
        doubt_id=doubt.id,
        response_type='teacher',
        responder_id=current_user.id,
        response_text=response_text
    )
    db.session.add(response)

    # Update doubt status
    doubt.status = 'resolved'
    doubt.resolved_at = datetime.utcnow()

    db.session.commit()

    return jsonify({
        'response_id': response.id,
        'created_at': response.created_at.isoformat(),
        'message': 'Response added successfully'
    }), 201


@doubts_bp.route('/<int:doubt_id>/helpful', methods=['POST'])
@require_login
def mark_helpful(doubt_id):
    """Mark a response as helpful or not"""
    data = request.get_json()
    if not data or 'response_id' not in data or 'is_helpful' not in data:
        return jsonify({'error': 'Missing response_id or is_helpful'}), 400

    response = DoubtResponse.query.get_or_404(data['response_id'])

    if response.doubt_id != doubt_id:
        return jsonify({'error': 'Response does not belong to this doubt'}), 400

    response.is_helpful = bool(data['is_helpful'])
    db.session.commit()

    return jsonify({'message': 'Feedback recorded', 'response_id': response.id}), 200


@doubts_bp.route('/ai-status', methods=['GET'])
def ai_status():
    """Check if Ollama AI is available"""
    available = OllamaClient.is_available()
    models = OllamaClient.list_models() if available else []

    return jsonify({
        'available': available,
        'model': OllamaClient.get_model(),
        'available_models': [m.get('name') for m in models]
    }), 200

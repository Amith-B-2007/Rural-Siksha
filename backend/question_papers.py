"""
Question Papers routes - browse and download previous year papers
"""

import os
from flask import Blueprint, request, jsonify, send_file
from flask_login import current_user
from werkzeug.utils import secure_filename
from uuid import uuid4
from extensions import db
from backend.models import QuestionPaper
from backend.utils import require_login

question_papers_bp = Blueprint('question_papers', __name__, url_prefix='/api/question-papers')


@question_papers_bp.route('', methods=['GET'])
@require_login
def list_papers():
    """List question papers filtered by grade, subject, year"""
    grade = request.args.get('grade', type=int)
    subject = request.args.get('subject', type=str)
    year = request.args.get('year', type=int)
    exam_type = request.args.get('exam_type', type=str)

    query = QuestionPaper.query.filter_by(is_published=True)

    if grade:
        query = query.filter_by(grade_level=grade)
    if subject:
        query = query.filter_by(subject=subject)
    if year:
        query = query.filter_by(year=year)
    if exam_type:
        query = query.filter_by(exam_type=exam_type)

    papers = query.order_by(QuestionPaper.year.desc(), QuestionPaper.subject).all()

    return jsonify([{
        'id': p.id,
        'title': p.title,
        'description': p.description,
        'subject': p.subject,
        'grade_level': p.grade_level,
        'year': p.year,
        'exam_type': p.exam_type,
        'duration_minutes': p.duration_minutes,
        'total_marks': p.total_marks,
        'file_size': p.file_size,
        'created_at': p.created_at.isoformat()
    } for p in papers]), 200


@question_papers_bp.route('/<int:paper_id>', methods=['GET'])
@require_login
def get_paper(paper_id):
    """Get details of a specific question paper"""
    paper = QuestionPaper.query.get_or_404(paper_id)

    if not paper.is_published:
        return jsonify({'error': 'Paper not available'}), 403

    return jsonify({
        'id': paper.id,
        'title': paper.title,
        'description': paper.description,
        'subject': paper.subject,
        'grade_level': paper.grade_level,
        'year': paper.year,
        'exam_type': paper.exam_type,
        'duration_minutes': paper.duration_minutes,
        'total_marks': paper.total_marks,
        'file_path': paper.file_path,
        'content_type': paper.content_type,
        'file_size': paper.file_size
    }), 200


@question_papers_bp.route('/<int:paper_id>/download', methods=['GET'])
@require_login
def download_paper(paper_id):
    """Download/view question paper file"""
    paper = QuestionPaper.query.get_or_404(paper_id)

    if not paper.file_path or not os.path.exists(paper.file_path):
        return jsonify({'error': 'File not found'}), 404

    as_attachment = request.args.get('download') == '1'
    mimetype = 'application/pdf' if paper.content_type == 'pdf' else None

    return send_file(
        paper.file_path,
        as_attachment=as_attachment,
        download_name=paper.title + '.' + (paper.content_type or 'txt'),
        mimetype=mimetype
    )


@question_papers_bp.route('/upload', methods=['POST'])
@require_login
def upload_paper():
    """Teacher uploads a new question paper"""
    if current_user.role != 'teacher':
        return jsonify({'error': 'Only teachers can upload papers'}), 403

    title = request.form.get('title', '').strip()
    subject = request.form.get('subject', '').strip()
    grade = request.form.get('grade_level', type=int)
    year = request.form.get('year', type=int)
    exam_type = request.form.get('exam_type', 'annual')
    duration = request.form.get('duration_minutes', type=int)
    total_marks = request.form.get('total_marks', type=int)
    description = request.form.get('description', '').strip()

    if not all([title, subject, grade, year]):
        return jsonify({'error': 'Missing required fields'}), 400

    file = request.files.get('file')
    if not file or not file.filename:
        return jsonify({'error': 'No file uploaded'}), 400

    os.makedirs('./data/question_papers', exist_ok=True)

    # Save file with unique name
    filename = secure_filename(file.filename)
    unique_filename = f"{uuid4().hex}_{filename}"
    file_path = f"data/question_papers/{unique_filename}"
    file.save(file_path)

    file_size = os.path.getsize(file_path)
    content_type = filename.rsplit('.', 1)[-1].lower() if '.' in filename else 'txt'

    paper = QuestionPaper(
        title=title,
        description=description,
        subject=subject,
        grade_level=grade,
        year=year,
        exam_type=exam_type,
        duration_minutes=duration,
        total_marks=total_marks,
        file_path=file_path,
        content_type=content_type,
        file_size=file_size,
        created_by=current_user.id,
        is_published=True
    )
    db.session.add(paper)
    db.session.commit()

    return jsonify({
        'message': 'Question paper uploaded successfully',
        'paper_id': paper.id
    }), 201


@question_papers_bp.route('/years', methods=['GET'])
@require_login
def list_years():
    """Get unique years available"""
    years = db.session.query(QuestionPaper.year).distinct().order_by(QuestionPaper.year.desc()).all()
    return jsonify([y[0] for y in years]), 200

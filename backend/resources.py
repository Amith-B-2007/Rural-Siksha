import os
import mimetypes
from flask import Blueprint, request, jsonify, send_file
from flask_login import current_user
from werkzeug.utils import secure_filename
from uuid import uuid4
from extensions import db
from backend.models import Resource, StudentProgress
from backend.utils import require_login, require_role

resources_bp = Blueprint('resources', __name__, url_prefix='/api/resources')

ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'jpeg', 'png', 'gif', 'txt', 'mp4', 'webm'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@resources_bp.route('', methods=['GET'])
@require_login
def list_resources():
    """List resources by grade and subject"""
    grade = request.args.get('grade', type=int)
    subject = request.args.get('subject', type=str)

    query = Resource.query.filter_by(is_published=True)

    if grade:
        query = query.filter_by(grade_level=grade)
    if subject:
        query = query.filter_by(subject=subject)

    resources = query.all()

    return jsonify([{
        'id': r.id,
        'title': r.title,
        'subject': r.subject,
        'grade_level': r.grade_level,
        'content_type': r.content_type,
        'description': r.description,
        'file_size': r.file_size,
        'youtube_url': r.youtube_url,
        'youtube_channel': r.youtube_channel,
        'ncert_url': r.ncert_url,
        'ncert_chapter': r.ncert_chapter,
        'created_at': r.created_at.isoformat()
    } for r in resources]), 200


@resources_bp.route('/<int:resource_id>', methods=['GET'])
@require_login
def get_resource(resource_id):
    """Get resource metadata"""
    resource = Resource.query.get_or_404(resource_id)

    if not resource.is_published and resource.created_by != current_user.id:
        return jsonify({'error': 'Resource not available'}), 403

    # Increment view count for students
    if current_user.role == 'student':
        progress = StudentProgress.query.filter_by(
            student_id=current_user.id,
            subject=resource.subject
        ).first()
        if not progress:
            progress = StudentProgress(
                student_id=current_user.id,
                subject=resource.subject,
                grade_level=current_user.grade_level
            )
            db.session.add(progress)
        progress.resources_viewed += 1
        progress.last_activity = db.func.now()
        db.session.commit()

    return jsonify({
        'id': resource.id,
        'title': resource.title,
        'description': resource.description,
        'subject': resource.subject,
        'grade_level': resource.grade_level,
        'content_type': resource.content_type,
        'file_size': resource.file_size,
        'created_by': resource.creator.full_name,
        'created_at': resource.created_at.isoformat(),
        'download_url': f'/api/resources/{resource_id}/download'
    }), 200


@resources_bp.route('/<int:resource_id>/download', methods=['GET'])
@require_login
def download_resource(resource_id):
    """Download resource file"""
    resource = Resource.query.get_or_404(resource_id)

    if not resource.is_published and resource.created_by != current_user.id:
        return jsonify({'error': 'Resource not available'}), 403

    file_path = os.path.join(os.getcwd(), resource.file_path)

    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404

    try:
        # Check if user wants to view inline (default for PDF) or download
        as_attachment = request.args.get('download') == '1'

        # Set proper MIME type for PDF
        mimetype = 'application/pdf' if resource.content_type == 'pdf' else None

        return send_file(
            file_path,
            as_attachment=as_attachment,
            download_name=resource.title + '.' + resource.content_type,
            mimetype=mimetype
        )
    except Exception as e:
        return jsonify({'error': f'Download failed: {str(e)}'}), 500


@resources_bp.route('/upload', methods=['POST'])
@require_login
def upload_resource():
    """Upload a new resource (teacher only)"""
    if current_user.role != 'teacher':
        return jsonify({'error': 'Only teachers can upload resources'}), 403

    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'}), 400

    # Get metadata
    title = request.form.get('title', '').strip()
    subject = request.form.get('subject', '').strip()
    grade_level = request.form.get('grade_level', type=int)
    description = request.form.get('description', '').strip()

    if not all([title, subject, grade_level]):
        return jsonify({'error': 'Missing title, subject, or grade_level'}), 400

    if not (1 <= grade_level <= 10):
        return jsonify({'error': 'Grade level must be 1-10'}), 400

    # Save file
    ext = file.filename.rsplit('.', 1)[1].lower()
    filename = f"{uuid4()}_{secure_filename(file.filename)}"
    file_path = os.path.join('data/resources', filename)
    os.makedirs('data/resources', exist_ok=True)

    try:
        file.save(file_path)
        file_size = os.path.getsize(file_path)

        # Create resource record
        resource = Resource(
            title=title,
            description=description,
            subject=subject,
            grade_level=grade_level,
            content_type=ext,
            file_path=file_path,
            file_size=file_size,
            created_by=current_user.id,
            is_published=False  # Requires admin approval (can be removed in Phase 1)
        )

        db.session.add(resource)
        db.session.commit()

        return jsonify({
            'message': 'Resource uploaded successfully',
            'resource_id': resource.id,
            'title': resource.title,
            'status': 'pending_review'
        }), 201

    except Exception as e:
        db.session.rollback()
        if os.path.exists(file_path):
            os.remove(file_path)
        return jsonify({'error': f'Upload failed: {str(e)}'}), 500


@resources_bp.route('/<int:resource_id>/publish', methods=['POST'])
def publish_resource(resource_id):
    """Publish resource (admin only) - TODO: add admin role"""
    resource = Resource.query.get_or_404(resource_id)
    resource.is_published = True
    db.session.commit()
    return jsonify({'message': 'Resource published', 'resource_id': resource.id}), 200

from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, current_user
from extensions import db
from backend.models import User
from backend.utils import validate_email, validate_password

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth_bp.route('/register', methods=['POST'])
def register():
    """Register a new student or teacher"""
    data = request.get_json()

    # Validation
    if not data or not all(k in data for k in ['email', 'password', 'full_name', 'role']):
        return jsonify({'error': 'Missing required fields'}), 400

    email = data.get('email', '').strip()
    password = data.get('password', '')
    full_name = data.get('full_name', '').strip()
    role = data.get('role', '').strip()

    # Validate inputs
    if not validate_email(email):
        return jsonify({'error': 'Invalid email format'}), 400
    if not validate_password(password):
        return jsonify({'error': 'Password must be at least 6 characters'}), 400
    if role not in ['student', 'teacher', 'parent']:
        return jsonify({'error': 'Role must be "student", "teacher", or "parent"'}), 400
    if not full_name:
        return jsonify({'error': 'Full name is required'}), 400

    # Check if user exists
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already registered'}), 409

    # Validate role-specific fields
    if role == 'student':
        grade_level = data.get('grade_level')
        if not grade_level or not (1 <= int(grade_level) <= 10):
            return jsonify({'error': 'Valid grade_level (1-10) required for students'}), 400
    elif role == 'teacher':
        subject = data.get('subject', '').strip()
        if not subject:
            return jsonify({'error': 'Subject is required for teachers'}), 400

    # Create user
    user = User(
        email=email,
        full_name=full_name,
        role=role,
        grade_level=data.get('grade_level') if role == 'student' else None,
        subject=data.get('subject') if role == 'teacher' else None
    )
    user.set_password(password)

    try:
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return jsonify({
            'message': 'Registration successful',
            'user_id': user.id,
            'email': user.email,
            'role': user.role
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Registration failed: {str(e)}'}), 500


@auth_bp.route('/login', methods=['POST'])
def login():
    """Login a user"""
    data = request.get_json()

    if not data or not all(k in data for k in ['email', 'password']):
        return jsonify({'error': 'Missing email or password'}), 400

    email = data.get('email', '').strip()
    password = data.get('password', '')

    user = User.query.filter_by(email=email).first()

    if not user or not user.check_password(password):
        return jsonify({'error': 'Invalid email or password'}), 401

    login_user(user)
    return jsonify({
        'message': 'Login successful',
        'user_id': user.id,
        'email': user.email,
        'full_name': user.full_name,
        'role': user.role,
        'grade_level': user.grade_level,
        'subject': user.subject
    }), 200


@auth_bp.route('/logout', methods=['POST'])
def logout():
    """Logout a user"""
    logout_user()
    return jsonify({'message': 'Logout successful'}), 200


@auth_bp.route('/me', methods=['GET'])
def get_current_user():
    """Get current user info"""
    if not current_user.is_authenticated:
        return jsonify({'error': 'Not authenticated'}), 401

    return jsonify({
        'user_id': current_user.id,
        'email': current_user.email,
        'full_name': current_user.full_name,
        'role': current_user.role,
        'grade_level': current_user.grade_level,
        'subject': current_user.subject
    }), 200

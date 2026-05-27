import os
from flask import Flask, jsonify, send_from_directory, request
from extensions import db, login_manager
from config import config


def create_app(config_name='development'):
    """Flask app factory"""
    # Serve static files from frontend folder
    app = Flask(__name__, static_folder='frontend', static_url_path='/static')

    # Load config
    app.config.from_object(config[config_name])

    # Create data directories if they don't exist
    os.makedirs(app.config['RESOURCE_FOLDER'], exist_ok=True)
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    from backend import auth_bp, resources_bp, health_bp, quizzes_bp, doubts_bp, progress_bp, question_papers_bp, parent_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(resources_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(quizzes_bp)
    app.register_blueprint(doubts_bp)
    app.register_blueprint(progress_bp)
    app.register_blueprint(question_papers_bp)
    app.register_blueprint(parent_bp)

    # Serve index.html for all non-API routes
    @app.route('/')
    def index():
        return send_from_directory('frontend', 'index.html')

    # Serve Service Worker
    @app.route('/sw.js')
    def service_worker():
        response = send_from_directory('frontend', 'sw.js')
        response.headers['Service-Worker-Allowed'] = '/'
        response.headers['Cache-Control'] = 'no-cache'
        return response

    # Serve PWA Manifest
    @app.route('/manifest.json')
    def manifest():
        return send_from_directory('frontend', 'manifest.json')

    @app.errorhandler(404)
    def not_found(error):
        # Serve index for SPA routing
        if not request.path.startswith('/api'):
            return send_from_directory('frontend', 'index.html')
        return jsonify({'error': 'Not found'}), 404

    # Create tables
    with app.app_context():
        # Import models so they're registered with SQLAlchemy
        from backend import models
        db.create_all()

        # Auto-seed demo data on cloud deploys (idempotent)
        if os.getenv('SEED_DEMO_DATA') == '1':
            try:
                User = models.User
                if User.query.count() == 0:
                    demos = [
                        ('Demo Student', 'student@example.com', 'student', 10, None),
                        ('Demo Teacher', 'teacher@example.com', 'teacher', None, 'Mathematics'),
                        ('Demo Parent',  'parent@example.com',  'parent',  None, None),
                    ]
                    for full_name, email, role, grade, subject in demos:
                        u = User(email=email, full_name=full_name, role=role,
                                 grade_level=grade, subject=subject)
                        u.set_password('password123')
                        db.session.add(u)
                    db.session.commit()
                    print('[seed] Demo accounts created.')
            except Exception as e:
                print(f'[seed] Skipped: {e}')

    return app


if __name__ == '__main__':
    app = create_app(os.getenv('FLASK_ENV', 'development'))
    # Listen on all interfaces (0.0.0.0) so mobile devices can access
    print("\n" + "=" * 60)
    print(" Rural Siksha - Starting Server")
    print("=" * 60)
    print(" Access on this computer: http://127.0.0.1:5000")
    print(" Access from mobile (same WiFi):")
    try:
        import socket
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print(f"   http://{local_ip}:5000")
    except:
        print("   http://YOUR_COMPUTER_IP:5000")
    print("=" * 60 + "\n")
    app.run(debug=False, host='0.0.0.0', port=5000, use_reloader=False)

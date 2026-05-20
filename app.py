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

    return app


if __name__ == '__main__':
    app = create_app(os.getenv('FLASK_ENV', 'development'))
    # Disable reloader to avoid context issues
    app.run(debug=False, host='127.0.0.1', port=5000, use_reloader=False)

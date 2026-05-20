from flask import Blueprint, jsonify
import requests
from config import config
from flask import current_app
from sqlalchemy import text

health_bp = Blueprint('health', __name__, url_prefix='/api')


@health_bp.route('/health', methods=['GET'])
def health_check():
    """Check system health: database and Ollama connectivity"""
    status = 'ok'
    details = {
        'database': False,
        'ollama': False
    }

    # Check database
    try:
        from extensions import db
        db.session.execute(text('SELECT 1'))
        details['database'] = True
    except Exception as e:
        details['database'] = False
        status = 'degraded'

    # Check Ollama
    try:
        ollama_url = current_app.config.get('OLLAMA_API_URL')
        response = requests.get(f'{ollama_url}/api/tags', timeout=5)
        details['ollama'] = response.status_code == 200
    except Exception as e:
        details['ollama'] = False
        status = 'degraded'

    return jsonify({
        'status': status,
        'details': details
    }), 200

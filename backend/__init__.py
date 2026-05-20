from .auth import auth_bp
from .resources import resources_bp
from .health import health_bp
from .quizzes import quizzes_bp
from .doubts import doubts_bp
from .progress import progress_bp
from .question_papers import question_papers_bp
from .parent import parent_bp

__all__ = ['auth_bp', 'resources_bp', 'health_bp', 'quizzes_bp', 'doubts_bp', 'progress_bp', 'question_papers_bp', 'parent_bp']

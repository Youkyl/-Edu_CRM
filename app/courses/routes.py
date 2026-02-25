# Exemples de blueprint courses à protéger avec @login_required

from flask import Blueprint
from app.auth.decorators import login_required

courses_bp = Blueprint('courses', __name__, url_prefix='/courses')

@courses_bp.route('/')
@login_required
def list_courses():
    return "Liste des cours (protégée)"

@courses_bp.route('/<int:course_id>')
@login_required
def view_course(course_id):
    return f"Détails cours {course_id} (protégé)"

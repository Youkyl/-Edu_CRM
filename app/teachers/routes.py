# Exemples de blueprint teachers à protéger avec @login_required

from flask import Blueprint
from app.auth.decorators import login_required

teachers_bp = Blueprint('teachers', __name__, url_prefix='/teachers')

@teachers_bp.route('/')
@login_required
def list_teachers():
    return "Liste des professors (protégée)"

@teachers_bp.route('/<int:teacher_id>')
@login_required
def view_teacher(teacher_id):
    return f"Détails professor {teacher_id} (protégé)"

# Exemples de blueprints students, teachers, courses à protéger avec @login_required

from flask import Blueprint, render_template
from app.auth.decorators import login_required

students_bp = Blueprint('students', __name__, url_prefix='/students')

@students_bp.route('/')
@login_required
def list_students():
    return "Liste des étudiants (protégée)"

@students_bp.route('/<int:student_id>')
@login_required
def view_student(student_id):
    return f"Détails étudiant {student_id} (protégé)"

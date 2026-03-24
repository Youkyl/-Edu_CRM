from flask import render_template, request
from . import students_bp
from ...services import student_service

@students_bp.route('/')
def list_students():
    students = student_service.list_students()
    return render_template('list.html', students=students)

@students_bp.route('/search')
def search():
    query = request.args.get('q', '')
    students = student_service.search_students(query)
    return render_template('students/_rows.html', students=students)

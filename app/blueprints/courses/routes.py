from flask import render_template, request, redirect, url_for, flash
from . import courses_bp
from ...services import course_service

@courses_bp.route('/')
def list_courses():
    courses = course_service.list_courses()
    return render_template('list.html', courses=courses)

@courses_bp.route('/search')
def search():
    query = request.args.get('q', '')
    courses = course_service.search_courses(query)
    return render_template('courses/_rows.html', courses=courses)

@courses_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        course_id = request.form.get('id')
        title = request.form.get('title')
        teacher_id = request.form.get('teacher_id')
        
        if not course_id or not title:
            flash("ID and Title are required!", "error")
            return redirect(url_for('courses.create'))
            
        success, message = course_service.add_course(course_id, title, teacher_id)
        if success:
            flash(message, "success")
            return redirect(url_for('courses.list_courses'))
        else:
            flash(message, "error")
            
    return render_template('create.html')

@courses_bp.route('/delete/<id>', methods=['POST'])
def delete(id):
    if course_service.delete_course(id):
        flash("Course deleted successfully.", "success")
    else:
        flash("Error: Course not found.", "error")
    return redirect(url_for('courses.list_courses'))

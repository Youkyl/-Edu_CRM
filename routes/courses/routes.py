from flask import render_template, request, redirect, session, url_for, flash
from . import courses_bp
from ...services import course_service
from ...services import student_service
from ...services import teacher_service

@courses_bp.route('/')
def list_courses():
    role = session.get("role")
    teacher_id = session.get("teacher_id")
    student_id = session.get("student_id")

    if role == "teacher":
        courses = course_service.list_courses(teacher_id=teacher_id)
    elif role == "student":
        courses = course_service.list_courses(student_id=student_id)
    else:
        courses = course_service.list_courses()

    all_students = student_service.list_students() if role == "admin" else []
    all_teachers = teacher_service.list_teachers() if role == "admin" else []

    return render_template(
        'courses/list.html',
        courses=courses,
        role=role,
        students=all_students,
        teachers=all_teachers,
    )

@courses_bp.route('/create', methods=['GET', 'POST'])
def create():
    if session.get("role") != "admin":
        return redirect(url_for('dashboard.index'))

    teachers = teacher_service.list_teachers()

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
            
    return render_template('courses/create.html', teachers=teachers)

@courses_bp.route('/delete/<id>', methods=['POST'])
def delete(id):
    if session.get("role") != "admin":
        return redirect(url_for('dashboard.index'))

    if course_service.delete_course(id):
        flash("Course deleted successfully.", "success")
    else:
        flash("Error: Course not found.", "error")
    return redirect(url_for('courses.list_courses'))


@courses_bp.route('/assign-student/<course_id>', methods=['POST'])
def assign_student(course_id):
    if session.get("role") != "admin":
        return redirect(url_for('dashboard.index'))

    student_id = request.form.get('student_id')
    success, message = course_service.assign_student_to_course(course_id, student_id)
    flash(message, 'success' if success else 'danger')
    return redirect(url_for('courses.list_courses'))


@courses_bp.route('/assign-teacher/<course_id>', methods=['POST'])
def assign_teacher(course_id):
    if session.get("role") != "admin":
        return redirect(url_for('dashboard.index'))

    teacher_id = request.form.get('teacher_id')
    success, message = course_service.assign_teacher_to_course(course_id, teacher_id)
    flash(message, 'success' if success else 'danger')
    return redirect(url_for('courses.list_courses'))
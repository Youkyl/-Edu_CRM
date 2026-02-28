from flask import Blueprint, render_template, session
from ...services.student_service import list_students
from ...services.teacher_service import list_teachers
from ...services.course_service import list_courses, get_students_for_teacher, get_teachers_for_student

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
def index():
    role = session.get("role")

    if role == "teacher":
        teacher_id = session.get("teacher_id")
        teacher_courses = list_courses(teacher_id=teacher_id)
        return render_template(
            'dashboard/index.html',
            nb_students=len(get_students_for_teacher(teacher_id)),
            nb_teachers=1,
            nb_courses=len(teacher_courses),
            role=role,
        )

    if role == "student":
        student_id = session.get("student_id")
        student_courses = list_courses(student_id=student_id)
        return render_template(
            'dashboard/index.html',
            nb_students=1,
            nb_teachers=len(get_teachers_for_student(student_id)),
            nb_courses=len(student_courses),
            role=role,
        )

    return render_template('dashboard/index.html',
        nb_students=len(list_students()),
        nb_teachers=len(list_teachers()),
        nb_courses=len(list_courses()),
        role=role,
    )
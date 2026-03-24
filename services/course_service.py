from ..data import courses, students, teachers

def list_courses(teacher_id=None, student_id=None):
    """Returns courses with teacher details, optionally filtered by teacher or student."""
    detailed_courses = []
    for course in courses:
        if teacher_id is not None and course.get('teacher_id') != teacher_id:
            continue
        if student_id is not None and student_id not in course.get('student_ids', []):
            continue

        teacher = next((t for t in teachers if t['id'] == course['teacher_id']), None)
        course_copy = course.copy()
        course_copy['teacher_name'] = teacher['name'] if teacher else "Unknown"
        detailed_courses.append(course_copy)
    return detailed_courses

def add_course(course_id, title, teacher_id):
    """Adds a new course to the in-memory list."""
    if any(c['id'] == course_id for c in courses):
        return False, "Course ID already exists."

    if teacher_id in (None, ""):
        teacher_id = None
    elif str(teacher_id).isdigit():
        teacher_id = int(teacher_id)
    else:
        return False, "Teacher ID must be numeric."
    
    new_course = {
        'id': course_id,
        'title': title,
        'teacher_id': teacher_id,
        'student_ids': []
    }
    courses.append(new_course)
    return True, "Course added successfully."

def delete_course(course_id):
    """Deletes a course by ID."""
    global courses
    initial_len = len(courses)
    courses[:] = [c for c in courses if str(c['id']) != str(course_id)]
    return len(courses) < initial_len


def assign_teacher_to_course(course_id, teacher_id):
    """Assigns a teacher to a course if both exist."""
    course = next((c for c in courses if str(c['id']) == str(course_id)), None)
    if not course:
        return False, "Course not found."

    if not str(teacher_id).isdigit():
        return False, "Teacher ID must be numeric."

    teacher_id = int(teacher_id)
    teacher = next((t for t in teachers if t['id'] == teacher_id), None)
    if not teacher:
        return False, "Teacher not found."

    course['teacher_id'] = teacher_id
    return True, "Teacher assigned successfully."

def assign_student_to_course(course_id, student_id):
    """Assigns a student to a course if both exist."""
    course = next((c for c in courses if str(c['id']) == str(course_id)), None)
    if not course:
        return False, "Course not found."

    if not str(student_id).isdigit():
        return False, "Student ID must be numeric."

    student_id = int(student_id)
    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        return False, "Student not found."
    
    if student_id not in course['student_ids']:
        course['student_ids'].append(student_id)
        return True, "Student assigned to course."
    
    return False, "Student already assigned to this course."


def get_students_for_teacher(teacher_id):
    """Returns unique students enrolled in courses taught by the teacher."""
    teacher_courses = list_courses(teacher_id=teacher_id)
    student_ids = set()
    for course in teacher_courses:
        student_ids.update(course.get('student_ids', []))
    return [s for s in students if s['id'] in student_ids]


def get_teachers_for_student(student_id):
    """Returns unique teachers teaching the student's enrolled courses."""
    student_courses = list_courses(student_id=student_id)
    teacher_ids = {c.get('teacher_id') for c in student_courses if c.get('teacher_id') is not None}
    return [t for t in teachers if t['id'] in teacher_ids]

def get_course_by_id(course_id):
    """Returns a specific course by ID."""
    return next((c for c in courses if str(c['id']) == str(course_id)), None)


def update_course(course_id, title=None, teacher_id=None):
    """
    Met à jour le titre et/ou l'enseignant d'un cours existant.
    Seuls les champs fournis (non None) sont modifiés.

    Retourne :
        (True,  cours)    → mise à jour réussie
        (False, message)  → cours introuvable ou teacher_id invalide
    """
    course = get_course_by_id(course_id)
    if not course:
        return False, "Cours introuvable."
    if title is not None and title.strip():
        course['title'] = title.strip()
    if teacher_id is not None:
        if teacher_id == "" or teacher_id is None:
            course['teacher_id'] = None
        elif str(teacher_id).isdigit():
            tid = int(teacher_id)
            teacher = next((t for t in teachers if t['id'] == tid), None)
            if not teacher:
                return False, "Enseignant introuvable."
            course['teacher_id'] = tid
        else:
            return False, "L'ID de l'enseignant doit être numérique."
    return True, course
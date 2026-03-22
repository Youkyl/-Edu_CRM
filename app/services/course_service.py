from ..data import courses, students, teachers

def list_courses():
    """Returns a list of all courses with teacher details."""
    detailed_courses = []
    for course in courses:
        teacher = next((t for t in teachers if t['id'] == course['teacher_id']), None)
        course_copy = course.copy()
        course_copy['teacher_name'] = teacher['name'] if teacher else "Unknown"
        detailed_courses.append(course_copy)
    return detailed_courses

def add_course(course_id, title, teacher_id):
    """Adds a new course to the in-memory list."""
    if any(c['id'] == course_id for c in courses):
        return False, "Course ID already exists."
        
    if any(c['title'].lower() == title.lower() for c in courses):
        return False, "Course title already exists."
    
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
    initial_len = len(courses)
    courses[:] = [c for c in courses if str(c['id']) != str(course_id)]
    return len(courses) < initial_len

def assign_student_to_course(course_id, student_id):
    """Assigns a student to a course if both exist."""
    course = next((c for c in courses if str(c['id']) == str(course_id)), None)
    if not course:
        return False, "Course not found."
    
    if student_id not in course['student_ids']:
        course['student_ids'].append(student_id)
        return True, "Student assigned to course."
    
    return False, "Student already assigned to this course."

def get_course_by_id(course_id):
    """Returns a specific course by ID."""
    return next((c for c in courses if str(c['id']) == str(course_id)), None)

def search_courses(query):
    query = query.lower()
    return [c for c in list_courses() if query in c['title'].lower() or query in c.get('teacher_name', '').lower()]

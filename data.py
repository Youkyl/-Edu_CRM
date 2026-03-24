# In-memory storage for the application
# These lists store dictionaries representing students, teachers, and courses.

students = [
	{"id": 1, "name": "Alice Dupont", "email": "alice@edu.com", 'password': '1234', "age": 20},
	{"id": 2, "name": "Bob Martin", "email": "bob@edu.com", 'password': '1234', "age": 22},
]

teachers = [
	{"id": 1, "name": "Prof Martin", "email": "prof.martin@edu.com", 'password': '1234', "speciality": "Mathématiques"},
	{"id": 2, "name": "Prof Leroy", "email": "prof.leroy@edu.com", 'password': '1234', "speciality": "Physique"},
]

courses = [
	{"id": "C001", "title": "Algorithmique", "teacher_id": 1, "student_ids": [1, 2]},
	{"id": "C002", "title": "Mécanique", "teacher_id": 2, "student_ids": [2]},
]
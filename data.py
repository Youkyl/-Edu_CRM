# In-memory storage for the application
# These lists store dictionaries representing students, teachers, and courses.

students = [
	{"id": 1, "name": "Alice Dupont", "email": "alice@edu.com", "age": 20, "password": "alice123"},
	{"id": 2, "name": "Bob Martin", "email": "bob@edu.com", "age": 22, "password": "bob123"},
	{"id": 3, "name": "Chloe Bernard", "email": "chloe@edu.com", "age": 19, "password": "chloe123"},
	{"id": 4, "name": "David Moreau", "email": "david@edu.com", "age": 23, "password": "david123"},
	{"id": 5, "name": "Emma Laurent", "email": "emma@edu.com", "age": 21, "password": "emma123"},
	{"id": 6, "name": "Farid Karim", "email": "farid@edu.com", "age": 24, "password": "farid123"},
	{"id": 7, "name": "Gina Robert", "email": "gina@edu.com", "age": 20, "password": "gina123"},
	{"id": 8, "name": "Hugo Petit", "email": "hugo@edu.com", "age": 22, "password": "hugo123"},
	{"id": 9, "name": "Ines Diallo", "email": "ines@edu.com", "age": 19, "password": "ines123"},
	{"id": 10, "name": "Jules Simon", "email": "jules@edu.com", "age": 21, "password": "jules123"},
]

teachers = [
	{"id": 1, "name": "Prof Martin", "email": "prof.martin@edu.com", 'password': '1234', "speciality": "Mathématiques"},
	{"id": 2, "name": "Prof Leroy", "email": "prof.leroy@edu.com", 'password': '1234', "speciality": "Physique"},
	{"id": 3, "name": "Prof Haddad", "email": "prof.haddad@edu.com", 'password': '1234', "speciality": "Informatique"},
	{"id": 4, "name": "Prof Nguyen", "email": "prof.nguyen@edu.com", 'password': '1234', "speciality": "Réseaux"},
	{"id": 5, "name": "Prof Garcia", "email": "prof.garcia@edu.com", 'password': '1234', "speciality": "Statistiques"},
]

courses = [
	{"id": "C001", "title": "Algorithmique", "teacher_id": 3, "student_ids": [1, 2, 3, 7]},
	{"id": "C002", "title": "Mécanique", "teacher_id": 2, "student_ids": [2, 4, 8]},
	{"id": "C003", "title": "Analyse Mathématique", "teacher_id": 1, "student_ids": [1, 5, 9]},
	{"id": "C004", "title": "Programmation Web", "teacher_id": 3, "student_ids": [3, 5, 6, 10]},
	{"id": "C005", "title": "Réseaux", "teacher_id": 4, "student_ids": [4, 6, 8, 10]},
	{"id": "C006", "title": "Base de Données", "teacher_id": 3, "student_ids": [1, 2, 6, 9]},
	{"id": "C007", "title": "Probabilités", "teacher_id": 5, "student_ids": [5, 7, 9]},
	{"id": "C008", "title": "Cybersécurité", "teacher_id": 4, "student_ids": [3, 4, 8, 10]},
]
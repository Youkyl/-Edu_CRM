from ..data import students

def list_students():
    return students

def search_students(query):
    query = query.lower()
    return [s for s in students if query in s.get('name', '').lower() or query in s.get('email', '').lower()]

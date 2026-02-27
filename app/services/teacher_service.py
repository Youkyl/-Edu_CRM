
teachers: list[dict] = [
    {"id": 1, "name": "Alice Dupont", "email": "alice.dupont@example.com", "speciality": "Mathématiques"},
    {"id": 2, "name": "Bob Martin", "email": "bob.martin@example.com", "speciality": "Physique"},
    {"id": 3, "name": "Charlie Durand", "email": "charlie.durand@example.com", "speciality": "Histoire"},
    {"id": 4, "name": "Diane Leroy", "email": "diane.leroy@example.com", "speciality": "Français"}
]
_next_id = len(teachers) + 1

#il faut vérifier que les champs ne sont pas vides et que l'email est valide et que l'email' n'est pas déjà utilisé
def add_teacher(name: str, email: str, speciality: str) -> dict:
   
    global _next_id
    if not name or not email or not speciality:
        raise ValueError("Tous les champs sont requis.")
    if "@" not in email or "." not in email:
        raise ValueError("Email invalide.")
    if any(t["email"] == email for t in teachers):
        raise ValueError("Email déjà utilisé.")
    teacher = {
        "id": _next_id,
        "name": name,
        "email": email,
        "speciality": speciality,
    }


    teachers.append(teacher)
    _next_id += 1
    return teacher

def list_teachers() -> list[dict]:
    return list(teachers)  


def get_teacher_by_id(teacher_id: int) -> dict | None:
    return next((t for t in teachers if t["id"] == teacher_id), None)


def delete_teacher(teacher_id: int) -> bool:
    teacher = get_teacher_by_id(teacher_id)
    if teacher:
        teachers.remove(teacher)
        return True
    return False


def update_teacher(teacher_id: int, name: str | None = None,
                   email: str | None = None, speciality: str | None = None) -> dict | None:
    teacher = get_teacher_by_id(teacher_id)
    if not teacher:
        return None
    if name is not None:
        teacher["name"] = name
    if email is not None:
        teacher["email"] = email
    if speciality is not None:
        teacher["speciality"] = speciality
    return teacher
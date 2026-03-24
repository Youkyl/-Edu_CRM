# app/services/student_service.py
# ================================================
# SERVICE LAYER — Toute la logique métier ici
# Ce fichier ne connaît PAS Flask
# Il manipule uniquement les données
# ================================================

from ..data import courses, students

# Compteur pour générer les IDs automatiquement (comme AUTO_INCREMENT en SQL)
_next_id = max([s["id"] for s in students], default=0) + 1

import re

def is_valid_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

def list_students():
    """
    Retourne la liste de tous les étudiants.
    On retourne une copie pour éviter les modifications accidentelles.
    """
    return list(students)


def get_student_by_id(student_id):
    """
    Cherche et retourne un étudiant par son ID.

    - On parcourt la liste avec next()
    - Si aucun étudiant trouvé, on retourne None

    Exemple :
        get_student_by_id(1) → {"id": 1, "name": "Alice", ...}
        get_student_by_id(99) → None
    """
    return next((s for s in students if s["id"] == student_id), None)


def add_student(name, email, age):
    """
    Crée un nouvel étudiant et l'ajoute à la liste.
    """
    global _next_id
    
    # --- VALIDATION ---
    if not name or not email or not age:
        raise ValueError("Tous les champs sont obligatoires")
    
    if not isinstance(age, (int, str)) or (isinstance(age, str) and not age.strip()):
        raise ValueError("L'âge doit être un nombre valide")
    
    try:
        age = int(age)
        if age < 0 or age > 120:
            raise ValueError("L'âge doit être entre 0 et 120")
    except ValueError:
        raise ValueError("L'âge doit être un nombre entier valide")
    
    # Validation email simple
    # if "@" not in email or "." not in email:
    #     raise ValueError("Email invalide")
    
    # verification rebuste
    if not is_valid_email(email):
        raise ValueError("Email invalide")
    
    # Vérifier doublon

    # Créer
    new_student = {
        "id":    _next_id,
        "name":  name.strip(),
        "email": email.strip(),
        "age":   age,
    }
    
    students.append(new_student)
    _next_id += 1

    return new_student


def delete_student(student_id):
    """
    Supprime l'étudiant qui a cet ID.

    Retourne :
        True  → étudiant trouvé et supprimé
        False → étudiant introuvable

    Astuce : on recrée la liste SANS l'étudiant ciblé
    C'est plus simple et plus sûr que de modifier la liste en boucle
    """
    taille_avant = len(students)

    # On garde tout le monde SAUF l'étudiant avec cet ID
    students[:] = [s for s in students if s["id"] != student_id]

    for course in courses:
        if student_id in course["student_ids"]:
            course["student_ids"].remove(student_id)

    taille_apres = len(students)

    # Si la taille a diminué, c'est qu'on a supprimé quelqu'un
    return taille_apres < taille_avant
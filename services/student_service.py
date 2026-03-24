# app/services/student_service.py
# ================================================
# SERVICE LAYER — Toute la logique métier ici
# Ce fichier ne connaît PAS Flask
# Il manipule uniquement les données
# ================================================

from ..data import courses, students

# Compteur pour générer les IDs automatiquement (comme AUTO_INCREMENT en SQL)
_next_id = max([s["id"] for s in students], default=0) + 1


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


def add_student(name, email, age, password):
    """
    Crée un nouvel étudiant et l'ajoute à la liste.

    Paramètres :
        name  (str) : Nom complet
        email (str) : Adresse email
        age   (int) : Âge

    Retourne le dictionnaire du nouvel étudiant créé.
    """
    global _next_id  # On modifie la variable globale

    new_student = {
        "id":    _next_id,
        "name":  name,
        "email": email,
        "age":   int(age),  # On force la conversion en entier
        "password": password,
    }

    students.append(new_student)
    _next_id += 1  # On prépare l'ID pour le prochain étudiant

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
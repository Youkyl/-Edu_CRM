# app/students/route.py
# ================================================
# BLUEPRINT STUDENTS
# Gère toutes les routes liées aux étudiants
# ================================================

from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services import student_service

# ------------------------------------------------
# Création du Blueprint
#
# "students"        → nom du blueprint, utilisé dans url_for("students.xxx")
# __name__          → dit à Flask où trouver les templates
# url_prefix        → toutes les routes commencent par /students
# ------------------------------------------------
students_bp = Blueprint("students", __name__, url_prefix="/students")


# ------------------------------------------------
# ROUTE 1 : /students/
# Affiche la liste de tous les étudiants
# ------------------------------------------------
@students_bp.route("/")
def list_students():
    # On demande au service la liste complète
    all_students = student_service.list_students()

    # On envoie les données au template HTML
    return render_template("students/list.html", students=all_students)


# ------------------------------------------------
# ROUTE 2 : /students/create
#
# GET  → affiche le formulaire vide
# POST → reçoit les données et crée l'étudiant
# ------------------------------------------------
@students_bp.route("/create", methods=["GET", "POST"])
def create_student():
    if request.method == "POST":
        # On récupère les données envoyées par le formulaire HTML
        name  = request.form.get("name",  "").strip()
        email = request.form.get("email", "").strip()
        age   = request.form.get("age",   "").strip()

        # --- Validation ---
        if not name or not email or not age:
            flash("Tous les champs sont obligatoires.", "danger")
            return render_template("students/create.html")

        if not age.isdigit():
            flash("L'âge doit être un nombre entier.", "danger")
            return render_template("students/create.html")

        # --- On appelle le service pour créer l'étudiant ---
        student_service.add_student(name, email, age)

        # flash() envoie un message qui survive à la redirection
        flash(f"Étudiant '{name}' ajouté avec succès !", "success")

        # Toujours rediriger après un POST (pattern PRG)
        # Format url_for : "nom_blueprint.nom_fonction"
        return redirect(url_for("students.list_students"))

    # GET : on affiche juste le formulaire vide
    return render_template("students/create.html")


# ------------------------------------------------
# ROUTE 3 : /students/delete/<id>
#
# POST uniquement — jamais GET pour une suppression !
# <int:student_id> → Flask convertit l'URL en entier automatiquement
# ------------------------------------------------
@students_bp.route("/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    # On vérifie que l'étudiant existe avant de supprimer
    student = student_service.get_student_by_id(student_id)

    if student is None:
        flash(f"Étudiant introuvable (ID: {student_id}).", "warning")
    else:
        student_service.delete_student(student_id)
        flash(f"Étudiant '{student['name']}' supprimé.", "success")

    return redirect(url_for("students.list_students"))
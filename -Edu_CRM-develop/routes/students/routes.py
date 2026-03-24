# app/students/route.py
# ================================================
# BLUEPRINT STUDENTS
# Gère toutes les routes liées aux étudiants
# ================================================

from flask import render_template, request, redirect, session, url_for, flash
from . import students_bp
from ..auth.decorators import login_required
from ...services import student_service
from ...services import teacher_service
from ...services import course_service

# ------------------------------------------------
# ROUTE 1 : /students/
# Affiche la liste de tous les étudiants
# ------------------------------------------------
@students_bp.route("/")
@login_required
def list_students():
    role = session.get("role")

    if role == "teacher":
        teacher_id = session.get("teacher_id")
        all_students = course_service.get_students_for_teacher(teacher_id)
    else:
        all_students = student_service.list_students()

    # On envoie les données au template HTML
    return render_template("students/list.html", students=all_students, role=role)


# ------------------------------------------------
# ROUTE 2 : /students/create
#
# GET  → affiche le formulaire vide
# POST → reçoit les données et crée l'étudiant
# ------------------------------------------------
@students_bp.route("/create", methods=["GET", "POST"])
@login_required
def create_student():
    if session.get("role") != "admin":
        return redirect(url_for("dashboard.index"))

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
@login_required
def delete_student(student_id):
    if session.get("role") != "admin":
        return redirect(url_for("dashboard.index"))

    # On vérifie que l'étudiant existe avant de supprimer
    student = student_service.get_student_by_id(student_id)

    if student is None:
        flash(f"Étudiant introuvable (ID: {student_id}).", "warning")
    else:
        student_service.delete_student(student_id)
        flash(f"Étudiant '{student['name']}' supprimé.", "success")

    return redirect(url_for("students.list_students"))

# ------------------------------------------------
# ROUTE 4 : /students/<id>
#
# GET  → affiche les informations de l'étudiant
# <int:student_id> → Flask convertit l'URL en entier automatiquement
# ------------------------------------------------
@students_bp.route("/<int:student_id>", methods = ["GET"])
@login_required
def personal_infos(student_id):
    
    role = session.get("role")
    
    if role == "student" and session.get("student_id") != student_id :
        
        return redirect(url_for("dashboard.index"))
        
    # On vérifie que l'étudiant existe 
    student = student_service.get_student_by_id(student_id)
    
    if student is None:
        flash(f"Étudiant introuvable (ID: {student_id}).", "warning")
        
        return redirect(url_for("students.list_students"))
    
    list_courses = course_service.list_courses(student_id=student_id)
    list_teachers = course_service.get_teachers_for_student(student_id=student_id)
    
    return render_template("students/info.html",student=student, list_courses=list_courses, list_teachers=list_teachers)
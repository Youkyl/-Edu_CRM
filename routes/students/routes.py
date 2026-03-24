# app/students/route.py
# ================================================
# BLUEPRINT STUDENTS
# Gère toutes les routes liées aux étudiants
# ================================================


from flask import render_template, request, redirect, session, url_for, flash,make_response
import csv
import io
from . import students_bp
from ..auth.decorators import login_required
from ...services import student_service
from ...services import teacher_service
from ...services import course_service
from ...data import students



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

        for student in students:
            if student["email"] == email:
                flash(f"L'étudiant avec l'email {email} existe déjà.", "danger")
                return render_template("students/create.html")

        # --- On appelle le service pour créer l'étudiant ---
        try:
            student_service.add_student(name, email, age)
        except ValueError as e:
            flash(str(e), "danger")
            return render_template("students/create.html")

        flash(f"Étudiant '{name}' ajouté avec succès !", "success")
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


@students_bp.route("/export")
@login_required
def export_students():
    if session.get("role") != "admin":
        return redirect(url_for("dashboard.index"))

    all_students = student_service.list_students()

    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=["id", "name", "email", "age"])
    writer.writeheader()
    for student in all_students:
        writer.writerow({
            "id":    student["id"],
            "name":  student["name"],
            "email": student["email"],
            "age":   student["age"],
        })

    response = make_response(output.getvalue())
    response.headers["Content-Type"] = "text/csv; charset=utf-8"
    response.headers["Content-Disposition"] = "attachment; filename=students.csv"
    return response


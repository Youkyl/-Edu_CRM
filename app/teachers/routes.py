from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services import teacher_service

teachers_bp = Blueprint("teachers", __name__, url_prefix="/teachers")

@teachers_bp.route("/")
def list_teachers():
    all_teachers = teacher_service.list_teachers()
    return render_template("teachers/list.html", teachers=all_teachers)

@teachers_bp.route("/create", methods=["GET", "POST"])
def create_teacher():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        speciality = request.form.get("speciality", "").strip()
        if not name or not email or not speciality:
            flash("Tous les champs sont requis.", "danger")
            return redirect(url_for("teachers.create_teacher"))
        try:
            teacher = teacher_service.add_teacher(name, email, speciality)
            flash(f"Enseignant {teacher['name']} ajouté avec succès.", "success")
        except ValueError as ve:
            flash(str(ve), "danger")
            return redirect(url_for("teachers.create_teacher"))
        return redirect(url_for("teachers.list_teachers"))
    return render_template("teachers/create.html")

@teachers_bp.route("/delete/<int:teacher_id>")
def delete_teacher(teacher_id):
    success = teacher_service.delete_teacher(teacher_id)
    if success:
        flash("Enseignant supprimé.", "warning")
    else:
        flash("Aucun enseignant trouvé pour cet ID.", "danger")
    return redirect(url_for("teachers.list_teachers"))
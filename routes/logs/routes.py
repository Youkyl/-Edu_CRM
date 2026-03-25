from flask import render_template, redirect, url_for, session, flash
from . import logs_bp
from ...services import log_service

@logs_bp.route("/")
def index():
    if session.get("role") != "admin":
        flash("Accès réservé à l'administrateur.", "danger")
        return redirect(url_for("dashboard.index"))
    
    all_logs = log_service.get_logs()
    return render_template("logs/index.html", logs=all_logs)

@logs_bp.route("/clear")
def clear():
    if session.get("role") != "admin":
        flash("Accès réservé à l'administrateur.", "danger")
        return redirect(url_for("dashboard.index"))
    
    log_service.clear_logs()
    flash("Journal effacé.", "warning")
    return redirect(url_for("logs.index"))
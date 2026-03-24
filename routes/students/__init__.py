# Package routes.students
from flask import Blueprint

# ------------------------------------------------
# Création du Blueprint
#
# "students"        → nom du blueprint, utilisé dans url_for("students.xxx")
# __name__          → dit à Flask où trouver les templates
# url_prefix        → toutes les routes commencent par /students
# ------------------------------------------------
students_bp = Blueprint("students", __name__, url_prefix="/students")

from . import routes
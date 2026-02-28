# app/__init__.py
# ================================================
# Application Factory
# C'est ici que Flask est créé et configuré
# ================================================

from flask import Flask
from config import config


def create_app():
    # Création de l'instance Flask
    # __name__ dit à Flask où chercher les templates et fichiers statiques
    app = Flask(__name__)

    # Chargement de la configuration (SECRET_KEY, DEBUG, etc.)
    app.config.from_object(config["default"])

    # -----------------------------------------------
    # Enregistrement des Blueprints
    # Chaque module s'enregistre ici
    # -----------------------------------------------
    from app.students.route import students_bp
    app.register_blueprint(students_bp)

    # Plus tard l'équipe ajoutera :
    # from app.auth.route import auth_bp
    # app.register_blueprint(auth_bp)
    # etc.

    return app
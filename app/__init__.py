from flask import Flask, redirect, url_for


def create_app():
    app = Flask(__name__)
    app.secret_key = "secret"

    from app.teachers.routes import teachers_bp
    app.register_blueprint(teachers_bp)

    @app.route("/")
    def index():
        # redirige vers la liste des enseignants
        return redirect(url_for("teachers.list_teachers"))

    return app
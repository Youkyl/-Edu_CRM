from flask import Flask, redirect, request, session, url_for

from .routes.auth import auth_bp
from .routes.courses import courses_bp
from .routes.dashboard.route import dashboard_bp
from .routes.students.routes import students_bp
from .routes.teachers.routes import teachers_bp


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev-secret-key"

    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
    app.register_blueprint(students_bp)
    app.register_blueprint(teachers_bp)
    app.register_blueprint(courses_bp)
    app.register_blueprint(auth_bp)

    @app.before_request
    def require_login():
        if request.endpoint is None:
            return None

        if request.endpoint.startswith("static"):
            return None

        if request.endpoint.startswith("auth."):
            if request.endpoint == "auth.login" and session.get("user_id"):
                return redirect(url_for("dashboard.index"))
            return None

        if not session.get("user_id"):
            return redirect(url_for("auth.login"))

        role = session.get("role")

        if role == "admin":
            return None

        if role == "teacher":
            forbidden_prefixes = ("teachers.",)
            forbidden_endpoints = {
                "students.create_student",
                "students.delete_student",
                "courses.create",
                "courses.delete",
                "courses.assign_student",
                "courses.assign_teacher",
            }

            if request.endpoint.startswith(forbidden_prefixes) or request.endpoint in forbidden_endpoints:
                return redirect(url_for("dashboard.index"))

            return None

        if role == "student":
            forbidden_prefixes = ("teachers.", "students.")
            forbidden_endpoints = {
                "courses.create",
                "courses.delete",
                "courses.assign_student",
                "courses.assign_teacher",
            }

            if request.endpoint.startswith(forbidden_prefixes) or request.endpoint in forbidden_endpoints:
                return redirect(url_for("dashboard.index"))

            return None

        return None

    @app.route("/")
    def home():
        if not session.get("user_id"):
            return redirect(url_for("auth.login"))
        return redirect(url_for("dashboard.index"))

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
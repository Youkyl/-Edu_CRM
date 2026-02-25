from flask import Flask
from flask_session import Session

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = 'your-secret-key-change-this'
    app.config['SESSION_TYPE'] = 'filesystem'
    
    # Initialiser la session
    Session(app)
    
    # Enregistrer les blueprints
    from app.auth.routes import auth_bp
    from app.students.routes import students_bp
    from app.teachers.routes import teachers_bp
    from app.courses.routes import courses_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(students_bp)
    app.register_blueprint(teachers_bp)
    app.register_blueprint(courses_bp)
    
    return app

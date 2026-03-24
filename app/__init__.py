from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev_key_for_edu_crm'

    # Registration of Blueprints
    from .blueprints.courses import courses_bp
    # Temporary: set to '/' for easier testing instead of '/courses'
    app.register_blueprint(courses_bp, url_prefix='/')

    # Placeholder for other blueprints (to be integrated by others)
    # from .blueprints.auth import auth_bp
    # app.register_blueprint(auth_bp, url_prefix='/auth')
    
    from .blueprints.students import students_bp
    app.register_blueprint(students_bp, url_prefix='/students')

    # from .blueprints.teachers import teachers_bp
    # app.register_blueprint(teachers_bp, url_prefix='/teachers')

    # from .blueprints.dashboard import dashboard_bp
    # app.register_blueprint(dashboard_bp)

    return app

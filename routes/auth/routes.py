from flask import render_template, request, session, redirect, url_for, flash
from ...data import students, teachers
from . import auth_bp

# Base de données d'exemple
USERS = {
    'prof': {'password': '1234', 'role': 'teacher'},
    'admin': {'password': '1234', 'role': 'admin'},
}


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Route de connexion.
    GET: affiche le formulaire
    POST: traite la soumission
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Rechercher un utilisateur dans les listes étudiants/professeurs via email
        student_match = next((s for s in students if s.get('email') == username), None)
        teacher_match = next((t for t in teachers if t.get('email') == username), None)
        
        # Valider les identifiants
        if (
            (username in USERS and USERS[username]['password'] == password)
            or (student_match and student_match.get('password') == password)
            or (teacher_match and teacher_match.get('password') == password)
        ):
            # Créer la session
            session["user_id"] = username
            session.pop("student_id", None)
            session.pop("teacher_id", None)

            if username in USERS:
                session["role"] = USERS[username]["role"]
            elif student_match:
                session["role"] = "student"
                session["student_id"] = student_match["id"]
            elif teacher_match:
                session["role"] = "teacher"
                session["teacher_id"] = teacher_match["id"]
                
            flash(f'Bienvenue {username}!', 'success')
            return redirect(url_for('dashboard.index'))
        else:
            flash('Identifiants invalides. Essayez avec admin/1234 pour vous connecter en tant qu\'admin', 'danger')
    
    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    """
    Route de déconnexion.
    Vide la session et redirige vers login.
    """
    username = session.get('user_id')
    session.clear()
    flash(f'Au revoir {username}! Vous avez été déconnecté.', 'info')
    return redirect(url_for('auth.login'))

# @auth_bp.route('/dashboard')
# def dashboard():
#     """
#     Tableau de bord utilisateur (exemple protégé).
#     """
#     if 'user_id' not in session:
#         flash('Veuillez vous connecter.', 'warning')
#         return redirect(url_for('auth.login'))
    
#     return render_template('auth/dashboard.html', user=session.get('user_id'), role=session.get('role'))

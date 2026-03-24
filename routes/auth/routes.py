from flask import render_template, request, session, redirect, url_for, flash
from . import auth_bp
from ...data import students

# Base de données d'exemple
USERS = {
    'prof': {'password': '1234', 'role': 'teacher', 'teacher_id': 1},
    'admin': {'password': '1234', 'role': 'admin'}
}


def find_student_by_name(name):
    normalized_name = name.strip().lower()
    return next((s for s in students if s['name'].strip().lower() == normalized_name), None)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Route de connexion.
    GET: affiche le formulaire
    POST: traite la soumission
    """
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        # Comptes fixes admin/prof
        if username in USERS and USERS[username]['password'] == password:
            user = USERS[username]
            session['user_id'] = username
            session['role'] = user['role']
            session['student_id'] = user.get('student_id')
            session['teacher_id'] = user.get('teacher_id')
            flash(f'Bienvenue {username}!', 'success')

            if user['role'] == 'admin':
                return redirect(url_for('dashboard.index'))

            if user['role'] == 'teacher':
                return redirect(url_for('courses.list_courses'))

            return redirect(url_for('courses.list_courses'))

        # Compte étudiant basé sur son nom + mot de passe personnel
        student = find_student_by_name(username)
        if student and student.get('password') == password:
            session['user_id'] = student['name']
            session['role'] = 'student'
            session['student_id'] = student['id']
            session['teacher_id'] = None
            flash(f"Bienvenue {student['name']}!", 'success')
            return redirect(url_for('courses.list_courses'))
        
        flash('Identifiants invalides. Utilisez admin/1234, prof/1234, ou nom étudiant + son mot de passe.', 'danger')
    
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

@auth_bp.route('/dashboard')
def dashboard():
    """
    Route legacy conservée pour compatibilité.
    Redirige vers le dashboard principal qui adapte l'affichage au rôle.
    """
    if 'user_id' not in session:
        flash('Veuillez vous connecter.', 'warning')
        return redirect(url_for('auth.login'))

    return redirect(url_for('dashboard.index'))
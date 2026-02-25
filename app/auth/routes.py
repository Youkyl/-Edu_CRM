from flask import render_template, request, session, redirect, url_for, flash
from app.auth import auth_bp

# Base de données d'exemple
USERS = {
    'etudiant': {'password': '1234', 'role': 'student'},
    'prof': {'password': '1234', 'role': 'teacher'},
    'admin': {'password': '1234', 'role': 'admin'}
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
        
        # Valider les identifiants
        if username in USERS and USERS[username]['password'] == password:
            # Créer la session
            session['user_id'] = username
            session['role'] = USERS[username]['role']
            flash(f'Bienvenue {username}!', 'success')
            return redirect(url_for('auth.dashboard'))
        else:
            flash('Identifiants invalides. Essayez avec etudiant/1234, prof/1234 ou admin/1234', 'danger')
    
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
    Tableau de bord utilisateur (exemple protégé).
    """
    if 'user_id' not in session:
        flash('Veuillez vous connecter.', 'warning')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/dashboard.html', user=session.get('user_id'), role=session.get('role'))

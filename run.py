# run.py
# ================================================
# Point d'entrée de l'application
# Lance le serveur Flask en mode développement
# ================================================

from app import create_app

app = create_app()

if __name__ == "__main__":
    # debug=True : rechargement automatique quand tu modifies le code
    # port=5000  : accessible sur http://localhost:5000
    app.run(debug=True, port=5000)
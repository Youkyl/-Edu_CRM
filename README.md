# Edu CRM

Simple application Flask pour gérer une liste d'enseignants en mémoire.

## Structure

- `app/` : code source de l'application
  - `services/` : logique métier (gestion des enseignants)
  - `teachers/` : blueprint Flask pour les routes liées aux enseignants
  - `templates/` : vues Jinja2

## Lancer l'application

```powershell
# activer l'environnement virtuel
venv\Scripts\activate

# installer les dépendances si nécessaire
pip install flask

# exécuter
python -m app.run
```

L'application sera accessible sur `http://127.0.0.1:5000/`.

## Améliorations possibles

- Persistance en base de données
- Édition des enseignants
- Validation avancée des adresses e-mail

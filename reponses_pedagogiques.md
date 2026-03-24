# Réponses aux Questions Pédagogiques (Étudiant 4)

Voici les réponses aux questions demandées dans la phase finale du projet :

### 1. Pourquoi utiliser Application Factory ?
L'Application Factory (`create_app()`) permet de :
- **Faciliter les tests** : On peut créer plusieurs instances de l'application avec des configurations différentes (test, dév, prod).
- **Éviter les imports circulaires** : En ne déclarant pas l'objet `app` au niveau global, on réduit les risques de dépendances cycliques entre les modules.
- **Flexibilité** : Permet d'enregistrer les Blueprints dynamiquement au moment de l'initialisation.

### 2. Pourquoi séparer routes et services ?
La séparation (Pattern Service) permet de :
- **Séparation des responsabilités (SOC)** : Les routes s'occupent du HTTP (requêtes, templates, redirections), tandis que les services s'occupent de la logique métier (calculs, manipulation des données).
- **Réutilisabilité** : La logique dans `course_service.py` peut être réutilisée par une API, une commande CLI ou d'autres parties du code sans modifier les routes.
- **Maintenabilité** : Plus facile à tester unitairement sans avoir besoin du contexte Flask.

### 3. Que se passe-t-il si un blueprint n'est pas enregistré ?
Si un Blueprint n'est pas enregistré via `app.register_blueprint()` dans l'Application Factory :
- Les routes définies dans ce Blueprint ne seront **pas accessibles** par le serveur Flask.
- Toute tentative d'accès à ces URLs renverra une erreur **404 Not Found**.
- Flask ne connaîtra pas l'existence de ces endpoints.

### 4. Pourquoi utiliser url_prefix ?
L'argument `url_prefix` permet de :
- **Organiser les URLs** : Préfixer toutes les routes d'un module (ex: `/courses`, `/students`).
- **Éviter les collisions** : Si deux Blueprints utilisent la même route (ex: `/create`), le préfixe permet de les distinguer (ex: `/courses/create` vs `/students/create`).
- **Modularité** : Permet de changer le point d'entrée d'un module entier à un seul endroit sans toucher à toutes les routes.

### 5. Où doit se trouver la logique métier ?
La logique métier doit se trouver exclusivement dans la **couche Service** (`student_service.py`, `course_service.py`, etc.).
Les routes ne doivent servir que d'intermédiaire pour recevoir les données de l'utilisateur et renvoyer une réponse (Redirection ou Template).

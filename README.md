# Edu_CRM

Application web de gestion scolaire construite avec Flask.

## Prerequis

- Python 3.10+ (recommande)
- pip
- Un terminal:
	- PowerShell (Windows)
	- Terminal/Bash/zsh (macOS/Linux)

## Installation

1. Se placer dans le dossier du projet.
2. Creer un environnement virtuel.

Windows (PowerShell):

```powershell
python -m venv .venv
```

macOS/Linux:

```bash
python3 -m venv .venv
```

3. Activer l'environnement virtuel.

Windows (PowerShell):

```powershell
.\.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

4. Installer les dependances:

```bash
pip install -r requirements.txt
```

## Lancement de l'application Flask

Windows (PowerShell):

```powershell
flask --app app run
```

macOS/Linux:

```bash
flask --app app run
```

Si la commande `flask` n'est pas reconnue, utiliser:

Windows (PowerShell):

```powershell
.\.venv\Scripts\python -m flask --app app run
```

macOS/Linux:

```bash
python -m flask --app app run
```

ou

```bash
python3 -m flask --app app run
```

L'application sera disponible sur:

`http://127.0.0.1:5000`

## Comptes de test

- admin / 1234
- prof.martin@edu.com / 1234
- alice@edu.com / alice123
- bob@edu.com / bob123

## Membres du projet

- HOUNKPATIN Youan
- Ares Bienvenu
- Koffi Emmanuel Martin GAMISSO
- NYADZI-EMMANUEL
- Malik
- Joy
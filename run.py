# run.py
# ================================================
# Lance l'application via Flask CLI
# Commande équivalente : flask --app app run
# ================================================

import subprocess
import sys


if __name__ == "__main__":
    subprocess.run([sys.executable, "-m", "flask", "--app", "app", "run"], check=False)

# config.py
# ================================================
# Configuration de l'application Flask
# ================================================

class Config:
    # Clé secrète pour sécuriser les sessions et les flash messages
    # En production, ce serait une vraie clé complexe et cachée
    SECRET_KEY = "edu-crm-secret-123"

    # Mode debug désactivé par défaut
    DEBUG = False


class DevelopmentConfig(Config):
    # On hérite de Config et on active le debug pour le développement
    DEBUG = True


# On dit à l'app quelle config utiliser par défaut
config = {
    "development": DevelopmentConfig,
    "default": DevelopmentConfig
}
"""
Script d'initialisation de la base de données
À exécuter une seule fois pour créer les tables
"""
from models import init_db

if __name__ == '__main__':
    print("Initialisation de la base de données...")
    init_db()
    print("Base de données initialisée avec succès!")


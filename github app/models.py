import sqlite3
import os
from contextlib import contextmanager

DATABASE = os.path.join(os.path.dirname(__file__), 'deneigement.db')

def get_db():
    """Connexion à la base de données"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@contextmanager
def get_db_connection():
    """Context manager pour la connexion DB"""
    conn = get_db()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def init_db():
    """Initialise la base de données avec les tables nécessaires"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        
        # Table Clients
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                adresse TEXT NOT NULL,
                telephone TEXT NOT NULL,
                email TEXT,
                status TEXT DEFAULT 'planifié',
                heure_debut TEXT NOT NULL,
                heure_fin TEXT,
                date_intervention TEXT NOT NULL,
                type_service TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Ajouter la colonne type_service si elle n'existe pas (migration)
        try:
            cursor.execute('ALTER TABLE clients ADD COLUMN type_service TEXT')
        except sqlite3.OperationalError:
            pass  # La colonne existe déjà
        
        # Table Déneigeurs (pour multi-admin si besoin)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS deneigeurs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                login TEXT UNIQUE NOT NULL,
                mot_de_passe TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Table Notifications (historique)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notifications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER NOT NULL,
                type_notification TEXT NOT NULL,
                message TEXT NOT NULL,
                envoyee_sms BOOLEAN DEFAULT 0,
                envoyee_email BOOLEAN DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (client_id) REFERENCES clients (id)
            )
        ''')
        
        conn.commit()
        print("Base de données initialisée avec succès!")

def get_client_by_id(client_id):
    """Récupère un client par son ID"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM clients WHERE id = ?', (client_id,))
        row = cursor.fetchone()
        if row:
            return dict(row)
        return None

def get_all_clients():
    """Récupère tous les clients"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM clients ORDER BY date_intervention, heure_debut')
        rows = cursor.fetchall()
        return [dict(row) for row in rows]

def create_client(nom, adresse, telephone, email, date_intervention, heure_debut, heure_fin=None, type_service=None):
    """Crée un nouveau client"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO clients (nom, adresse, telephone, email, date_intervention, heure_debut, heure_fin, type_service, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'planifié')
        ''', (nom, adresse, telephone, email, date_intervention, heure_debut, heure_fin, type_service))
        return cursor.lastrowid

def update_client(client_id, nom=None, adresse=None, telephone=None, email=None, 
                  date_intervention=None, heure_debut=None, heure_fin=None, type_service=None):
    """Met à jour un client"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        updates = []
        params = []
        
        if nom:
            updates.append('nom = ?')
            params.append(nom)
        if adresse:
            updates.append('adresse = ?')
            params.append(adresse)
        if telephone:
            updates.append('telephone = ?')
            params.append(telephone)
        if email:
            updates.append('email = ?')
            params.append(email)
        if date_intervention:
            updates.append('date_intervention = ?')
            params.append(date_intervention)
        if heure_debut:
            updates.append('heure_debut = ?')
            params.append(heure_debut)
        if heure_fin is not None:
            updates.append('heure_fin = ?')
            params.append(heure_fin)
        if type_service is not None:
            updates.append('type_service = ?')
            params.append(type_service)
        
        if updates:
            updates.append('updated_at = CURRENT_TIMESTAMP')
            params.append(client_id)
            cursor.execute(f'UPDATE clients SET {", ".join(updates)} WHERE id = ?', params)
            return True
        return False

def update_client_status(client_id, status):
    """Met à jour le statut d'un client"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE clients 
            SET status = ?, updated_at = CURRENT_TIMESTAMP 
            WHERE id = ?
        ''', (status, client_id))
        return True

def delete_client(client_id):
    """Supprime un client"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM clients WHERE id = ?', (client_id,))
        return cursor.rowcount > 0

def log_notification(client_id, type_notification, message, envoyee_sms=False, envoyee_email=False):
    """Enregistre une notification dans l'historique"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO notifications (client_id, type_notification, message, envoyee_sms, envoyee_email)
            VALUES (?, ?, ?, ?, ?)
        ''', (client_id, type_notification, message, envoyee_sms, envoyee_email))
        return cursor.lastrowid


# 💻 Utilisation Locale - Dossier "github app"

Ce dossier contient **TOUTE l'application** et peut fonctionner **indépendamment**.

## 🚀 Lancer l'Application en Local

### Option 1 : Script Automatique (Recommandé)
Double-cliquez sur :
- **`DEMARRER_LOCAL.bat`** (Windows)
- **`DEMARRER_LOCAL.ps1`** (PowerShell)

### Option 2 : Manuel
```powershell
# Activer l'environnement virtuel (depuis le dossier parent)
..\venv\Scripts\Activate.ps1

# Installer les dépendances (si pas déjà fait)
pip install -r requirements.txt

# Initialiser la base de données
python init_db.py

# Lancer l'application
python app.py
```

## 📁 Structure

- **app.py** : Application principale
- **models.py** : Base de données (SQLite locale)
- **notifications.py** : Système de notifications
- **templates/** : Pages HTML
- **Images/** : Images de l'application
- **requirements.txt** : Dépendances Python

## ⚙️ Configuration

Créez un fichier **`.env`** dans ce dossier avec :
```
GMAIL_USER=votre.email@gmail.com
GMAIL_PASSWORD=votre_mot_de_passe_application
SECRET_KEY=cle-secrete
FLASK_ENV=development
```

## 📊 Base de Données

La base de données `deneigement.db` sera créée **automatiquement** dans ce dossier lors du premier lancement.

## 🌐 Accès

Une fois lancé, allez sur :
- **Dashboard** : http://localhost:5000/dashboard
- **Page client** : http://localhost:5000/client/{id}

## 📤 Pour GitHub

Tout le contenu de ce dossier est **prêt à être uploadé** sur GitHub.
Voir `INSTRUCTIONS_UPLOAD.md` pour les étapes.


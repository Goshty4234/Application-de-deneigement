# MVP Notification Déneigement

Application web simple pour gérer les interventions de déneigement et notifier automatiquement les clients.

## 🚀 Fonctionnalités

### Dashboard Déneigeur/Admin
- Gestion des clients (ajouter, modifier, supprimer)
- Planification des interventions avec fenêtres horaires
- Changement de statut des interventions (En route, Commencé, Terminé)
- Vue tableau/calendrier des interventions
- **📊 Statistiques avec graphiques**
- **🗺️ Carte globale avec tous les clients**
- **📄 Export PDF des rapports**
- **🔍 Filtres avancés** (statut, type de service, date, recherche)
- **🗺️ Mini-cartes** dans le tableau

### Notifications Automatiques
- **Notification 1** : Avant l'intervention (quand statut → "En route")
- **Notification 2** : Pendant l'intervention (quand statut → "Commencé") - optionnel
- **Notification 3** : Après l'intervention (quand statut → "Terminé")

### Page Client
- Affichage des informations d'intervention
- Statut en temps réel
- Auto-refresh toutes les 30 secondes

## 💻 Installation Locale

### Option 1 : Script Automatique
Double-cliquez sur `DEMARRER_LOCAL.bat` (Windows)

### Option 2 : Manuel
```bash
# Activer l'environnement virtuel (depuis le dossier parent)
..\venv\Scripts\Activate.ps1

# Installer les dépendances
pip install -r requirements.txt

# Initialiser la base de données
python init_db.py

# Lancer l'application
python app.py
```

L'application sera accessible sur `http://localhost:5000/dashboard`

## ⚙️ Configuration

Créez un fichier `.env` dans ce dossier avec :
```
GMAIL_USER=votre.email@gmail.com
GMAIL_PASSWORD=votre_mot_de_passe_application
SECRET_KEY=cle-secrete-changez-en-production
FLASK_ENV=development
```

**Note** : Utilisez un **mot de passe d'application Gmail** (16 caractères), pas votre mot de passe Gmail normal.
Voir `CONFIGURATION_GRATUITE.md` pour les instructions détaillées.

## 🌐 Déploiement en Ligne

### Sur Render (Recommandé)
1. Uploadez ce dossier sur GitHub
2. Connectez votre repo à Render
3. Ajoutez les variables d'environnement
4. C'est tout !

Voir `DEPLOIEMENT_RAPIDE.md` pour les détails.

## 📊 Base de Données

- **Local** : SQLite (`deneigement.db` dans ce dossier)
- **En ligne** : PostgreSQL (fourni par Render/Railway)

## 🆓 Notifications Gratuites

L'application utilise :
- **Gmail SMTP** pour les emails (100% gratuit, ~500/jour)
- **Email-to-SMS** pour les SMS (100% gratuit, pas de limite fixe)

Voir `CONFIGURATION_GRATUITE.md` pour la configuration.

## 📁 Structure

```
github app/
├── app.py                 # Application Flask principale
├── models.py              # Modèles de base de données
├── notifications.py        # Gestion des notifications
├── init_db.py            # Initialisation de la base de données
├── templates/             # Templates HTML
│   ├── dashboard.html    # Dashboard déneigeur
│   └── client.html       # Page client
├── Images/               # Images (fond d'écran)
├── requirements.txt      # Dépendances Python
├── Procfile             # Configuration Render
└── render.yaml          # Configuration Render
```

## 📚 Documentation

- `README_LOCAL.md` : Utilisation locale
- `INSTRUCTIONS_UPLOAD.md` : Guide pour GitHub
- `DEPLOIEMENT_RAPIDE.md` : Déploiement sur Render
- `CONFIGURATION_GRATUITE.md` : Configuration Gmail
- `GUIDE_TEST.md` : Guide de test

## 🎯 Fonctionnalités Avancées

- **Statistiques** : Graphiques interactifs avec Chart.js
- **Carte globale** : Vue de tous les clients sur une carte
- **Export PDF** : Génération de rapports
- **Calendrier** : Vue mois/semaine/jour avec FullCalendar
- **Filtres** : Recherche et filtrage avancé
- **Mini-cartes** : Aperçu rapide des adresses

## 📝 Licence

MIT

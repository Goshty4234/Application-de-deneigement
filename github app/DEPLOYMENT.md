# Guide de Déploiement

## Déploiement sur Render (Recommandé)

1. **Créer un compte sur [Render](https://render.com/)**

2. **Créer un nouveau Web Service**
   - Connecter votre repository GitHub/GitLab
   - Sélectionner le repository du projet
   - Render détectera automatiquement le fichier `render.yaml`

3. **Configurer les variables d'environnement**
   Dans le dashboard Render, ajoutez :
   - `TWILIO_ACCOUNT_SID`
   - `TWILIO_AUTH_TOKEN`
   - `TWILIO_PHONE_NUMBER`
   - `SENDGRID_API_KEY`
   - `SENDGRID_FROM_EMAIL`
   - `SECRET_KEY` (généré automatiquement par Render)
   - `FLASK_ENV=production`
   - `PORT=5000`

4. **Déployer**
   - Render déploiera automatiquement
   - L'URL sera fournie après le déploiement

## Déploiement sur Railway

1. **Créer un compte sur [Railway](https://railway.app/)**

2. **Nouveau projet depuis GitHub**
   - Connecter votre repository
   - Railway détectera automatiquement Python

3. **Configurer les variables d'environnement**
   - Ajouter toutes les variables listées ci-dessus

4. **Déployer**
   - Railway déploiera automatiquement

## Configuration Twilio

1. Créer un compte sur [Twilio](https://www.twilio.com/)
2. Obtenir un numéro de téléphone (plan trial disponible)
3. Récupérer :
   - Account SID
   - Auth Token
   - Numéro de téléphone (format: +1234567890)

## Configuration SendGrid

1. Créer un compte sur [SendGrid](https://sendgrid.com/)
2. Vérifier votre domaine ou utiliser l'email de vérification
3. Générer une clé API dans Settings > API Keys
4. Ajouter la clé dans les variables d'environnement

## Mode Développement Local

1. Installer les dépendances :
```bash
pip install -r requirements.txt
```

2. Créer le fichier `.env` :
```bash
# Copier config_example.txt en .env et remplir les valeurs
```

3. Initialiser la base de données :
```bash
python init_db.py
```

4. Lancer l'application :
```bash
python app.py
```

L'application sera accessible sur `http://localhost:5000`

## Notes Importantes

- **Base de données** : SQLite est utilisé par défaut. Pour la production, considérez PostgreSQL (disponible sur Render/Railway)
- **Notifications** : Si les clés API ne sont pas configurées, les notifications seront simulées dans les logs
- **Sécurité** : Changez le `SECRET_KEY` en production
- **HTTPS** : Render et Railway fournissent HTTPS automatiquement


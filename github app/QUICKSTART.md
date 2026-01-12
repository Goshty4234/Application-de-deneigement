# Démarrage Rapide

## Installation en 5 minutes

### 1. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 2. Configurer l'environnement
Créez un fichier `.env` à la racine du projet avec :
```
TWILIO_ACCOUNT_SID=votre_sid
TWILIO_AUTH_TOKEN=votre_token
TWILIO_PHONE_NUMBER=+1234567890
SENDGRID_API_KEY=votre_cle
SENDGRID_FROM_EMAIL=notifications@votreentreprise.com
SECRET_KEY=cle-secrete-changez-en-production
```

**Note** : Si vous n'avez pas encore de comptes Twilio/SendGrid, vous pouvez laisser ces valeurs vides. L'application fonctionnera mais les notifications seront simulées dans les logs.

### 3. Initialiser la base de données
```bash
python init_db.py
```

### 4. Lancer l'application
```bash
python app.py
```

### 5. Accéder à l'application
- **Dashboard déneigeur** : http://localhost:5000/dashboard
- **Page client** : http://localhost:5000/client/{id} (remplacer {id} par l'ID du client)

## Utilisation

### Ajouter un client
1. Cliquez sur "Ajouter un client" dans le dashboard
2. Remplissez les informations (nom, adresse, téléphone, date, heure)
3. Cliquez sur "Enregistrer"

### Changer le statut d'une intervention
1. Dans le tableau, cliquez sur le bouton correspondant :
   - **"En route"** → Envoie la notification 1 (client doit libérer l'entrée)
   - **"Commencé"** → Envoie la notification 2 (déneigeur sur place)
   - **"Terminé"** → Envoie la notification 3 (intervention terminée)

### Partager la page client
Chaque client a une URL unique : `/client/{id}` que vous pouvez partager avec vos clients.

## Test sans API externes

Pour tester sans configurer Twilio/SendGrid :
1. Laissez les variables d'environnement vides
2. Les notifications seront affichées dans la console/logs
3. L'application fonctionnera normalement

## Prochaines étapes

- Configurer Twilio pour les SMS réels
- Configurer SendGrid pour les emails réels
- Déployer sur Render ou Railway (voir DEPLOYMENT.md)


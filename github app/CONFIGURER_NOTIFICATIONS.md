# 📧📱 Configuration des Notifications Réelles

## État Actuel

**SANS configuration** : Les notifications sont **SIMULÉES** (affichées dans la console du terminal)

**AVEC configuration** : Les notifications sont **VRAIMENT ENVOYÉES** (SMS + Email)

---

## 🔧 Configuration Twilio (SMS)

### Étape 1 : Créer un compte Twilio
1. Allez sur https://www.twilio.com/
2. Créez un compte gratuit (plan trial disponible)
3. Vérifiez votre numéro de téléphone

### Étape 2 : Obtenir vos identifiants
1. Dans le dashboard Twilio, allez dans **Console** → **Account Info**
2. Notez :
   - **Account SID** (commence par AC...)
   - **Auth Token** (cliquez sur "View" pour le voir)

### Étape 3 : Obtenir un numéro de téléphone
1. Dans Twilio, allez dans **Phone Numbers** → **Buy a number**
2. Choisissez un numéro (gratuit avec le plan trial)
3. Notez le numéro (format : +1234567890)

### Étape 4 : Configurer dans l'application
1. Créez un fichier `.env` à la racine du projet
2. Ajoutez :
```
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=votre_auth_token_ici
TWILIO_PHONE_NUMBER=+1234567890
```

**Note** : Remplacez les valeurs par les vôtres !

---

## 📧 Configuration SendGrid (Email)

### Étape 1 : Créer un compte SendGrid
1. Allez sur https://sendgrid.com/
2. Créez un compte gratuit (100 emails/jour gratuits)

### Étape 2 : Vérifier votre email
1. SendGrid vous enverra un email de vérification
2. Cliquez sur le lien pour vérifier

### Étape 3 : Créer une clé API
1. Dans SendGrid, allez dans **Settings** → **API Keys**
2. Cliquez sur **Create API Key**
3. Donnez un nom (ex: "Deneigement App")
4. Choisissez **Full Access** ou **Restricted Access** (Mail Send)
5. **Copiez la clé** (vous ne pourrez plus la voir après !)

### Étape 4 : Configurer dans l'application
Dans votre fichier `.env`, ajoutez :
```
SENDGRID_API_KEY=SG.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
SENDGRID_FROM_EMAIL=notifications@votreentreprise.com
```

**Important** : 
- Remplacez par votre vraie clé API
- L'email doit être vérifié dans SendGrid

---

## 📝 Fichier .env Complet

Votre fichier `.env` devrait ressembler à ça :

```
# Twilio SMS
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=votre_auth_token_ici
TWILIO_PHONE_NUMBER=+1234567890

# SendGrid Email
SENDGRID_API_KEY=SG.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
SENDGRID_FROM_EMAIL=notifications@votreentreprise.com

# Flask
SECRET_KEY=votre-cle-secrete-ici
FLASK_ENV=development
```

---

## ✅ Tester les Notifications

1. **Redémarrez l'application** (arrêtez avec Ctrl+C, puis relancez `python app.py`)

2. **Dans le dashboard**, changez le statut d'un client :
   - Cliquez sur "En route"
   - Vérifiez le terminal : vous devriez voir "SMS envoyé avec succès" au lieu de "[SMS SIMULÉ]"

3. **Vérifiez** :
   - Le client reçoit un SMS sur son téléphone
   - Le client reçoit un email (vérifiez les spams)

---

## 💰 Coûts

### Twilio (SMS)
- **Plan Trial** : Gratuit (crédits de test)
- **Payant** : ~$0.0075 par SMS (environ 0.75 centime)
- **Numéro de téléphone** : Gratuit avec plan trial, ~$1/mois après

### SendGrid (Email)
- **Plan Free** : 100 emails/jour gratuit
- **Plan Essentials** : $19.95/mois pour 50,000 emails

---

## 🎯 Pour Tester SANS Configurer (Mode Simulation)

Si vous voulez juste tester l'application sans configurer les API :

1. **Ne créez pas de fichier `.env`** (ou laissez les valeurs vides)
2. **Lancez l'application normalement**
3. **Les notifications apparaîtront dans la console** du terminal
4. **L'application fonctionne normalement**, mais sans envoi réel

C'est parfait pour tester toutes les fonctionnalités !

---

## ❓ Problèmes Courants

### "Erreur envoi SMS"
- Vérifiez que votre numéro Twilio est actif
- Vérifiez que le numéro du client est au format international (+1234567890)
- Vérifiez vos identifiants dans `.env`

### "Erreur envoi email"
- Vérifiez que votre email est vérifié dans SendGrid
- Vérifiez que la clé API est correcte
- Vérifiez que vous n'avez pas dépassé la limite (100/jour en gratuit)

### Les notifications ne partent pas
- Vérifiez que le fichier `.env` existe et est bien formaté
- Redémarrez l'application après avoir modifié `.env`
- Vérifiez les logs dans le terminal pour voir les erreurs


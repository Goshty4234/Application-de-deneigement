# 🆓 Configuration 100% GRATUITE (Sans Limite Fixe)

## ✅ Solution Gratuite Implémentée

L'application utilise maintenant **Gmail SMTP** pour les emails et **Email-to-SMS** pour les SMS. **100% GRATUIT** et **sans limite fixe** !

---

## 📧 Configuration Gmail (Emails)

### Étape 1 : Activer l'authentification à deux facteurs
1. Allez sur https://myaccount.google.com/
2. **Sécurité** → **Validation en deux étapes** → Activez-la

### Étape 2 : Créer un mot de passe d'application
1. Toujours dans **Sécurité**, allez dans **Mots de passe des applications**
2. Sélectionnez **Application** : "Autre" (ou "Mail")
3. Sélectionnez **Appareil** : "Ordinateur Windows" (ou autre)
4. Cliquez sur **Générer**
5. **COPIEZ LE MOT DE PASSE** (16 caractères, vous ne pourrez plus le voir !)

### Étape 3 : Configurer dans l'application
Créez un fichier `.env` à la racine du projet :

```
# Gmail SMTP (100% GRATUIT, pas de limite fixe)
GMAIL_USER=votre.email@gmail.com
GMAIL_PASSWORD=votre_mot_de_passe_application_16_caracteres

# Flask
SECRET_KEY=votre-cle-secrete-ici
FLASK_ENV=development
```

**Important** : Utilisez le **mot de passe d'application** (16 caractères), PAS votre mot de passe Gmail normal !

---

## 📱 Configuration SMS (Email-to-SMS)

### Comment ça fonctionne
Les SMS sont envoyés via **Email-to-SMS** : on envoie un email à une adresse spéciale qui le convertit en SMS.

### Format des numéros
Les numéros doivent être au format :
- **Canada** : `+15141234567` (avec le + et l'indicatif 1)
- **US** : `+12125551234`

### Opérateurs supportés automatiquement
L'application essaie automatiquement ces formats :
- **Bell** : `numero@txt.bell.ca`
- **Rogers** : `numero@pcs.rogers.com`
- **Telus** : `numero@msg.telus.com`
- **Fido** : `numero@fido.ca`
- **Virgin Mobile** : `numero@vmobile.ca`
- **AT&T** (US) : `numero@txt.att.net`
- **Verizon** (US) : `numero@vtext.com`
- **T-Mobile** (US) : `numero@tmomail.net`

### Si ça ne fonctionne pas
Si le SMS n'arrive pas, vous pouvez spécifier manuellement le format dans le code `notifications.py` selon l'opérateur de votre client.

---

## 🎯 Avantages de cette Solution

✅ **100% GRATUIT** - Aucun coût
✅ **Pas de limite fixe** - Gmail permet ~500 emails/jour (renouvelable)
✅ **SMS gratuits** - Via Email-to-SMS (pas de limite fixe)
✅ **Simple à configurer** - Juste Gmail
✅ **Fiable** - Gmail est très fiable

---

## 📊 Limites (Non-Fixes)

### Gmail SMTP
- **~500 emails/jour** (limite renouvelable, pas fixe)
- Si vous dépassez, attendez 24h et ça reprend
- Pour plus, créez un deuxième compte Gmail

### Email-to-SMS
- **Pas de limite fixe** connue
- Dépend de l'opérateur du client
- Certains opérateurs peuvent bloquer si trop de messages

---

## 🚀 Configuration Rapide

1. **Créez le fichier `.env`** :
```
GMAIL_USER=votre.email@gmail.com
GMAIL_PASSWORD=mot_de_passe_application_16_caracteres
SECRET_KEY=cle-secrete-changez-en-production
```

2. **Redémarrez l'application**

3. **Testez** en changeant le statut d'un client

---

## 🔄 Migration depuis Twilio/SendGrid

Si vous aviez déjà configuré Twilio ou SendGrid, vous pouvez :
- **Les garder** : L'application essaiera d'abord Twilio/SendGrid, puis Gmail si ça échoue
- **Les retirer** : Supprimez simplement les variables du `.env`

---

## ❓ Problèmes Courants

### "Erreur d'authentification Gmail"
- Vérifiez que vous utilisez le **mot de passe d'application** (16 caractères)
- PAS votre mot de passe Gmail normal
- Vérifiez que la validation en 2 facteurs est activée

### "SMS n'arrive pas"
- Vérifiez que le numéro est au bon format (+1...)
- Certains opérateurs ne supportent pas Email-to-SMS
- Essayez de spécifier manuellement le format dans le code

### "Limite Gmail atteinte"
- Attendez 24h ou créez un deuxième compte Gmail
- 500 emails/jour est généralement suffisant pour une petite entreprise

---

## 💡 Astuce

Pour augmenter la limite d'emails, créez plusieurs comptes Gmail et alternez entre eux dans le code.

---

## ✅ C'est Tout !

Avec cette configuration, vous avez une solution **100% GRATUITE** et **sans limite fixe** (juste des limites renouvelables) !


# 🔍 Guide de Débogage - Erreur Envoi Email

## ✅ Vérifications à Faire

### 1. Vérifier le fichier `.env`

Ouvrez votre fichier `.env` et vérifiez qu'il contient :

```
GMAIL_USER=votre.email@gmail.com
GMAIL_PASSWORD=votre_mot_de_passe_application_16_caracteres
```

**Important** :
- ❌ PAS votre mot de passe Gmail normal
- ✅ Le **mot de passe d'application** de 16 caractères (sans espaces)

### 2. Vérifier les logs dans le terminal

Quand vous cliquez sur "Email test", regardez le terminal où l'application tourne. Vous devriez voir des messages comme :

```
🧪 TEST EMAIL - Envoi à client@email.com...
🔌 Connexion à Gmail SMTP...
🔐 Authentification avec votre.email@gmail.com...
📧 Envoi de l'email à client@email.com...
✅ Email envoyé avec succès à client@email.com
```

**Si vous voyez une erreur**, notez le message exact.

---

## ❌ Erreurs Courantes

### Erreur : "Gmail non configuré"
**Solution** : Vérifiez que `GMAIL_USER` et `GMAIL_PASSWORD` sont bien dans votre `.env`

### Erreur : "SMTPAuthenticationError" ou "Erreur d'authentification"
**Causes possibles** :
1. Vous utilisez votre mot de passe Gmail normal au lieu du mot de passe d'application
2. Le mot de passe d'application est incorrect
3. La validation en 2 facteurs n'est pas activée

**Solution** :
1. Allez sur https://myaccount.google.com/
2. **Sécurité** → **Mots de passe des applications**
3. Créez un nouveau mot de passe d'application
4. Copiez-le dans votre `.env` (sans espaces)

### Erreur : "Le client n'a pas d'adresse email"
**Solution** : Vérifiez que le client a bien un email dans la base de données

### Erreur : Connexion timeout
**Causes possibles** :
- Problème de connexion internet
- Firewall bloque le port 587

**Solution** : Vérifiez votre connexion internet

---

## 🧪 Test Rapide

1. **Vérifiez votre `.env`** :
   ```powershell
   Get-Content .env
   ```

2. **Redémarrez l'application** (important après modification du `.env`)

3. **Essayez d'envoyer un email de test**

4. **Regardez les logs dans le terminal** pour voir l'erreur exacte

---

## 💡 Astuce

Si ça ne fonctionne toujours pas, copiez-collez le message d'erreur exact du terminal ici et je vous aiderai !


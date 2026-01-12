# ⚙️ Configuration Render - Guide Rapide

## 🔧 Paramètres à Configurer sur Render

### 1. **Name** ✅
- Gardez : `Application-de-deneigement` (ou changez si vous voulez)

### 2. **Language** ⚠️ IMPORTANT - À CHANGER
- **Changez de "Docker" à "Python"**
- Render détectera automatiquement Flask

### 3. **Branch** ✅
- Gardez : `main` (ou votre branche principale)

### 4. **Region** ✅
- Gardez : `Oregon (US West)` (ou choisissez celui le plus proche de vous)

### 5. **Root Directory** ⚠️ IMPORTANT
- **Si votre code est dans un sous-dossier "github app"** :
  - Mettez : `github app`
- **Si vous avez uploadé directement les fichiers** (pas dans un sous-dossier) :
  - Laissez vide

### 6. **Dockerfile Path** ❌
- **Laissez vide** (pas nécessaire pour Python/Flask)

### 7. **Instance Type** ✅
- Gardez : **Free** (gratuit pour commencer)

---

## 📝 Résumé des Changements

**À CHANGER :**
1. **Language** : `Docker` → `Python`
2. **Root Directory** : Mettez `github app` si votre code est dans ce sous-dossier

**À GARDER :**
- Tout le reste peut rester par défaut

---

## ⚠️ Important

Si vous avez uploadé le contenu de "github app" **directement à la racine** du repository GitHub (pas dans un sous-dossier), alors :
- **Root Directory** : Laissez vide

Si vous avez uploadé le dossier "github app" **comme sous-dossier** dans GitHub, alors :
- **Root Directory** : Mettez `github app`

---

## ✅ Après Configuration

1. Cliquez sur "Create Web Service"
2. Render va :
   - Installer les dépendances
   - Démarrer l'application
   - Vous donner une URL publique

3. **Ajoutez les variables d'environnement** dans Settings → Environment :
   - `GMAIL_USER`
   - `GMAIL_PASSWORD`
   - `SECRET_KEY` (généré automatiquement ou créez-en un)
   - `FLASK_ENV=production`

---

## 🎯 Votre App Sera En Ligne !

Après ça, vous aurez une URL comme :
`https://application-de-deneigement.onrender.com`

Au lieu de `localhost:5000` ! 🎉


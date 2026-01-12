# 🚀 Comment Lancer l'Application - Guide Simple

## Étape 1 : Ouvrir le Terminal PowerShell

1. **Dans votre dossier du projet**, faites un **clic droit** sur un espace vide
2. Choisissez **"Ouvrir dans le terminal"** ou **"Ouvrir PowerShell ici"**

OU

1. Ouvrez **PowerShell** (cherchez "PowerShell" dans le menu Démarrer)
2. Naviguez vers votre dossier :
   ```powershell
   cd "D:\ENTREPRISE\Daler\Notification déneigement"
   ```

---

## Étape 2 : Activer l'Environnement Virtuel

Dans le terminal, tapez :
```powershell
.\venv\Scripts\Activate.ps1
```

**Vous devriez voir** `(venv)` apparaître au début de la ligne, comme ça :
```
(venv) PS D:\ENTREPRISE\Daler\Notification déneigement>
```

✅ **Si vous voyez (venv), c'est bon !**

---

## Étape 3 : Lancer l'Application

Tapez :
```powershell
python app.py
```

**Vous devriez voir** quelque chose comme :
```
 * Running on http://127.0.0.1:5000
 * Running on http://0.0.0.0:5000
```

✅ **Si vous voyez ça, l'application est lancée !**

---

## Étape 4 : Ouvrir dans le Navigateur

1. **Laissez le terminal ouvert** (ne le fermez pas !)
2. **Ouvrez votre navigateur** (Chrome, Firefox, Edge)
3. **Allez à :**
   ```
   http://localhost:5000/dashboard
   ```

---

## ⚠️ Important

- **Ne fermez PAS le terminal** tant que vous utilisez l'application
- Si vous fermez le terminal, l'application s'arrête
- Pour arrêter l'application, appuyez sur **Ctrl + C** dans le terminal

---

## 🎯 Résumé Rapide

1. Ouvrir PowerShell dans le dossier
2. `.\venv\Scripts\Activate.ps1`
3. `python app.py`
4. Ouvrir `http://localhost:5000/dashboard` dans le navigateur

C'est tout ! 🎉


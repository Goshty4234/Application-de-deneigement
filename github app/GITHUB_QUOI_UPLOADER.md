# 📤 Quoi Uploader sur GitHub - Guide Simple

## ✅ À METTRE sur GitHub (OUI)

### Fichiers de Code
- ✅ `app.py`
- ✅ `models.py`
- ✅ `notifications.py`
- ✅ `init_db.py`

### Dossiers
- ✅ `templates/` (tous les fichiers HTML)
- ✅ `Images/` (votre image de fond)

### Configuration
- ✅ `requirements.txt`
- ✅ `Procfile`
- ✅ `render.yaml`
- ✅ `.gitignore`
- ✅ `config_example.txt` (exemple, pas vos vraies données)

### Documentation
- ✅ Tous les fichiers `.md` (README, guides, etc.)

---

## ❌ À NE PAS METTRE sur GitHub (NON)

### Fichiers Sensibles
- ❌ `.env` (contient vos mots de passe Gmail !)
- ❌ `deneigement.db` (base de données locale)

### Dossiers Générés
- ❌ `venv/` (environnement virtuel, trop gros)
- ❌ `__pycache__/` (fichiers Python compilés)

### Fichiers Temporaires
- ❌ Tous les `.bat` et `.ps1` (scripts Windows locaux)
- ❌ Fichiers de logs

---

## 🎯 Résumé Simple

**METTEZ :**
- Tous les fichiers `.py`
- Le dossier `templates/`
- Le dossier `Images/`
- `requirements.txt`
- `Procfile`
- `.gitignore`
- Tous les fichiers `.md`

**NE METTEZ PAS :**
- `.env` (vos mots de passe)
- `venv/` (trop gros)
- `deneigement.db` (sera créé automatiquement)
- `__pycache__/`

---

## 💡 Astuce

Le fichier `.gitignore` que j'ai créé exclut automatiquement :
- `.env`
- `venv/`
- `*.db`
- `__pycache__/`

Donc même si vous les sélectionnez, GitHub ne les uploadera pas ! ✅

---

## 📝 Checklist Rapide

Avant d'uploader, vérifiez :
- [ ] `.env` n'est PAS sélectionné
- [ ] `venv/` n'est PAS sélectionné
- [ ] `deneigement.db` n'est PAS sélectionné
- [ ] Tous les fichiers `.py` sont sélectionnés
- [ ] Le dossier `templates/` est sélectionné
- [ ] Le dossier `Images/` est sélectionné

---

## 🚨 Important

Si vous uploadez `.env` par accident :
1. Changez immédiatement votre mot de passe Gmail
2. Créez un nouveau mot de passe d'application
3. Mettez à jour le `.env` sur Render

Mais avec le `.gitignore`, ça ne devrait pas arriver ! 😊


# 🧪 Test Local - Vérification

## ✅ Vérifications à Faire

### 1. Structure des Fichiers
Vérifiez que vous avez :
- [x] app.py
- [x] models.py
- [x] notifications.py
- [x] init_db.py
- [x] templates/ (avec dashboard.html et client.html)
- [x] Images/ (avec votre image)
- [x] requirements.txt
- [x] .env (à créer avec vos identifiants Gmail)

### 2. Test de Lancement
1. Ouvrez un terminal dans ce dossier "github app"
2. Lancez `DEMARRER_LOCAL.bat`
3. L'application devrait démarrer sur http://localhost:5000

### 3. Test des Fonctionnalités
- [ ] Dashboard s'affiche
- [ ] Ajouter un client fonctionne
- [ ] Calendrier s'affiche
- [ ] Statistiques s'affichent
- [ ] Carte globale fonctionne
- [ ] Export PDF fonctionne
- [ ] Mini-cartes s'affichent dans le tableau

### 4. Test des Notifications
- [ ] Email de test fonctionne (si Gmail configuré)
- [ ] Changement de statut déclenche les notifications

## 🐛 Si Problème

### Erreur "Module not found"
→ Activez l'environnement virtuel : `..\venv\Scripts\Activate.ps1`

### Erreur "Database not found"
→ Lancez `python init_db.py` une fois

### Erreur "Images not found"
→ Vérifiez que le dossier Images/ existe avec votre image

### Erreur "Templates not found"
→ Vérifiez que le dossier templates/ existe avec dashboard.html et client.html

## ✅ Si Tout Fonctionne

Vous pouvez maintenant uploader ce dossier complet sur GitHub ! 🎉


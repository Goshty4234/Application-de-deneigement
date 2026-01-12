# Guide de Test - Étape par Étape

## ✅ Étape 1 : Vérifier que l'application fonctionne

1. **Ouvrez votre navigateur web** (Chrome, Firefox, Edge, etc.)

2. **Allez à l'adresse suivante :**
   ```
   http://localhost:5000
   ```
   ou
   ```
   http://localhost:5000/dashboard
   ```

3. **Vous devriez voir :**
   - Un titre "Dashboard Déneigement"
   - Un bouton bleu "+ Ajouter un client"
   - Un tableau vide (ou avec des clients si vous en avez déjà ajouté)

✅ **Si vous voyez ça, l'application fonctionne !**

---

## ✅ Étape 2 : Ajouter votre premier client

1. **Cliquez sur le bouton bleu "+ Ajouter un client"**

2. **Remplissez le formulaire :**
   - **Nom** : Exemple : "Jean Dupont"
   - **Adresse** : Exemple : "123 rue Principale, Montréal"
   - **Téléphone** : Exemple : "+15141234567" (format international avec +)
   - **Email** : Exemple : "jean.dupont@email.com" (optionnel)
   - **Date intervention** : Choisissez une date (ex: demain)
   - **Heure début** : Exemple : "06:30"
   - **Heure fin** : Exemple : "07:00" (optionnel, laissez vide si une seule heure)

3. **Cliquez sur "Enregistrer"**

4. **Le client apparaît maintenant dans le tableau !**

---

## ✅ Étape 3 : Tester les notifications (changement de statut)

Dans le tableau, vous verrez votre client avec le statut "Planifié".

### Test 1 : Envoyer "En route"
1. **Cliquez sur le bouton jaune "En route"** à côté de votre client
2. **Confirmez** dans la popup
3. **Résultat attendu :**
   - Le statut change à "En route"
   - Une notification est envoyée (SMS + Email si configuré, sinon simulée dans la console)

### Test 2 : Envoyer "Commencé"
1. **Cliquez sur le bouton orange "Commencé"**
2. **Confirmez**
3. **Résultat :** Statut change à "Commencé"

### Test 3 : Envoyer "Terminé"
1. **Cliquez sur le bouton vert "Terminé"**
2. **Confirmez**
3. **Résultat :** Statut change à "Terminé"

---

## ✅ Étape 4 : Voir la page client

1. **Dans le tableau, notez l'ID du client** (première colonne ou dans l'URL si vous modifiez)

2. **Ouvrez un nouvel onglet dans votre navigateur**

3. **Allez à :**
   ```
   http://localhost:5000/client/1
   ```
   (Remplacez "1" par l'ID de votre client)

4. **Vous verrez :**
   - La page publique du client
   - Son statut actuel
   - Les informations de l'intervention
   - La page se met à jour automatiquement toutes les 30 secondes

---

## ✅ Étape 5 : Modifier un client

1. **Dans le dashboard, cliquez sur "Modifier"** à côté d'un client
2. **Changez les informations** (nom, adresse, heure, etc.)
3. **Cliquez sur "Enregistrer"**
4. **Les modifications apparaissent dans le tableau**

---

## ✅ Étape 6 : Supprimer un client

1. **Cliquez sur "Supprimer"** à côté d'un client
2. **Confirmez** dans la popup
3. **Le client disparaît du tableau**

---

## 📱 Test des Notifications

### Si vous avez configuré Twilio et SendGrid :
- Les SMS seront envoyés au numéro de téléphone du client
- Les emails seront envoyés à l'adresse email du client

### Si vous n'avez PAS configuré les API :
- Les notifications sont **simulées** dans la console du terminal
- Vous verrez des messages comme : `[SMS SIMULÉ] À +15141234567: ...`
- L'application fonctionne normalement, mais sans envoi réel

---

## 🎯 Scénario de test complet

1. **Ajoutez 3 clients** avec des dates/heures différentes
2. **Changez le statut** du premier client : Planifié → En route → Commencé → Terminé
3. **Ouvrez la page client** dans un autre onglet et observez les changements
4. **Modifiez** l'heure d'un client
5. **Supprimez** un client de test

---

## ❓ Problèmes courants

### L'application ne démarre pas
- Vérifiez que l'environnement virtuel est activé : `.\venv\Scripts\Activate.ps1`
- Vérifiez que vous êtes dans le bon dossier

### Erreur "Port déjà utilisé"
- Fermez l'application (Ctrl+C dans le terminal)
- Changez le port dans `app.py` (ligne avec `port = 5000`)

### La page ne se charge pas
- Vérifiez que l'application tourne (regardez le terminal)
- Essayez de rafraîchir la page (F5)

---

## 🎉 Félicitations !

Si vous avez réussi tous ces tests, votre application fonctionne parfaitement !

**Prochaines étapes :**
- Configurez Twilio et SendGrid pour les vraies notifications (voir QUICKSTART.md)
- Déployez sur Render ou Railway (voir DEPLOYMENT.md)


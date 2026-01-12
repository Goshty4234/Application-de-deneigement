from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
from dotenv import load_dotenv
import os
from models import (
    init_db, get_all_clients, get_client_by_id, create_client,
    update_client, update_client_status, delete_client
)
from notifications import (
    send_notification_en_route, send_notification_commence,
    send_notification_termine, send_notification_manuelle
)

load_dotenv()

# Configuration pour servir les fichiers statiques depuis le dossier actuel
app = Flask(__name__, 
            static_folder=os.path.dirname(__file__), 
            static_url_path='',
            template_folder=os.path.join(os.path.dirname(__file__), 'templates'))
CORS(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

# Initialiser la base de données au démarrage
with app.app_context():
    init_db()

@app.route('/')
def index():
    """Page d'accueil - redirige vers le dashboard"""
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    """Dashboard déneigeur/admin"""
    return render_template('dashboard.html')

@app.route('/client/<int:client_id>')
def client_page(client_id):
    """Page publique pour le client"""
    client = get_client_by_id(client_id)
    if not client:
        return "Client non trouvé", 404
    return render_template('client.html', client=client)

# API Endpoints

@app.route('/api/clients', methods=['GET'])
def api_get_clients():
    """Récupère tous les clients"""
    clients = get_all_clients()
    return jsonify(clients)

@app.route('/api/clients/<int:client_id>', methods=['GET'])
def api_get_client(client_id):
    """Récupère un client spécifique"""
    client = get_client_by_id(client_id)
    if not client:
        return jsonify({'error': 'Client non trouvé'}), 404
    return jsonify(client)

@app.route('/api/clients', methods=['POST'])
def api_create_client():
    """Crée un nouveau client"""
    data = request.json
    
    required_fields = ['nom', 'adresse', 'telephone', 'date_intervention', 'heure_debut']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Champ requis manquant: {field}'}), 400
    
    client_id = create_client(
        nom=data['nom'],
        adresse=data['adresse'],
        telephone=data['telephone'],
        email=data.get('email'),
        date_intervention=data['date_intervention'],
        heure_debut=data['heure_debut'],
        heure_fin=data.get('heure_fin'),
        type_service=data.get('type_service')
    )
    
    return jsonify({'id': client_id, 'message': 'Client créé avec succès'}), 201

@app.route('/api/clients/<int:client_id>', methods=['PUT'])
def api_update_client(client_id):
    """Met à jour un client"""
    client = get_client_by_id(client_id)
    if not client:
        return jsonify({'error': 'Client non trouvé'}), 404
    
    data = request.json
    update_client(
        client_id,
        nom=data.get('nom'),
        adresse=data.get('adresse'),
        telephone=data.get('telephone'),
        email=data.get('email'),
        date_intervention=data.get('date_intervention'),
        heure_debut=data.get('heure_debut'),
        heure_fin=data.get('heure_fin'),
        type_service=data.get('type_service')
    )
    
    return jsonify({'message': 'Client mis à jour avec succès'})

@app.route('/api/clients/<int:client_id>', methods=['DELETE'])
def api_delete_client(client_id):
    """Supprime un client"""
    client = get_client_by_id(client_id)
    if not client:
        return jsonify({'error': 'Client non trouvé'}), 404
    
    delete_client(client_id)
    return jsonify({'message': 'Client supprimé avec succès'})

@app.route('/api/clients/<int:client_id>/status', methods=['PUT'])
def api_update_status(client_id):
    """Met à jour le statut d'un client et déclenche les notifications"""
    client = get_client_by_id(client_id)
    if not client:
        return jsonify({'error': 'Client non trouvé'}), 404
    
    data = request.json
    new_status = data.get('status')
    
    if new_status not in ['planifié', 'en_route', 'commence', 'termine']:
        return jsonify({'error': 'Statut invalide'}), 400
    
    # Mettre à jour le statut
    update_client_status(client_id, new_status)
    
    # Déclencher les notifications selon le statut
    notification_sent = False
    if new_status == 'en_route':
        notification_sent = send_notification_en_route(client_id)
    elif new_status == 'commence':
        notification_sent = send_notification_commence(client_id)
    elif new_status == 'termine':
        notification_sent = send_notification_termine(client_id)
    
    return jsonify({
        'message': 'Statut mis à jour avec succès',
        'notification_sent': notification_sent
    })

@app.route('/api/notifications', methods=['POST'])
def api_send_notification():
    """Envoie une notification manuelle"""
    data = request.json
    client_id = data.get('client_id')
    message = data.get('message')
    
    if not client_id or not message:
        return jsonify({'error': 'client_id et message requis'}), 400
    
    client = get_client_by_id(client_id)
    if not client:
        return jsonify({'error': 'Client non trouvé'}), 404
    
    notification_sent = send_notification_manuelle(client_id, message)
    
    return jsonify({
        'message': 'Notification envoyée',
        'sent': notification_sent
    })

@app.route('/api/clients/<int:client_id>/test-email', methods=['POST'])
def api_send_test_email(client_id):
    """Envoie un email de test au client"""
    client = get_client_by_id(client_id)
    if not client:
        return jsonify({'error': 'Client non trouvé'}), 404
    
    if not client.get('email'):
        return jsonify({'error': 'Le client n\'a pas d\'adresse email'}), 400
    
    # Vérifier la configuration Gmail
    from notifications import GMAIL_USER, GMAIL_PASSWORD
    if not GMAIL_USER or not GMAIL_PASSWORD:
        return jsonify({
            'error': 'Gmail non configuré. Vérifiez votre fichier .env (GMAIL_USER et GMAIL_PASSWORD)',
            'sent': False
        }), 400
    
    # Message de test
    test_message = f"Bonjour {client['nom']},\n\nCeci est un email de test pour vérifier que les notifications fonctionnent correctement.\n\nVotre intervention est prévue le {client.get('date_intervention', 'N/A')}.\n\nCordialement,\nÉquipe de déneigement"
    
    # Envoyer l'email
    from notifications import send_email
    print(f"\n🧪 TEST EMAIL - Envoi à {client['email']}...")
    email_sent = send_email(
        client['email'],
        "Test - Notification Déneigement",
        test_message
    )
    
    if email_sent:
        return jsonify({
            'message': 'Email de test envoyé avec succès !',
            'sent': True
        })
    else:
        return jsonify({
            'error': 'Erreur lors de l\'envoi. Vérifiez les logs dans le terminal pour plus de détails.',
            'sent': False
        }), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)


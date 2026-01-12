import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from models import log_notification, get_client_by_id
from datetime import datetime
import re

# Configuration Gmail SMTP (100% GRATUIT, pas de limite fixe)
GMAIL_USER = os.getenv('GMAIL_USER')  # Votre adresse Gmail
GMAIL_PASSWORD = os.getenv('GMAIL_PASSWORD')  # Mot de passe d'application Gmail

# Configuration optionnelle Twilio (si vous voulez l'utiliser)
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

# Configuration optionnelle SendGrid (si vous voulez l'utiliser)
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
SENDGRID_FROM_EMAIL = os.getenv('SENDGRID_FROM_EMAIL')

def format_heure(heure_str):
    """Formate l'heure pour l'affichage (ex: 06:30 -> 6h30)"""
    try:
        if ':' in heure_str:
            h, m = heure_str.split(':')
            h = int(h)
            m = int(m)
            if m == 0:
                return f"{h}h"
            return f"{h}h{m:02d}"
        return heure_str
    except:
        return heure_str

def get_sms_email_gateways(telephone):
    """
    Convertit un numéro de téléphone en liste d'adresses email SMS selon différents opérateurs
    Fonctionne pour les opérateurs canadiens et américains
    Retourne une liste de gateways à essayer dans l'ordre
    """
    # Nettoyer le numéro (enlever +, espaces, tirets)
    clean_number = re.sub(r'[^\d]', '', telephone)
    
    # Si le numéro commence par 1 (Amérique du Nord), enlever le 1
    if clean_number.startswith('1') and len(clean_number) == 11:
        clean_number = clean_number[1:]
    
    # Formats Email-to-SMS pour opérateurs canadiens/américains
    # Ordre de préférence : opérateurs canadiens d'abord
    gateways = [
        f"{clean_number}@txt.bell.ca",           # Bell Canada
        f"{clean_number}@pcs.rogers.com",          # Rogers
        f"{clean_number}@msg.telus.com",           # Telus
        f"{clean_number}@fido.ca",                # Fido
        f"{clean_number}@vmobile.ca",            # Virgin Mobile
        f"{clean_number}@sms.rogers.com",         # Rogers alternatif
        f"{clean_number}@sms.bell.ca",           # Bell alternatif
        f"{clean_number}@txt.att.net",            # AT&T (US)
        f"{clean_number}@vtext.com",              # Verizon (US)
        f"{clean_number}@tmomail.net",            # T-Mobile (US)
    ]
    
    return gateways

def send_sms(telephone, message):
    """
    Envoie un SMS via Email-to-SMS (100% GRATUIT) ou Twilio si configuré
    """
    # Si Twilio est configuré, l'utiliser (plus fiable)
    if all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER]):
        try:
            from twilio.rest import Client as TwilioClient
            client = TwilioClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
            msg = client.messages.create(
                body=message,
                from_=TWILIO_PHONE_NUMBER,
                to=telephone
            )
            print(f"SMS envoyé avec succès via Twilio: {msg.sid}")
            return True
        except Exception as e:
            print(f"Erreur envoi SMS Twilio: {e}, tentative Email-to-SMS...")
    
    # Sinon, utiliser Email-to-SMS (GRATUIT)
    if GMAIL_USER and GMAIL_PASSWORD:
        gateways = get_sms_email_gateways(telephone)
        # Essayer chaque gateway jusqu'à ce qu'un fonctionne
        for sms_email in gateways:
            try:
                if send_email_via_smtp(sms_email, "", message):  # Pas de sujet pour SMS
                    print(f"SMS envoyé via Email-to-SMS à {sms_email}")
                    return True
            except Exception as e:
                print(f"Erreur avec {sms_email}: {e}, tentative suivante...")
                continue
        print(f"Impossible d'envoyer SMS à {telephone} via Email-to-SMS")
    
    # Mode simulation si rien n'est configuré
    print(f"[SMS SIMULÉ] À {telephone}: {message}")
    return False

def send_email_via_smtp(to_email, subject, message):
    """Envoie un email via Gmail SMTP (100% GRATUIT)"""
    if not GMAIL_USER or not GMAIL_PASSWORD:
        print("❌ GMAIL_USER ou GMAIL_PASSWORD non configuré dans .env")
        return False
    
    try:
        # Créer le message
        msg = MIMEMultipart()
        msg['From'] = GMAIL_USER
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain', 'utf-8'))
        
        # Connexion au serveur SMTP Gmail
        print(f"🔌 Connexion à Gmail SMTP...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        print(f"🔐 Authentification avec {GMAIL_USER}...")
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        
        # Envoyer l'email
        print(f"📧 Envoi de l'email à {to_email}...")
        text = msg.as_string()
        server.sendmail(GMAIL_USER, to_email, text)
        server.quit()
        
        print(f"✅ Email envoyé avec succès à {to_email}")
        return True
    except smtplib.SMTPAuthenticationError as e:
        print(f"❌ Erreur d'authentification Gmail: {e}")
        print("💡 Vérifiez que vous utilisez un 'mot de passe d'application' (16 caractères), pas votre mot de passe Gmail normal")
        return False
    except smtplib.SMTPException as e:
        print(f"❌ Erreur SMTP: {e}")
        return False
    except Exception as e:
        print(f"❌ Erreur envoi email SMTP: {e}")
        print(f"💡 Type d'erreur: {type(e).__name__}")
        return False

def send_email(email, subject, message):
    """
    Envoie un email via Gmail SMTP (GRATUIT) ou SendGrid si configuré
    """
    if not email:
        return False
    
    # Si SendGrid est configuré, l'utiliser
    if SENDGRID_API_KEY and SENDGRID_FROM_EMAIL:
        try:
            from sendgrid import SendGridAPIClient
            from sendgrid.helpers.mail import Mail
            sg = SendGridAPIClient(SENDGRID_API_KEY)
            mail = Mail(
                from_email=SENDGRID_FROM_EMAIL,
                to_emails=email,
                subject=subject,
                plain_text_content=message
            )
            response = sg.send(mail)
            print(f"Email envoyé avec succès via SendGrid: {response.status_code}")
            return True
        except Exception as e:
            print(f"Erreur envoi email SendGrid: {e}, tentative Gmail SMTP...")
    
    # Sinon, utiliser Gmail SMTP (GRATUIT)
    if GMAIL_USER and GMAIL_PASSWORD:
        if send_email_via_smtp(email, subject, message):
            print(f"Email envoyé avec succès via Gmail SMTP à {email}")
            return True
    
    # Mode simulation si rien n'est configuré
    print(f"[EMAIL SIMULÉ] À {email}: {subject} - {message}")
    return False

def send_notification_en_route(client_id):
    """Notification 1: Le déneigeur est en route"""
    client = get_client_by_id(client_id)
    if not client:
        return False
    
    heure_debut = format_heure(client['heure_debut'])
    heure_fin = format_heure(client['heure_fin']) if client['heure_fin'] else heure_debut
    
    if client['heure_fin']:
        message = f"Bonjour {client['nom']}, le déneigeur arrivera chez vous entre {heure_debut} et {heure_fin}. Merci de libérer votre entrée."
    else:
        message = f"Bonjour {client['nom']}, le déneigeur arrivera chez vous à {heure_debut}. Merci de libérer votre entrée."
    
    # Envoi SMS
    sms_sent = send_sms(client['telephone'], message)
    
    # Envoi Email
    email_sent = send_email(
        client['email'],
        "Déneigement prévu - Libérez votre entrée",
        message
    )
    
    # Log
    log_notification(client_id, "en_route", message, sms_sent, email_sent)
    
    return sms_sent or email_sent

def send_notification_commence(client_id):
    """Notification 2: Le déneigeur est sur place (optionnel)"""
    client = get_client_by_id(client_id)
    if not client:
        return False
    
    message = f"Le déneigeur est maintenant chez vous, intervention en cours."
    
    # Envoi SMS
    sms_sent = send_sms(client['telephone'], message)
    
    # Envoi Email
    email_sent = send_email(
        client['email'],
        "Déneigement en cours",
        message
    )
    
    # Log
    log_notification(client_id, "commence", message, sms_sent, email_sent)
    
    return sms_sent or email_sent

def send_notification_termine(client_id):
    """Notification 3: Intervention terminée"""
    client = get_client_by_id(client_id)
    if not client:
        return False
    
    message = f"Votre entrée est maintenant déneigée, vous pouvez remettre votre voiture. Merci!"
    
    # Envoi SMS
    sms_sent = send_sms(client['telephone'], message)
    
    # Envoi Email
    email_sent = send_email(
        client['email'],
        "Déneigement terminé",
        message
    )
    
    # Log
    log_notification(client_id, "termine", message, sms_sent, email_sent)
    
    return sms_sent or email_sent

def send_notification_manuelle(client_id, message, type_notif="manuelle"):
    """Envoie une notification manuelle"""
    client = get_client_by_id(client_id)
    if not client:
        return False
    
    # Envoi SMS
    sms_sent = send_sms(client['telephone'], message)
    
    # Envoi Email
    email_sent = send_email(
        client['email'],
        "Notification déneigement",
        message
    )
    
    # Log
    log_notification(client_id, type_notif, message, sms_sent, email_sent)
    
    return sms_sent or email_sent


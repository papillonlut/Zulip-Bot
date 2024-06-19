import zulip

# Initialiser le client Zulip
client = zulip.Client(config_file="zuliprc")

# Définir les paramètres du message
message = {
    "type": "stream",  # "stream" pour un message public ou "private" pour un message privé
    "to": "general",  # nom du salon "general" ou ["email_de_l_utilisateur"] pour un message privé
    "subject": "greetings", # Nom du sous-salon (inutile si message privée)
    "content": "Contenu du message" # Le message
}

# Envoyer le message
result = client.send_message(message)
print(result)

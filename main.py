import tweepy
from telegram import Bot
import time

# Configuration des identifiants de l'API Twitter
consumer_key = 'ta_clé_de_consommateur'
consumer_secret = 'ton_secret_de_consommateur'
access_token = 'ton_token_d\'accès'
access_token_secret = 'ton_secret_de_token_d\'accès'

# Configuration du token Telegram
telegram_token = 'ton_token_de_bot_telegram'

# Configuration des comptes Twitter à surveiller
comptes_a_surveiller = ['nom_utilisateur_1', 'nom_utilisateur_2']

# Configuration du mot-clé
mot_cle = ''

# Créer une instance de l'API Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter_api = tweepy.API(auth)

# Créer une instance du bot Telegram
telegram_bot = Bot(token=telegram_token)

# Fonction pour rechercher des tweets et envoyer des notifications sur Telegram
def rechercher_tweets_et_notifier(nom_utilisateur):
    # Obtenir l'heure actuelle
    current_time = time.time()
    # Obtenir l'heure de début du mois
    start_of_month = current_time - (current_time % 2592000)  # 2592000 secondes = 30 jours

    # Initialiser un compteur de requêtes
    request_count = 0

    # Rechercher les tweets de l'utilisateur spécifié
    tweets = tweepy.Cursor(twitter_api.user_timeline, screen_name=nom_utilisateur).items(1500)
    for tweet in tweets:
        # Vérifier si le tweet contient le mot-clé 'mot_cle'
        if mot_cle.lower() in tweet.text.lower():
            message = f"Un tweet a été trouvé dans le compte '{nom_utilisateur}' avec le mot-clé '{mot_cle}':\n{tweet.text}"
            # Envoyer la notification à un groupe Telegram
            telegram_bot.send_message(chat_id='chat_id', text=message)

        # Incrémenter le compteur de requêtes
        request_count += 1

        # Vérifier si la limite de 1500 tweets par mois est atteinte
        if request_count >= 1500:
            # Attendre jusqu'au début du mois suivant pour réinitialiser le compteur
            time_to_wait = start_of_month + 2592000 - current_time  # 2592000 secondes = 30 jours
            time.sleep(time_to_wait)
            # Réinitialiser le compteur de requêtes
            request_count = 0

if __name__ == "__main__":
    for compte in comptes_a_surveiller:
        rechercher_tweets_et_notifier(compte)

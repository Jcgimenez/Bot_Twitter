import tweepy
from telegram import Bot
import time

consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = 'access_token'
access_token_secret = 'access_token_secret'

telegram_token = 'token_bot_telegram'

comptes_a_surveiller = ['nom_utilisateur_1', 'nom_utilisateur_2']

mot_cle = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter_api = tweepy.API(auth)

telegram_bot = Bot(token=telegram_token)

def rechercher_tweets_et_notifier(nom_utilisateur):
    current_time = time.time()
    start_of_month = current_time - (current_time % 2592000)
    request_count = 0
    tweets = tweepy.Cursor(twitter_api.user_timeline, screen_name=nom_utilisateur).items(1500)
    for tweet in tweets:
        if mot_cle.lower() in tweet.text.lower():
            message = f"Un tweet a été trouvé dans le compte '{nom_utilisateur}' avec le mot-clé '{mot_cle}':\n{tweet.text}"
            telegram_bot.send_message(chat_id='chat_id', text=message)

        request_count += 1

        if request_count >= 1500:
            time_to_wait = start_of_month + 2592000 - current_time
            time.sleep(time_to_wait)
            request_count = 0

if __name__ == "__main__":
    for compte in comptes_a_surveiller:
        rechercher_tweets_et_notifier(compte)

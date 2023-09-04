README - Monitor Twitter Accounts for Keywords and Notify via Telegram

This Python script is designed to monitor specific Twitter accounts for tweets containing a specified keyword and notify you via a Telegram bot. It uses the Tweepy library to access the Twitter API for retrieving tweets and the python-telegram-bot library for sending notifications to a Telegram chat.

Prerequisites
Before using this script, make sure you have the following:

1. Twitter Developer Account: You need to create a Twitter Developer account and obtain API keys and access tokens. Replace the placeholder values in the script with your actual keys and tokens.
2. Telegram Bot: Create a Telegram bot and obtain its token. Replace the telegram_token variable with your bot's token.
3. Python Libraries: You must have the tweepy and python-telegram-bot libraries installed. You can install them using pip:
pip install tweepy python-telegram-bot


Configuration
Before running the script, you need to configure it by setting the following variables at the beginning of the script:

. consumer_key: Your Twitter API consumer key.
. consumer_secret: Your Twitter API consumer secret.
. access_token: Your Twitter API access token.
. access_token_secret: Your Twitter API access token secret.
. telegram_token: Your Telegram bot token.
. comptes_a_surveiller: A list of Twitter usernames (without '@') that you want to monitor.
. mot_cle: The keyword you want to search for in tweets.


Usage
1. Configure the script with your Twitter API and Telegram bot credentials and the accounts you want to monitor.
2. Run the script using Python:
  python script_name.py
3. The script will start monitoring the specified Twitter accounts for tweets containing the specified keyword.
4. If a tweet matching the keyword is found, it will send a notification to your Telegram bot with the tweet content.
5. The script will continue to monitor tweets, and if it reaches the Twitter API rate limit (1500 requests per 15 minutes), it will wait until the next month to reset the rate limit and continue monitoring.
6. The monitoring process will continue indefinitely until you stop the script.

Note: Make sure your Telegram bot is added to the chat where you want to receive notifications and replace 'chat_id' with the actual chat ID in the telegram_bot.send_message call.
Feel free to customize the script to suit your specific monitoring needs.

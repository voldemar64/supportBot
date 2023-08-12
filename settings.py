import os
from dotenv import load_dotenv, find_dotenv

# Loading .env variables
load_dotenv(find_dotenv())

#TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_TOKEN = '6640138493:AAEB7pRHv_YvjAct9A-x1X04pprHn63a3Fw'
if TELEGRAM_TOKEN is None:
    raise Exception("Please setup the .env variable TELEGRAM_TOKEN.")

#PORT = int(os.environ.get('PORT', '8443'))
PORT = 8443
TELEGRAM_SUPPORT_CHAT_ID = -938774742
#TELEGRAM_SUPPORT_CHAT_ID = os.environ.get("TELEGRAM_SUPPORT_CHAT_ID")
if TELEGRAM_SUPPORT_CHAT_ID is None or not str(TELEGRAM_SUPPORT_CHAT_ID).lstrip("-").isdigit():
    raise Exception("You need to specify 'TELEGRAM_SUPPORT_CHAT_ID' env variable: The bot will forward all messages to this chat_id. Add this bot https://t.me/ShowJsonBot to your private chat to find its chat_id.")
TELEGRAM_SUPPORT_CHAT_ID = int(TELEGRAM_SUPPORT_CHAT_ID)

WELCOME_MESSAGE = 'Welcome to the support bot!'
REPLY_TO_THIS_MESSAGE = "User above don't allow forward his messages. Reply to this message."
WRONG_REPLY = "User above don't allow forward his messages. You must reply to bot reply under user forwarded message."
#WELCOME_MESSAGE = os.environ.get("WELCOME_MESSAGE")
#REPLY_TO_THIS_MESSAGE = os.environ.get("REPLY_TO_THIS_MESSAGE")
#WRONG_REPLY = os.environ.get("WRONG_REPLY")
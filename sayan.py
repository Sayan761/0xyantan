import requests
import json
from telegram.ext import Updater, CommandHandler

def get_crypto_price(coin):
    URL = 'https://api.coingecko.com/api/v3/simple/price?ids=' + coin + '&vs_currencies=usd'
    response = requests.get(URL)
    data = response.json()
    price = data[coin]['usd']
    return price

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I am a bot that can give you the current price of cryptocurrencies. Type /price followed by the symbol of the cryptocurrency to get its price in USD.")

def price(update, context):
    coin = context.args[0].lower()
    price = get_crypto_price(coin)
    context.bot.send_message(chat_id=update.effective_chat.id, text=coin.upper() + " is currently trading at $" + str(price) + " USD.")

def main():
    updater = Updater(token='5701549938:AAGZTK-B5XcAUlWvVEAM-2T924LqKf2ZJK0', use_context=True)
    dp = updater.dispatcher
   

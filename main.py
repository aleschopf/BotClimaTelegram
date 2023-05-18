from consulta_clima import consultar_clima
from dotenv import load_dotenv 
import telebot
import os

load_dotenv()

CHAVE_API = os.getenv("API_KEY")

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Envie o local que deseja consultar o clima que irei lhe enviar a temperatura e a previsão do tempo atual.")

@bot.message_handler()
def clima(message):
    try:
        resultado = consultar_clima(message.text)
        mensagem = "O clima para o local informado é: " + resultado
        bot.send_message(message.chat.id, mensagem)
    except:
        bot.send_message(message.chat.id, "Gentileza tentar novamente")

bot.infinity_polling()

from telebot import TeleBot
from telebot.types import Message
from buttons import menu

TOKEN = '7738326967:AAHqHSaJXbpRfofEUN4aFpn8ZVYFlaEE76w'

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Assalomu alekum !",
                     reply_markup=menu())

@bot.message_handler(commands=['help'])
def help(message : Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Adminga murojaat qiling : @felix_teacher ")

if __name__ == '__main__':
    bot.infinity_polling()
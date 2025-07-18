from telebot import TeleBot
from telebot.types import Message

TOKEN = '7738326967:AAHqHSaJXbpRfofEUN4aFpn8ZVYFlaEE76w'

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Assalomu alekum !")


if __name__ == '__main__':
    bot.infinity_polling()
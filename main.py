from telebot import TeleBot

TOKEN = '7738326967:AAHqHSaJXbpRfofEUN4aFpn8ZVYFlaEE76w'

bot = TeleBot(TOKEN)

if __name__ == '__main__':
    bot.infinity_polling()
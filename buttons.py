from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = KeyboardButton("Fantastic")
    btn2 = KeyboardButton("Komediya")
    btn3 = KeyboardButton("Drama")
    btn4 = KeyboardButton("Triler")
    btn5 = KeyboardButton("Detectiv")
    markup.add(btn1, btn2, btn3, btn4)
    return markup

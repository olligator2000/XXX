# BOT_API = "7770590397:AAHBSzmBrZLiZxYe5JJHTh-2QvTm2K1I3r8"
#
# import telebot
# from telebot.types import ReplyKeyboardMarkup
#
# bot = telebot.TeleBot(BOT_API)
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, "😎╭∩╮( •̀_•́ )╭∩╮Привет! Я твой первый телеграм бот!╭∩╮( •̀_•́ )╭∩╮😎")
#
#
# @bot.message_handler(commands=['help'])
# def help_command(message):
#     bot.send_message(message.chat.id, "Я могу отвечать на команды /start и /help")
#
#
# @bot.message_handler(func=lambda message: True)
# def unknown_command(message):
#     # bot.send_message(message.chat.id, "Я не понимаю эту команду!")
#     bot.send_message(message.chat.id, message.text)
#     bot.send_message(message.chat.id, f"Пользователь: {message.from_user.username}")
#     print(message)
#
#
# bot.polling()

##################################################### МЕНЮ с КНОПКАМИ_в строке сообщения

# BOT_API = "7770590397:AAHBSzmBrZLiZxYe5JJHTh-2QvTm2K1I3r8"
#
#
# import telebot
# from telebot.types import ReplyKeyboardMarkup, KeyboardButton
#
#
# bot = telebot.TeleBot(BOT_API)
#
#
# def main_menu():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     button_1 = KeyboardButton('О боте')
#     button_2 = KeyboardButton('Помощь')
#     button_3 = KeyboardButton('Случайный факт')
#     markup.add(button_1, button_2, button_3)
#     return markup
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, "😎╭∩╮( •̀_•́ )╭∩╮Привет! Я твой первый телеграм бот!╭∩╮( •̀_•́ )╭∩╮😎", reply_markup=main_menu())
#
#
# @bot.message_handler(commands=['help'])
# def help_command(message):
#     bot.send_message(message.chat.id, "Я могу отвечать на команды /start и /help")
#
#
# @bot.message_handler(func=lambda message: True)
# def unknown_command(message):
#     # bot.send_message(message.chat.id, "Я не понимаю эту команду!")
#     bot.send_message(message.chat.id, message.text)
#     bot.send_message(message.chat.id, f"Пользователь: {message.from_user.username}")
#     print(message)
#
#
# @bot.message_handler(func=lambda message: message.text in ['О боте', 'Помощь', 'Случайный факт'])
# def handler_buttons(message):
#     if message.text == 'О боте':
#         bot.send_message(message.chat_id, "Я тестовый бот для обучения")
#     elif message.text == 'Помощь':
#         bot.send_message(message.chat_id, "Я могу отвечать и показывать кнопки")
#     elif message.text == 'Случайный факт':
#         bot.send_message(message.chat_id, "Факт")
#
#
# bot.polling()


##################################################### МЕНЮ с КНОПКАМИ_в сообщении

BOT_API = "7770590397:AAHBSzmBrZLiZxYe5JJHTh-2QvTm2K1I3r8"


import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


bot = telebot.TeleBot(BOT_API)


def inline_menu():
    markup = InlineKeyboardMarkup(row_width=3)
    button_1 = InlineKeyboardButton('Открыть сайт Телебот:', url="https://pypi.org/project/pyTelegramBotAPI/")
    button_2 = InlineKeyboardButton('Открыть сайт Телебот:', url="https://avatars.mds.yandex.net/get-mpic/1571231/img_id779278418351969261.jpeg/orig")
    button_3 = InlineKeyboardButton('Узнать больше', callback_data='info')
    markup.add(button_1, button_2, button_3)
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "😎╭∩╮( •̀_•́ )╭∩╮Привет! Я твой первый телеграм бот!╭∩╮( •̀_•́ )╭∩╮😎")


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "Я могу отвечать на команды /start и /help")


@bot.message_handler(commands=['menu'])
def menu(message):
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=inline_menu())


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "info":
        bot.send_message(call.message.chat.id, "Этот бот создан в на Python")


bot.polling()
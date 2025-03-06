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

# BOT_API = "7770590397:AAHBSzmBrZLiZxYe5JJHTh-2QvTm2K1I3r8"
#
#
# import telebot
# from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
#
#
# bot = telebot.TeleBot(BOT_API)
#
#
# def inline_menu():
#     markup = InlineKeyboardMarkup(row_width=2)
#     button_1 = InlineKeyboardButton('Открыть сайт Телебот:', url="https://pypi.org/project/pyTelegramBotAPI/")
#     button_2 = InlineKeyboardButton('Открыть сайт Телебот:', url="https://avatars.mds.yandex.net/get-mpic/1571231/img_id779278418351969261.jpeg/orig")
#     button_3 = InlineKeyboardButton('Узнать больше', callback_data='info')
#     button_4 = InlineKeyboardButton('Узнать больше', callback_data='info')
#     button_5 = InlineKeyboardButton('Узнать больше', callback_data='info')
#     button_6 = InlineKeyboardButton('Узнать больше', callback_data='info')
#     button_7 = InlineKeyboardButton('Узнать больше', callback_data='info')
#     button_8 = InlineKeyboardButton('Узнать больше', callback_data='info')
#     markup.add(button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8)
#     return markup
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
# @bot.message_handler(commands=['menu'])
# def menu(message):
#     bot.send_message(message.chat.id, "Выберите действие:", reply_markup=inline_menu())
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_query(call):
#     if call.data == "info":
#         bot.send_message(call.message.chat.id, "Этот бот создан в на Python")
#
#
# bot.polling()



####################################################### Бот для поиска фильмов

# import telebot
# import requests
#
# from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
# from telebot.types import ReplyKeyboardMarkup, KeyboardButton
#
# BOT_API = "7683989927:AAExSrCaEwgYo_90HFYUVIgn5DIWmJTarjk"
# OMDB_API_KEY = "caf5b564"
#
# bot = telebot.TeleBot(BOT_API)
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, "😎Привет! Я бот для поиска фильмов.😎\n"
#                                         "Напиши название фильма на английском и я найду информацию о нем!")
#
#
# def get_movie_info(title):
#     url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
#     response = requests.get(url)
#     data = response.json()
#
#     if data.get("Response") == "True":
#         movie_info = (
#             f"🎥 *{data['Title']}* *({data['Year']})*\n"
#             f"🌟 *Рейтинг:* {data['imdbRating']}\n"
#             f"🎬 *Жанр:* {data['Genre']}\n"
#             f"👤 *Режиссер:* {data['Genre']}\n"
#             f"👽 *Актеры:* {data['Actors']}\n"
#             f"💬 *Описание:* {data['Plot']}\n"
#         )
#         poster = data.get("Poster", "")
#         return movie_info, poster
#     else:
#         return "Фильм по такому запросу не найден!", None
#
#
# @bot.message_handler(func=lambda message: True)
# def search_movie(message):
#     movie_info, poster = get_movie_info(message.text)
#     if poster and poster != "N/A":
#         bot.send_photo(message.chat.id, poster, caption=movie_info, parse_mode="Markdown")
#     else:
#         bot.send_message(message.chat.id, movie_info, parse_mode="Markdown")
#
#
# bot.polling()


####################################################### Бот для поиска фильмов по названию и году выпуска

import telebot
import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_API = "7683989927:AAExSrCaEwgYo_90HFYUVIgn5DIWmJTarjk"
OMDB_API_KEY = "caf5b564"

bot = telebot.TeleBot(BOT_API)

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    button_title = InlineKeyboardButton("Поиск по названию фильма", callback_data='search_by_title')
    button_year = InlineKeyboardButton("Поиск по году выпуска", callback_data='search_by_year')
    markup.add(button_title, button_year)

    bot.send_message(message.chat.id, "😎Привет! Я бот для поиска фильмов.😎\n"
                                        "Выбери способ поиска:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'search_by_title':
        bot.send_message(call.message.chat.id, "Напиши название фильма на английском:")
        bot.answer_callback_query(call.id)
    elif call.data == 'search_by_year':
        bot.send_message(call.message.chat.id, "Напиши год выпуска фильма:")
        bot.answer_callback_query(call.id)

def get_movie_info(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "True":
        movie_info = (
            f"🎥 *{data['Title']}* *({data['Year']})*\n"
            f"🌟 *Рейтинг:* {data['imdbRating']}\n"
            f"🎬 *Жанр:* {data['Genre']}\n"
            f"👤 *Режиссер:* {data['Director']}\n"
            f"👽 *Актеры:* {data['Actors']}\n"
            f"💬 *Описание:* {data['Plot']}\n"
        )
        poster = data.get("Poster", "")
        return movie_info, poster
    else:
        return "Фильм по такому запросу не найден!", None

@bot.message_handler(func=lambda message: True)
def search_movie(message):
    # Попробуем сначала извлечь год из сообщения
    try:
        year = int(message.text)
        # Здесь я добавлю логику для поиска по году. Например, вы можете выполнять запросы к API, чтобы вернуть фильмы за этот год
        bot.send_message(message.chat.id, f"Ищу фильмы, выпущенные в {year}...")
        # Здесь можно вызвать функцию поиска фильмов по году
    except ValueError:
        # Если это не год, то искать по названию фильма
        movie_info, poster = get_movie_info(message.text)
        if poster and poster != "N/A":
            bot.send_photo(message.chat.id, poster, caption=movie_info, parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, movie_info, parse_mode="Markdown")

bot.polling()

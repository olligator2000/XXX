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

# import telebot
# import requests
# from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
#
# BOT_API = "7683989927:AAExSrCaEwgYo_90HFYUVIgn5DIWmJTarjk"
# OMDB_API_KEY = "caf5b564"
#
# bot = telebot.TeleBot(BOT_API)
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = InlineKeyboardMarkup()
#     button_title = InlineKeyboardButton("Поиск по названию фильма", callback_data='search_by_title')
#     button_year = InlineKeyboardButton("Поиск по году выпуска", callback_data='search_by_year')
#     markup.add(button_title, button_year)
#
#     bot.send_message(message.chat.id, "😎Привет! Я бот для поиска фильмов.😎\n"
#                                         "Выбери способ поиска:", reply_markup=markup)
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_query(call):
#     if call.data == 'search_by_title':
#         bot.send_message(call.message.chat.id, "Напиши название фильма на английском:")
#         bot.answer_callback_query(call.id)
#     elif call.data == 'search_by_year':
#         bot.send_message(call.message.chat.id, "Напиши год выпуска фильма:")
#         bot.answer_callback_query(call.id)
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
#             f"👤 *Режиссер:* {data['Director']}\n"
#             f"👽 *Актеры:* {data['Actors']}\n"
#             f"💬 *Описание:* {data['Plot']}\n"
#         )
#         poster = data.get("Poster", "")
#         return movie_info, poster
#     else:
#         return "Фильм по такому запросу не найден!", None
#
# @bot.message_handler(func=lambda message: True)
# def search_movie(message):
#     # Попробуем сначала извлечь год из сообщения
#     try:
#         year = int(message.text)
#         # Здесь я добавлю логику для поиска по году. Например, вы можете выполнять запросы к API, чтобы вернуть фильмы за этот год
#         bot.send_message(message.chat.id, f"Ищу фильмы, выпущенные в {year}...")
#         # Здесь можно вызвать функцию поиска фильмов по году
#     except ValueError:
#         # Если это не год, то искать по названию фильма
#         movie_info, poster = get_movie_info(message.text)
#         if poster and poster != "N/A":
#             bot.send_photo(message.chat.id, poster, caption=movie_info, parse_mode="Markdown")
#         else:
#             bot.send_message(message.chat.id, movie_info, parse_mode="Markdown")
#
# bot.polling()


####################################################### Бот прогноза погоды


# import telebot
# import requests
# from telebot.types import ReplyKeyboardMarkup, KeyboardButton
#
#
# BOT_API = "7770590397:AAHBSzmBrZLiZxYe5JJHTh-2QvTm2K1I3r8"
# WEATHER_API_KEY = "b73eeacce06afd66ec194738c9a4e57d"
#
# bot = telebot.TeleBot(BOT_API)
#
#
# def main_menu():
#     markup = ReplyKeyboardMarkup(row_width=2)
#     button_1 = KeyboardButton("Москва")
#     button_2 = KeyboardButton("Санкт-Петербург")
#     button_3 = KeyboardButton("Ввести город")
#     markup.add(button_1, button_2, button_3)
#     return markup
#
#
# def get_weather(city):
#     url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={WEATHER_API_KEY}'
#     response = requests.get(url).json()
#
#     if response.get("main"):
#         return (
#             f'Город: {city}\n'
#             f'Температура: {response["main"]["temp"]}°C\n'
#             f'Влажность: {response["main"]["humidity"]}%\n'
#             f'Ветер: {response["wind"]["speed"]}м/с\n'
#             f'Давление: {response["main"]["pressure"]}рт.ст.\n'
#         )
#     else:
#         return "Город не найден"
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, "😎Привет! Я бот для прогноза погоды по городу.😎\n"
#                                         "Выбери город или введи название:", reply_markup=main_menu())
#
#
# @bot.message_handler(func=lambda message: message.text in ["Москва", "Санкт-Петербург"])
# def handle_buttons(message):
#     city = message.text
#     bot.send_message(message.chat.id, get_weather(city))
#
#
# @bot.message_handler(func=lambda message: message.text == "Ввести город")
# def handle_buttons(message):
#     bot.send_message(message.chat.id, "Введите название города")
#     bot.register_next_step_handler(message, send_weather)
#
#
# def send_weather(message):
#     city = message.text
#     bot.send_message(message.chat.id, get_weather(city))
#
#
# bot.polling()

###########################################################################
###########################################################################
###########################################################################

# 3. Бот-анализатор новостей
# Описание:
# Бот ищет актуальные новости по ключевым словам и отправляет пользователю.
# Функционал:
# ✅ Получение свежих новостей (API: NewsAPI)
# ✅ Подписка на темы (технологии, спорт, экономика)
# ✅ Автоматическая отправка новостей каждый день
# ✅ Анализ тональности (позитивная/негативная)
# ✅ Перевод заголовков на русский (Google Translate API)
# Как сделать круче?
# • Добавить автоматическое резюме новостей с помощью GPT API.
# • Сделать голосовое озвучивание новостей (pyttsx3).
# • Подключить возможность фильтровать фейковые новости.

from datetime import date, timedelta
import telebot
import requests
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from newsdataapi import NewsDataApiClient

BOT_API = "7770590397:AAHBSzmBrZLiZxYe5JJHTh-2QvTm2K1I3r8"
NEWS_API_KEY = "pub_740976a50713043bac6ec9aa65409f1ec42e6"

bot = telebot.TeleBot(BOT_API)

today = date.today()
yesterday = today - timedelta(days=1)
formatted_date_today = today.strftime("%Y-%m-%d")
formatted_date_yesterday = yesterday.strftime("%Y-%m-%d")


def main_menu():
    markup = ReplyKeyboardMarkup(row_width=2)
    button_1 = KeyboardButton("Получить последние новости")
    button_2 = KeyboardButton("Получить новости по ключевому слову")
    button_3 = KeyboardButton("Подписаться на темы")
    button_4 = KeyboardButton("Отписаться от тем")
    button_5 = KeyboardButton("Получить последние новости по подписке")
    button_6 = KeyboardButton("Вкл автоматическую отправку новостей")
    button_7 = KeyboardButton("Выкл автоматическую отправку новостей")
    button_8 = KeyboardButton("Информация/Мои подписки")
    markup.add(button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8)
    return markup


def main_menu_subscription():
    markup = ReplyKeyboardMarkup(row_width=2)
    button_1 = KeyboardButton("Бизнес")
    button_2 = KeyboardButton("Развлечение")
    button_3 = KeyboardButton("Технологии")
    button_4 = KeyboardButton("Спорт")
    button_5 = KeyboardButton("Экономика")
    button_6 = KeyboardButton("Политика")
    button_7 = KeyboardButton("Назад↩️")
    markup.add(button_1, button_2, button_3, button_4, button_5, button_6, button_7)
    return markup


def latest_news():
    url = f'https://newsdata.io/api/1/latest?apikey={NEWS_API_KEY}&country=ru&language=ru'
    response = requests.get(url).json()
    keys = response["results"]

    for i in range(len(keys)):
        dt_string = keys[i]["pubDate"]
        if keys[i]["category"] == "top" or dt_string[:10] == formatted_date_today:
            article_info = (
                f'*Название статьи:* {keys[i]["title"]}\n'
                f'*Ссылка на источник:* {keys[i]["link"]}\n'
                f'*Автор новостной статьи:* {keys[i]["creator"]}\n'
                f'*Дата публикации:* {keys[i]["pubDate"]}\n'
                f'Категория: {keys[i]["category"]}\n'
            )
            poster = keys[i]["image_url"]
            return article_info, poster
        else:
            return "Свежих новостей нет!"


def key_word_news(key_word):
    url = f'https://newsdata.io/api/1/latest?q={key_word}&apikey={NEWS_API_KEY}&country=ru&language=ru'
    response = requests.get(url).json()
    keys = response["results"]

    for i in range(len(keys)):
        article_info = (
            f'*Название статьи:* {keys[i]["title"]}\n'
            f'*Ссылка на источник:* {keys[i]["link"]}\n'
            f'*Автор новостной статьи:* {keys[i]["creator"]}\n'
            f'*Дата публикации:* {keys[i]["pubDate"]}\n'
            f'Категория: {keys[i]["category"]}\n'
        )
        poster = keys[i]["image_url"]
        return article_info, poster
    else:
        return "Новостей по ключевому слову не найдено!"


def latest_news_subscription(*message):
    url = f'https://newsdata.io/api/1/latest?apikey={NEWS_API_KEY}&country=ru&language=ru'
    response = requests.get(url).json()
    keys = response["results"]

    for i in range(len(keys)):
        if keys[i]["category"] == ["sports" if sports is True else False] or keys[i]["category"] == ["sports" if sports is True else False] or:
            article_info = (
                f'*Название статьи:* {keys[i]["title"]}\n'
                f'*Ссылка на источник:* {keys[i]["link"]}\n'
                f'*Автор новостной статьи:* {keys[i]["creator"]}\n'
                f'*Дата публикации:* {keys[i]["pubDate"]}\n'
                f'Категория: {keys[i]["category"]}\n'
            )
            poster = keys[i]["image_url"]
            return article_info, poster
        else:
            return "Свежих новостей нет!"


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "😎Привет! Я бот новостей.😎\n"
                                      "Выбери нужный пункт меню:\n", reply_markup=main_menu())


@bot.message_handler(func=lambda message: message.text == "Подписаться на темы")
def subscription(message):
    bot.send_message(message.chat.id, "Выбери темы для подписки:\n", reply_markup=main_menu_subscription())


@bot.message_handler(func=lambda message: message.text == "Получить последние новости")
def search_article(message):
    try:
        article_info, poster = latest_news()
        if poster and poster != "null":
            bot.send_photo(message.chat.id, poster, caption=article_info, parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, article_info, parse_mode="Markdown")
    except:
        bot.send_message(message.chat.id, "Свежих новостей нет!", parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == "Получить новости по ключевому слову")
def handle_buttons(message):
    bot.send_message(message.chat.id, "Введите ключевое слово:")
    bot.register_next_step_handler(message, send_news)


def send_news(message):
    news = message.text
    bot.send_message(message.chat.id, key_word_news(news))


@bot.message_handler(func=lambda message: message.text == 'Назад↩️')
def start(message):
    bot.send_message(message.chat.id, 'Главное меню:', reply_markup=main_menu())


@bot.message_handler(func=lambda message: message.text == "Подписаться на темы")
def handle_buttons(message):
    bot.send_message(message.chat.id, "Выбирите темы для подписки:")
    bot.register_next_step_handler(message, send_news_subscriptions)


def send_news_subscriptions(message):
    subscriptions = [message.text]
    if "Наука" in subscriptions:
        science = True
    else:
        science = False
    if "Музыка" in subscriptions:
        music = True
    else:
        music = False
    if "Технологии" in subscriptions:
        technology = True
    else:
        technology = False
    if "Спорт" in subscriptions:
        sports = True
    else:
        sports = False
    if "Экономика" in subscriptions:
        economics = True
    if "Политика" in subscriptions:
        politics = True
    bot.send_message(message.chat.id, latest_news_subscription(subscriptions))





bot.polling()

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


import re
import schedule
import time
from datetime import date, timedelta
import telebot
import requests
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


BOT_API = "7770590397:AAHBSzmBrZLiZxYe5JJHTh-2QvTm2K1I3r8"
NEWS_API_KEY = "pub_740976a50713043bac6ec9aa65409f1ec42e6"

bot = telebot.TeleBot(BOT_API)

today = date.today()
yesterday = today - timedelta(days=1)
formatted_date_today = today.strftime("%Y-%m-%d")
formatted_date_yesterday = yesterday.strftime("%Y-%m-%d")


def main_menu():
    markup = ReplyKeyboardMarkup(row_width=2)
    button_1 = KeyboardButton("⏱Получить последние новости")
    button_2 = KeyboardButton("🗝Получить новости по ключевому слову")
    button_3 = KeyboardButton("✅Подписаться на темы")
    button_4 = KeyboardButton("❌Отписаться от тем")
    button_5 = KeyboardButton("📬Получить новости по подписке")
    button_6 = KeyboardButton("🟢Вкл автоматическую отправку новостей")
    button_7 = KeyboardButton("❓Информация/Мои подписки")
    button_8 = KeyboardButton("🔴Выкл автоматическую отправку новостей")
    markup.add(button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8)
    return markup


def main_menu_subscription_on():
    markup = ReplyKeyboardMarkup(row_width=3)
    button_1 = KeyboardButton("🔝ТОП новости✅")
    button_2 = KeyboardButton("💃Развлечение✅")
    button_3 = KeyboardButton("💰Бизнес✅")
    button_4 = KeyboardButton("⚽Спорт✅")
    button_5 = KeyboardButton("📈Экономика✅")
    button_6 = KeyboardButton("🇷🇺Политика✅")
    button_7 = KeyboardButton("🧬Технологии✅")
    button_8 = KeyboardButton("🌍Мир✅")
    markup.add(button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8)
    return markup


def main_menu_subscription_off():
    markup = ReplyKeyboardMarkup(row_width=3)
    button_1 = KeyboardButton("🔝ТОП новости❌")
    button_2 = KeyboardButton("💃Развлечение❌")
    button_3 = KeyboardButton("💰Бизнес❌")
    button_4 = KeyboardButton("⚽Спорт❌")
    button_5 = KeyboardButton("📈Экономика❌")
    button_6 = KeyboardButton("🇷🇺Политика❌")
    button_7 = KeyboardButton("🧬Технологии❌")
    button_8 = KeyboardButton("🌍Мир❌")
    markup.add(button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8)
    return markup


def escape_markdown(text):
    escape_chars = r'\_*[]()~`>#+-=|{}.!'
    return re.sub(f'([{re.escape(escape_chars)}])', r'\\\1', text)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "📰*Привет! Я бот новостей.*📰\n"
                                      "*Сделайте выбор:🤔\n*", reply_markup=main_menu(), parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == "✅Подписаться на темы")
def subscription(message):
    bot.send_message(message.chat.id, "Выбери темы для подписки:\n", reply_markup=main_menu_subscription_on())


@bot.message_handler(func=lambda message: message.text == "❌Отписаться от тем")
def subscription(message):
    global list_subscriptions
    global list_schedule
    not_subscription = [False, False, False, False, False, False, False, False]
    if not_subscription == list_subscriptions:
        bot.send_message(message.chat.id, '*Сначала надо подписаться на темы!*😉', reply_markup=main_menu(),
                         parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, "Выбери темы для подписки:\n", reply_markup=main_menu_subscription_off())


list_schedule = False


@bot.message_handler(func=lambda message: message.text == "🟢Вкл автоматическую отправку новостей")
def auto_news(message):
    global list_subscriptions
    global list_schedule
    not_subscription = [False, False, False, False, False, False, False, False]
    if not_subscription == list_subscriptions:
        bot.send_message(message.chat.id, '*Сначала надо подписаться на темы!*😉', reply_markup=main_menu(), parse_mode="Markdown")
    else:
        if list_schedule is False:
            list_schedule = True
            bot.send_message(message.chat.id, f'*Автоматическая отправка новостей включена!*🟢', parse_mode="Markdown")
            # Планирование задачи
            schedule.every(30).seconds.do(time_schedule)  # Каждые 20 секунд
            # schedule.every().day.at("9:00").do(my_function)  # Каждый день в 10:00
            while list_schedule:
                schedule.run_pending()
                time.sleep(1)
        else:
            bot.send_message(message.chat.id, '*Уже включена!*🙄', parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == "🔴Выкл автоматическую отправку новостей")
def auto_news(message):
    global list_schedule
    if list_schedule is True:
        list_schedule = False
        bot.send_message(message.chat.id, f'*Автоматическая отправка новостей отключена!*🔴', parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, '*Уже выключена!*🙄', parse_mode="Markdown")


def time_schedule():
    global list_subscriptions
    top, entertainment, business, sports, economics, politics, technology, world = list_subscriptions
    url = f'https://newsdata.io/api/1/latest?apikey={NEWS_API_KEY}'
    response = requests.get(url).json()
    keys = response["results"]
    not_keys = []
    count = 0
    not_subscription = [False, False, False, False, False, False, False, False]
    if not_subscription == list_subscriptions:
        bot.send_message(chat_id="484938227", text="*Вы еще не подписались ни на одну тему!*😞", reply_markup=main_menu(), parse_mode="Markdown")
    else:
        if keys == not_keys:
            bot.send_message(chat_id="484938227", text="*Новостей по подписке не найдено!*😞", reply_markup=main_menu(),
                             parse_mode="Markdown")
        else:
            for i in range(len(keys)):
                try:
                    if keys[i]["category"] == ["top" if top is True else False] \
                            or keys[i]["category"] == ["entertainment" if entertainment is True else False] \
                            or keys[i]["category"] == ["business" if business is True else False] \
                            or keys[i]["category"] == ["sports" if sports is True else False] \
                            or keys[i]["category"] == ["economics" if economics is True else False] \
                            or keys[i]["category"] == ["politics" if politics is True else False] \
                            or keys[i]["category"] == ["technology" if technology is True else False] \
                            or keys[i]["category"] == ["world" if world is True else False]:
                        count += 1
                        article_info = (
                            f'✒️Название статьи: {keys[i]["title"]}\n'
                            f'🔗Ссылка на источник: {keys[i]["link"]}\n'
                            f'©️Автор новостной статьи: {keys[i]["creator"]}\n'
                            f'🗓️Дата публикации: {keys[i]["pubDate"]}\n'
                            f'📌Категория: {keys[i]["category"]}\n'
                        )
                        poster = keys[i]["image_url"]
                        if poster and poster is not None:
                            bot.send_photo(chat_id="484938227", photo=poster, caption=article_info)
                        else:
                            bot.send_message(chat_id="484938227", text=article_info)
                except Exception as e:
                    print(e)
                    continue
    if count == 0:
        bot.send_message(chat_id="484938227", text="*Новостей по подписке не найдено!*😞😞😞", reply_markup=main_menu(), parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == "⏱Получить последние новости")
def handle_buttons(message):
    url = f'https://newsdata.io/api/1/latest?apikey={NEWS_API_KEY}'
    response = requests.get(url).json()
    keys = response["results"]
    not_keys = []
    count = 0
    if keys == not_keys:
        bot.send_message(message.chat.id, "*Последних новостей нет!*😞", parse_mode="Markdown")
    else:
        for i in range(len(keys)):
            try:
                dt_string = keys[i]["pubDate"]
                if dt_string[:10] == formatted_date_today or dt_string[:10] == formatted_date_yesterday:
                    count += 1
                    article_info = (
                        f'✒️Название статьи: {keys[i]["title"]}\n'
                        f'🔗Ссылка на источник: {keys[i]["link"]}\n'
                        f'©️Автор новостной статьи: {keys[i]["creator"]}\n'
                        f'🗓️Дата публикации: {keys[i]["pubDate"]}\n'
                        f'📌Категория: {keys[i]["category"]}\n'
                    )
                    poster = keys[i]["image_url"]
                    if poster and poster is not None:
                        bot.send_photo(message.chat.id, poster, caption=article_info)
                    else:
                        bot.send_message(message.chat.id, article_info)
            except Exception as e:
                print(e)
                continue
    if count == 0:
        bot.send_message(message.chat.id, "*Последних новостей нет!*😞", parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == "🗝Получить новости по ключевому слову")
def handle_buttons(message):
    bot.send_message(message.chat.id, "Введите ключевое слово:")
    bot.register_next_step_handler(message, send_news)


def send_news(message):
    key_word = message.text
    url = f'https://newsdata.io/api/1/latest?q={key_word}&apikey={NEWS_API_KEY}'
    response = requests.get(url).json()
    keys = response["results"]
    not_keys = []
    if keys == not_keys:
        bot.send_message(message.chat.id, "*Новостей по ключевому слову не найдено!*😞", reply_markup=main_menu(), parse_mode="Markdown")
    else:
        for i in range(len(keys)):
            try:
                article_info = (
                    f'✒️Название статьи: {keys[i]["title"]}\n'
                    f'🔗Ссылка на источник: {keys[i]["link"]}\n'
                    f'©️Автор новостной статьи: {keys[i]["creator"]}\n'
                    f'🗓️Дата публикации: {keys[i]["pubDate"]}\n'
                    f'📌Категория: {keys[i]["category"]}\n'
                )
                poster = keys[i]["image_url"]
                if poster and poster is not None:
                    bot.send_photo(message.chat.id, poster, caption=article_info)
                else:
                    bot.send_message(message.chat.id, article_info)
            except Exception as e:
                print(e)
                continue


@bot.message_handler(func=lambda message: message.text == "📬Получить новости по подписке")
def give_news_subscription(message):
    global list_subscriptions
    top, entertainment, business, sports, economics, politics, technology, world = list_subscriptions
    url = f'https://newsdata.io/api/1/latest?apikey={NEWS_API_KEY}'
    response = requests.get(url).json()
    keys = response["results"]
    not_keys = []
    count = 0
    not_subscription = [False, False, False, False, False, False, False, False]
    if not_subscription == list_subscriptions:
        bot.send_message(message.chat.id, "*Вы еще не подписались ни на одну тему!*😞", parse_mode="Markdown")
    else:
        if keys == not_keys:
            bot.send_message(message.chat.id, "*Новостей по подписке не найдено!*😞", reply_markup=main_menu(),
                             parse_mode="Markdown")
        else:
            for i in range(len(keys)):
                try:
                    if keys[i]["category"] == ["top" if top is True else False] \
                            or keys[i]["category"] == ["entertainment" if entertainment is True else False] \
                            or keys[i]["category"] == ["business" if business is True else False] \
                            or keys[i]["category"] == ["sports" if sports is True else False] \
                            or keys[i]["category"] == ["economics" if economics is True else False] \
                            or keys[i]["category"] == ["politics" if politics is True else False] \
                            or keys[i]["category"] == ["technology" if technology is True else False] \
                            or keys[i]["category"] == ["world" if world is True else False]:
                        count += 1
                        article_info = (
                            f'✒️Название статьи: {keys[i]["title"]}\n'
                            f'🔗Ссылка на источник: {keys[i]["link"]}\n'
                            f'©️Автор новостной статьи: {keys[i]["creator"]}\n'
                            f'🗓️Дата публикации: {keys[i]["pubDate"]}\n'
                            f'📌Категория: {keys[i]["category"]}\n'
                        )
                        poster = keys[i]["image_url"]
                        if poster and poster is not None:
                            bot.send_photo(message.chat.id, poster, caption=article_info)
                        else:
                            bot.send_message(message.chat.id, article_info)
                except Exception as e:
                    print(e)
                    continue
        if count == 0:
            bot.send_message(message.chat.id, "*Новостей по подписке не найдено!*😞", reply_markup=main_menu(), parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == '🔝ТОП новости✅')
def start(message):
    global list_subscriptions
    if list_subscriptions[0] is False:
        list_subscriptions[0] = True
        bot.send_message(message.chat.id, f'*Подписка успешно подключена!*🔔', reply_markup=main_menu(), parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, '*Вы уже подписаны!🤷‍♂️*', reply_markup=main_menu(), parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == '🔝ТОП новости❌')
def start(message):
    global list_subscriptions
    global list_schedule
    if list_schedule is True:
        bot.send_message(message.chat.id, f'*Сначала надо выкл авто рассылку!*☝', reply_markup=main_menu(),
                         parse_mode="Markdown")
    else:
        if list_subscriptions[0] is True:
            list_subscriptions[0] = False
            bot.send_message(message.chat.id, f'*Подписка успешно отключена!*🔕', reply_markup=main_menu(), parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, '*Подписки нету!*🙄', reply_markup=main_menu(), parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == '💃Развлечение✅')
def start(message):
    global list_subscriptions
    if list_subscriptions[1] is False:
        list_subscriptions[1] = True
        bot.send_message(message.chat.id, f'*Подписка успешно подключена!*🔔', reply_markup=main_menu(), parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, '*Вы уже подписаны!🤷‍♂️*', reply_markup=main_menu(), parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == '💃Развлечение❌')
def start(message):
    global list_subscriptions
    global list_schedule
    if list_schedule is True:
        bot.send_message(message.chat.id, f'*Сначала надо выкл авто рассылку!*☝', reply_markup=main_menu(),
                         parse_mode="Markdown")
    else:
        if list_subscriptions[1] is True:
            list_subscriptions[1] = False
            bot.send_message(message.chat.id, f'*Подписка успешно отключена!*🔕', reply_markup=main_menu(), parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, '*Подписки нету!*🙄', reply_markup=main_menu(), parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == '💰Бизнес✅')
def start(message):
    global list_subscriptions
    if list_subscriptions[2] is False:
        list_subscriptions[2] = True
        bot.send_message(message.chat.id, f'*Подписка успешно подключена!*🔔', reply_markup=main_menu(), parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, '*Вы уже подписаны!🤷‍♂️*', reply_markup=main_menu(), parse_mode="Markdown")



@bot.message_handler(func=lambda message: message.text == '💰Бизнес❌')
def start(message):
    global list_subscriptions
    global list_schedule
    if list_schedule is True:
        bot.send_message(message.chat.id, f'*Сначала надо выкл авто рассылку!*☝', reply_markup=main_menu(),
                         parse_mode="Markdown")
    else:
        if list_subscriptions[2] is True:
            list_subscriptions[2] = False
            bot.send_message(message.chat.id, f'*Подписка успешно отключена!*🔕', reply_markup=main_menu(), parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, '*Подписки нету!*🙄', reply_markup=main_menu(), parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == '⚽Спорт✅')
def start(message):
    global list_subscriptions
    if list_subscriptions[3] is False:
        list_subscriptions[3] = True
        bot.send_message(message.chat.id, f'*Подписка успешно подключена!*🔔', reply_markup=main_menu(), parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, '*Вы уже подписаны!🤷‍♂️*', reply_markup=main_menu(), parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == '⚽Спорт❌')
def start(message):
    global list_subscriptions
    global list_schedule
    if list_schedule is True:
        bot.send_message(message.chat.id, f'*Сначала надо выкл авто рассылку!*☝', reply_markup=main_menu(),
                         parse_mode="Markdown")
    else:
        if list_subscriptions[3] is True:
            list_subscriptions[3] = False
            bot.send_message(message.chat.id, f'*Подписка успешно отключена!*🔕', reply_markup=main_menu(), parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, '*Подписки нету!*🙄', reply_markup=main_menu(), parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == '📈Экономика✅')
def start(message):
    global list_subscriptions
    if list_subscriptions[4] is False:
        list_subscriptions[4] = True
        bot.send_message(message.chat.id, f'*Подписка успешно подключена!*🔔', reply_markup=main_menu(), parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, '*Вы уже подписаны!🤷‍♂️*', reply_markup=main_menu(), parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == '📈Экономика❌')
def start(message):
    global list_subscriptions
    global list_schedule
    if list_schedule is True:
        bot.send_message(message.chat.id, f'*Сначала надо выкл авто рассылку!*☝', reply_markup=main_menu(),
                         parse_mode="Markdown")
    else:
        if list_subscriptions[4] is True:
            list_subscriptions[4] = False
            bot.send_message(message.chat.id, f'*Подписка успешно отключена!*🔕', reply_markup=main_menu(), parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, '*Подписки нету!*🙄', reply_markup=main_menu(), parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == '🇷🇺Политика✅')
def start(message):
    global list_subscriptions
    if list_subscriptions[5] is False:
        list_subscriptions[5] = True
        bot.send_message(message.chat.id, f'*Подписка успешно подключена!*🔔', reply_markup=main_menu(), parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, '*Вы уже подписаны!🤷‍♂️*', reply_markup=main_menu(), parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == '🇷🇺Политика❌')
def start(message):
    global list_subscriptions
    global list_schedule
    if list_schedule is True:
        bot.send_message(message.chat.id, f'*Сначала надо выкл авто рассылку!*☝', reply_markup=main_menu(),
                         parse_mode="Markdown")
    else:
        if list_subscriptions[5] is True:
            list_subscriptions[5] = False
            bot.send_message(message.chat.id, f'*Подписка успешно отключена!*🔕', reply_markup=main_menu(), parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, '*Подписки нету!*🙄', reply_markup=main_menu(), parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == '🧬Технологии✅')
def start(message):
    global list_subscriptions
    if list_subscriptions[6] is False:
        list_subscriptions[6] = True
        bot.send_message(message.chat.id, f'*Подписка успешно подключена!*🔔', reply_markup=main_menu(), parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, '*Вы уже подписаны!🤷‍♂️*', reply_markup=main_menu(), parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == '🧬Технологии❌')
def start(message):
    global list_subscriptions
    global list_schedule
    if list_schedule is True:
        bot.send_message(message.chat.id, f'*Сначала надо выкл авто рассылку!*☝', reply_markup=main_menu(),
                         parse_mode="Markdown")
    else:
        if list_subscriptions[6] is True:
            list_subscriptions[6] = False
            bot.send_message(message.chat.id, f'*Подписка успешно отключена!*🔕', reply_markup=main_menu(), parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, '*Подписки нету!*🙄', reply_markup=main_menu(), parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == '🌍Мир✅')
def start(message):
    global list_subscriptions
    if list_subscriptions[7] is False:
        list_subscriptions[7] = True
        bot.send_message(message.chat.id, f'*Подписка успешно подключена!*🔔', reply_markup=main_menu(), parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, '*Вы уже подписаны!🤷‍♂️*', reply_markup=main_menu(), parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == '🌍Мир❌')
def start(message):
    global list_subscriptions
    global list_schedule
    if list_schedule is True:
        bot.send_message(message.chat.id, f'*Сначала надо выкл авто рассылку!*☝', reply_markup=main_menu(),
                         parse_mode="Markdown")
    else:
        if list_subscriptions[7] is True:
            list_subscriptions[7] = False
            bot.send_message(message.chat.id, f'*Подписка успешно отключена!*🔕', reply_markup=main_menu(), parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, '*Подписки нету!*🙄', reply_markup=main_menu(), parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == "❓Информация/Мои подписки")
def handle_buttons(message):
    global list_schedule
    bot.send_message(message.chat.id, f'*Этот Бот создан мною в целях получения опыта в программировании на языке*\n'
                                      f'*Python. По всем вопросам сотрудничества обращаться по т. 8-953-749-0060 Олег*\n'
                                      f'\n', parse_mode="Markdown")
    bot.send_message(message.chat.id, f'*Ваши подписки:*\n', parse_mode="Markdown")
    info_subscription = info_help_subscription()
    if info_subscription is False:
        bot.send_message(message.chat.id, f'*Подписок нет!😟*\n', parse_mode="Markdown")
    else:
        for i in range(len(info_subscription)):
            bot.send_message(message.chat.id, f'*{info_subscription[i][0]} - {info_subscription[i][1]}*', parse_mode="Markdown")
    if list_schedule is False:
        bot.send_message(message.chat.id, f'*Автоматическая рассылка отключена!😟*\n', reply_markup=main_menu(), parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, f'*Автоматическая рассылка включена!✅*\n', reply_markup=main_menu(), parse_mode="Markdown")


list_subscriptions = [False, False, False, False, False, False, False, False]


def info_help_subscription():
    global list_subscriptions
    global list_schedule
    title_subscriptions = ["ТОП новости", "Развлечение", "Бизнес", "Спорт", "Экономика", "Политика", "Технологии",
                           "Мир"]
    not_subscription = [False, False, False, False, False, False, False, False]
    info_subscription = []
    if list_subscriptions == not_subscription:
        return False
    else:
        for i, j in zip(title_subscriptions, list_subscriptions):
            if j is True:
                info_subscription.append((i, "✅"))
        return info_subscription


@bot.message_handler(func=lambda message: True)
def unknown_command(message):
    bot.send_message(message.chat.id, "*Я не понимаю эту команду!*🙄", reply_markup=main_menu(), parse_mode="Markdown")


bot.polling()
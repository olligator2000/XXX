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


url = f'https://newsdata.io/api/1/latest?apikey={NEWS_API_KEY}'
response = requests.get(url).json()
keys = response["results"]

sports = True
for i in range(len(keys)):
    dt_string = keys[i]["pubDate"]

    if keys[i]["category"] == ["economics"] or keys[i]["category"] == ["business"] or keys[i]["category"] == ["entertainment"] or keys[i]["category"] == ["politics"] or keys[i]["category"] == ["sports"]:
        article_info = (
            f'Название статьи: {keys[i]["title"]}\n'
            f'Ссылка на источник: {keys[i]["link"]}\n'
            f'Автор новостной статьи: {keys[i]["creator"]}\n'
            f'Дата публикации: {keys[i]["pubDate"]}\n'
            f'Категория: {keys[i]["category"]}\n'
        )
        poster = keys[i]["image_url"]
        print(article_info, poster)


# for i in range(len(keys)):
#     dt_string = keys[i]["pubDate"]
#     if dt_string[:10] == formatted_date_today or dt_string[:10] == formatted_date_yesterday:
#         list_article_info = {}
#         article_info = (
#             f'*Название статьи:* {keys[i]["title"]}\n'
#             f'*Ссылка на источник*: {keys[i]["link"]}\n'
#             f'*Автор новостной статьи: {keys[i]["creator"]}\n'
#             f'*Дата публикации:* {keys[i]["pubDate"]}\n'
#         )
#         poster = response.get("image_url", "")
#         list_article_info[poster] = article_info
#
# print(list_article_info)
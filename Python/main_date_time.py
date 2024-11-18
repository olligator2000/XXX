
#from datetime import date

# d = date(2024, 11, 12)
# d_2 = date(year=2024, day=12, month=11)
#
#
# print(d)
# print(type(d_2))
########################################################
# from datetime import date
# today = date.today() - 1    #Вывести сегодняшнюю дату
#
# print(today)

########################################################
# from datetime import date
#
# d_1 = date(year=2024, day=12, month=11)
# d_2 = date(year=2026, day=7, month=5)
#
# delta = d_2 - d_1     #Находим разницу во времени
#
# print(delta.days)

########################################################
########################################################
# from datetime import time
#
# t = time(hour=12, minute=20, second=12)
#
# print(t)
# print(type(t))

########################################################
########################################################

# from datetime import datetime
#
# time_now = datetime.now()
#
# print(time_now.hour)
# print(type(time_now))

########################################################
# from datetime import datetime
#
# dt = datetime(year=2024, month=12, day=4, hour=22, minute=32, second=12)
#
# print(dt)

########################################################

# from datetime import datetime
#
# print(datetime.now().isoweekday())      #Выводит день недели от 1 до 7

######################################################## ВЫВОДИМ В СТРОКУ ДАТУ УДОБНО ЧИТАБЕЛЬНУЮ
# from datetime import datetime
# today = datetime.today()
# print(today)
#
# formatted = today.strftime("%d.%m.%Y %H:%M")      #Переводим из даты в строку
# print(formatted)
# print(type(formatted))

########################################################
# from datetime import datetime
# dt_string = input("Введите дату в формате ГГГГ-ММ-ДД ЧЧ:ММ: ")
# print(dt_string)
#
# dt = datetime.strptime(dt_string, "%Y-%m-%d %H:%M")     #Парсим ,strptime переводим из строки в дату
# print(dt)
# print(type(dt))

########################################################
#
# from datetime import timedelta, datetime
#
# delta = timedelta(weeks=4, days=15, hours=6)
# today = datetime.today()
#
# print(today + delta)

######################################################## 1
# Напишите программу, которая определяет день недели для заданной даты
# from datetime import datetime
# dt_string = input("Введите дату в формате ГГГГ-ММ-ДД : ")
# dt = datetime.strptime(dt_string, "%Y-%m-%d")
# day = dt.strftime("%A")
# print(day)

######################################################## 2
# Напишите программу, которая находит разницу в днях между двумя заданными датами
# from datetime import datetime
# dt_string_1 = input("Введите 1-ю дату в формате ГГГГ-ММ-ДД : ")
# dt_string_2 = input("Введите 2-ю дату в формате ГГГГ-ММ-ДД : ")
# dt_1 = datetime.strptime(dt_string_1, "%Y-%m-%d")
# dt_2 = datetime.strptime(dt_string_2, "%Y-%m-%d")
# if dt_1 > datetime.now() or dt_1 == datetime.now() and dt_2 < datetime.now():
#     print(dt_1 - dt_2)
# else:
#     print(dt_2 - dt_1)

######################################################## 3
# Напишите программу, которая определяет количество дней до конца текущего месяца
from datetime import datetime, date
dt_string = input("Введите дату в формате ДД-ММ-ГГГГ : ")
dt = datetime.strptime(dt_string, "%d-%m-%Y")

if dt.month == 12:
    dt_2 = datetime(day=1, month=dt.month - 11, year=dt.year + 1)
else:
    dt_2 = datetime(day=1, month=dt.month + 1, year=dt.year)

print(dt_2 - dt)

######################################################## 4
# Напишите программу, которая определяет возраст человека по его дате рождения
# from datetime import datetime
# dt_string = input("Введите дату рождения в формате ГГГГ-ММ-ДД : ")
# dt = datetime.strptime(dt_string, "%Y-%m-%d")
# today = datetime.now()
# year = today.year - dt.year
# if today.day < dt.day or today.month <= dt.month:
#     year -= 1
# print(year)

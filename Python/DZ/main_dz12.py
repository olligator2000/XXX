############################################### 1
# Реализуйте расчет дня недели для дня рождения. Пользователь вводит месяц и день, а получает файл, содержащий
# # дни недели, на которые приходится его день рождения в ближайшие 20 лет.
from datetime import datetime, timedelta

hb_date = input("Введите дату в формате ДД-ММ : ")
today = datetime.now()
year_str = today.year                               #Заносим в переменную текущий год, так как года нет в hb_date
hb_date_end = hb_date + "-" + str(year_str)         #Создаем полную дату день-месяц-год
dt = datetime.strptime(hb_date_end, "%d-%m-%Y")
print("Дата: ", dt.strftime("%d.%m"))


def visokos_year(year):                                # Вычисляем (не)високосный год
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 366
    else:
        return 365


counts = 0

for i in range(0, 20):                                 # Диапозон 20 лет
    delta = timedelta(days=visokos_year(today.year + i))  # Находим основную дельту
    if delta != timedelta(days=365):                           # Корректируем дату на -1 день в високосный год
        dt = dt + delta - timedelta(days=1)
        day = dt.strftime("%A")
        print(dt.strftime("%d.%m.%Y"), "-", day)

    if delta == timedelta(days=365):
        if counts == 2:                             # Корректируем дату на +1 день перед високосным годом
            dt = dt + delta + timedelta(days=1)
            day = dt.strftime("%A")
            print(dt.strftime("%d.%m.%Y"), "-", day)
            counts = 0
        else:
            dt = dt + delta
            day = dt.strftime("%A")
            counts += 1
            print(dt.strftime("%d.%m.%Y"), "-", day)

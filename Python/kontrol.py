########################################################1 ПРОСТЫЕ ЗАДАЧИ
# Напишите программу, которая проверяет, является ли введенное число четным или нечетным
# number = int(input("Введите число :"))
# if number % 2 == 0:
#     print("Число является четным")
# else:
#     print("Число является нечетным")
from itertools import count

########################################################2
# Напишите программу, которая выводит на экран таблицу умножения от 1 до 10 для заданного числа.
# number = int(input("Введите число :"))
# for i in range(1, 11):
#     print(i * number, end=" ")

########################################################3
# Напишите программу, которая проверяет, является ли введенное слово палиндромом
# text = input("Введите слово :")
# if text.lower() == text.lower()[::-1]:
#     print("Слово является палиндромом")
# else:
#     print("Слово не является палиндромом")

########################################################4
# Напишите программу, которая находит сумму всех элементов в списке.
# numbers = [2, 6, 9, 1]
# summa = 0
# for i in numbers:
#     summa += i
# print(f"Сумма чисел равна {summa}")

########################################################5
# Напишите программу, которая выводит на экран все простые числа от 1 до 100
# for i in range(1, 101):
#     if i == 1 or i == 2:
#         continue
#     for a in range(2, i):
#         if i % a == 0:
#             break
#     else:
#         print(i)

######################################################## 1 СРЕДНИЕ ЗАДАЧИ
# Напишите программу, которая запрашивает у пользователя радиус круга и выводит его площадь и длину окружности. (4 балла)
# r = int(input("Введите радиус :"))
# print(f"Площадь круга = {3.14 * r * r} \n"
#       f"Длина окружности = {2 * 3.14 * r}")

######################################################## 2
# Напишите программу, которая принимает на вход строку и выводит количество гласных букв в ней
# text = input("Введите строку :")
# symbol = "qwrtpsdfghjklzxcvbnm"
# count1 = 0
# for i in text:
#     if symbol.count(i):
#         count1 += 1
# print(f"Количество гласных букв = {count1}")

######################################################## 3
# Напишите программу, которая считывает список чисел и выводит наибольшее и наименьшее число в списке
# numbers = [2, 6, 8, 20, 3, 12, -3]
# print(f"Наибольшее число = {max(numbers)} \n"
#       f"Наименьшее число равно {min(numbers)}")

######################################################## 4
# Напишите программу, которая принимает на вход строку и выводит ее в обратном порядке.
# text = input("Введите строку :")
# print(text[::-1])

######################################################## 5
# # Напишите программу, которая запрашивает у пользователя длины трех сторон треугольника и определяет, является ли
# # треугольник прямоугольным.
# a = float(input("Введите первый отрезок: "))
# b = float(input("Введите второй отрезок: "))
# c = float(input("Введите третий отрезок: "))
# if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2:
#     print("Треугольник прямоугольный")
# else:
#     print("Треугольник не прямоугольный")

######################################################## 1 Сложные задачи
# Напишите программу, которая принимает на вход строку и определяет, является ли она панграммой (строкой, содержащей все буквы алфавита).
# text = input("Введите строку :")
# symbol = "qwertyuiopasdfghjklzxcvbnm"
# count1 = 0
# end_text = []
# for i in text:
#     if symbol.count(i):
#         if i not in end_text:
#             end_text.append(i)
#             count1 += 1
# if len(end_text) >= 26:
#     print("Строка является панграммой")
# else:
#     print("Строка не является панграммой")

######################################################## 2 НЕ СДЕЛАЛ!!!!!!!!!!!!!!!
# Напишите программу, которая принимает на вход список и выводит
# наиболее часто встр   ечающийся элемент и его количество в списке.
# number_list = []
# while True:
#     number = input(f"Введите число: ")
#     if number == 'стоп':
#         break
#     number_list.append(int(number))
# end_list = number_list[0]
# count_index = number_list.index(end_list)
# for i in number_list:
#     if number_list > count_index:
#         end_list = i
#         count_index = number_list.index(i)
# print(end_list, count_index)



######################################################## 3
# Напишите программу, которая принимает на вход список чисел и сортирует его по убыванию.
# number_list = []
# while True:
#     number = input(f"Введите элемент: ")
#     if number == 'стоп':
#         break
#     number_list.append(int(number))
# number_list.sort(reverse=True)
# print(number_list)

######################################################## 4
# Напишите программу, которая принимает на вход две строки и определяет,
# является ли одна из них анаграммой другой (строкой, составленной из тех же букв
# в другом порядке).
# text1 = input("Введите 1 строку :").lower()
# text2 = input("Введите 2 строку :").lower()
# count1 = 0
# for i in text1:
#     if text2.count(i):
#         count += 1
# if count1 == len(text1):
#     print("Строка является анаграмой")
# else:
#     print("Строка НЕ является анаграмой")

######################################################## 5

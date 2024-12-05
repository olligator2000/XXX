##################################################### 1
# Напишите функцию, которая отображает на экран форматированный текст, указанный ниже:
# “Don't let the noise of others' opinions drown out your own inner voice.” Steve Jobs
# def jobs():
#     print("“Don't let the noise of others' opinions drown out your own inner voice.” Steve Jobs")
# print(jobs())

##################################################### 2
# Напишите функцию, которая принимает два числа в качестве параметра и отображает все нечетные числа между ними.
# def odd(a, b):
#     list1 = [i for i in range(a, b) if i % 2 == 1]
#     return list1
# print(odd(1, 10))

##################################################### 3
# Напишите функцию, которая отображает горизонтальную или вертикальную линию из некоторого символа.
# Функция принимает в качестве параметра: длину линии,направление, символ
# def lines(length, direction, symbol):
#     line = ""
#     if direction == "-":
#         for i in range(0, length):
#             line += symbol
#         return line
#     elif direction == "|":
#         for j in range(0, length):
#             print(symbol)
#     else:
#         return False
# print(lines(5,"-","*"))

##################################################### 4
# Напишите функцию, которая возвращает максимальное из четырёх чисел. Числа передаются в качестве параметров
# def maksi(a, b, c, d):
#     return max(a, b, c, d)
# print(maksi(4,10,2,3))

##################################################### 5
# Напишитефункцию, которая возвращает сумму чисел в указанном диапазоне. Границы диапазона передаются в качестве параметров
# def sum_num(mi, ma):
#     summa = 0
#     for i in range(mi, ma + 1):
#         summa += i
#     return summa
# print(sum_num(2,4))
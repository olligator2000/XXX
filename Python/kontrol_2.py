############################################# 1
# Напишите функцию, которая принимает на вход список функций
# и список аргументов. Функция должна последовательно применять каждую
# функцию из списка к соответствующему аргументу и возвращать список
# результатов
# import math
# z = [1, 2, 3]
#
# list_func = [lambda d: d**d, lambda d: d*d, lambda d: d+d]
#
# def funcs(funks, arguments):
#     return [func(arg) for func, arg in zip(funks, arguments)]
#
# print(funcs(list_func, z))

############################################# 2 НЕ РЕШИЛ!!!!!!!!!!!!!!!!!!!!
# Реализуйте функцию, которая принимает на вход другую
# функцию и список аргументов, и возвращает функцию, которая будет
# вызывать исходную функцию с аргументами, умноженными на заданное
# число
#
# n = [1, 2, 3]
# def f_1(func, arg):
#
#     def f_2(x):
#         for i in x:
#             f = i * 2
#         return f
#     return f_2()
#
# print(f_1(lambda x,y,z: x+x+z, n))

############################################# 3
# Напишите функцию, которая принимает переменное количество
# аргументов и возвращает их среднее арифметическое. Функция должна
# корректно работать как с числами, так и с последовательностями чисел.

# list_1 = [1, 2, 3, 4, 3, 4, 5, 6]
# def f_1(*args):
#     s = sum(list_1)
#     otvet = s / len(list_1)
#     return otvet
#
# print(f_1(list_1))

############################################# 4
# Создайте функцию, которая принимает на вход список слов и
# возвращает словарь, где ключами являются первые буквы слов, а значениями
# - списки слов, начинающихся с этой буквы
# texts = ['oleg', 'alex', 'mary', 'dedy', 'bob']
#
# def f_1(text):
#     key_1 = []
#     for i in text:
#         key_1.append(i[0])
#     dict_1 = {}
#     for j in range(len(key_1)):
#         key = key_1[j]
#         value = text[j]
#         dict_1[key] = value
#     return dict_1
#
# print(f_1(texts))

############################################# 5
# Напишите функцию, которая принимает на вход список чисел и возвращает список квадратов всех нечетных чисел из исходного списка,
# используя list comprehension и встроенные функции Python.

# numbers = [1, 2, 3, 4, 5, 6, 7]
#
# def f_1(args):
#     s = [i**2 for i in args if i % 2 == 1]
#     return s
#
# print(f_1(numbers))

############################################# 6
# Напишите функцию, которая принимает два множества и возвращает новое множество, содержащее только элементы,
# встречающиеся в обоих исходных множествах

# x = {1, 2, 3, 12, 4, 5, 23, 24}
# y = {23, 2, 3, 11, 4, 6, 7, 5}
# def f_1(a, b):
#     return a & b
#
# print(f_1(x, y))

############################################# 7
# Реализуйте функцию, которая проверяет, является ли одно множество подмножеством другого, без использования стандартных
# операторов для множеств

# x = {1, 2, 3}
# y = {1, 2, 3}
#
# def f_1(a, b):
#     return a.issubset(b)
#
# print(f_1(x, y))

############################################# 8
# Напишите функцию, которая принимает на вход список множеств
# и возвращает пересечение всех множеств в списке.

# x = {1, 2, 3, 12, 4, 5, 23, 24}
# y = {23, 2, 3, 11, 4, 6, 7, 5}
#
# def f_1(a, b):
#     return a | b
#
# print(f_1(x, y))

############################################# 9
# Создайте функцию, которая принимает на вход два множества и
# возвращает новое множество, содержащее только элементы, которые
# встречаются только в одном из исходных множеств

# x = {1, 2, 3, 12, 4, 5, 23, 24}
# y = {23, 2, 3, 11, 4, 6, 7, 5}
#
# def f_1(a, b):
#     return a - b, b - a
#
# print(f_1(x, y))

############################################# 10
# Напишите функцию, которая принимает на вход список множеств
# и возвращает новое множество, содержащее все уникальные элементы из всех
# множеств в списке.

# x = {1, 2, 3, 12, 4, 5, 23, 24}
# y = {23, 2, 3, 11, 4, 6, 7, 5}
#
# def f_1(a, b):
#     return a ^ b
#
# print(f_1(x, y))

############################################# 11
# Напишите функцию, которая принимает на вход словарь и
# возвращает новый словарь, в котором ключи и значения поменяны местами.

# dict_1 = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
# }
#
# def f_1(dicts):
#     new_dict = {}
#     for i, j in dicts.items():
#         key = j
#         volume = i
#         new_dict[key] = volume
#     return new_dict
#
# print(f_1(dict_1))

############################################# 12
# Создайте функцию, которая принимает на вход список словарей и
# возвращает новый словарь, содержащий уникальные ключи из всех словарей
# в списке и списки значений для каждого ключа

# list_dict = [
#     {'oleg': 40, 'alex': 20, 'bob': 24},
#     {'igor': 41, 'bob': 23, 'oleg': 34}
# ]
#
# def f_1(dicts):
#     new_dict = {}
#     for i in dicts:
#         for j in i:
#             if j not in new_dict:
#                 new_dict.update(j)
#     return new_dict
#
# print(f_1(list_dict))

############################################# 13
# Реализуйте функцию, которая принимает на вход словарь и
# возвращает новый словарь, в котором ключи - это первая буква слов, а
# значения - списки слов, начинающихся с этой буквы

texts = {'oleg': 23, 'alex': 44, 'mary':12, 'dedy':33, 'bob':55}

def f_1(text):
    key_1 = []
    for i in text:
        key_1.append(i[0])
    dict_1 = {}
    for j in range(len(key_1)):
        key = key_1[j]
        value = text[j]
        dict_1[key] = value
    return dict_1

print(f_1(texts))
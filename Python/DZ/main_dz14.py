############################################### 1
# Пусть дано множество, которое представляет студентов: students = {"Tom", "Bob", "Sam"}
# И пусть дано множество, которое представляет рабочих: employees = {"Tom", "Bob", "Alex", "Mike"}
# Как видно, некоторые одновременно могут учиться и работать.
# Напишите программу (с помощью разных функций), которая находит:
# - Всех людей в обоих группах
# - Всех людей, которые одновременно и учатся, и работают
# - Всех людей, которые только учатся, но не работают
# - Всех людей, которые либо только учатся, либо только работают, но не одновременно

# students = {"Tom", "Bob", "Sam"}
# employees = {"Tom", "Bob", "Alex", "Mike"}
#
#
# def all_people_in_groups(*set_1):
#     x = set_1[0]
#     for i in set_1[1:]:
#         x = x | i
#     return x
#
#
# def all_people_together_students_and_employees(*set_1):
#     x = set_1[0]
#     for i in set_1[1:]:
#         x = x & i
#     return x
#
#
# def all_people_students(*set_1):
#     x = set_1[0]
#     for i in set_1[1:]:
#         x = x - i
#     return x
#
#
# def all_people_students_or_employees_no_together(*set_1):
#     x = set_1[0]
#     for i in set_1[1:]:
#         x = x - i | i - x
#     return x
#
#
# while True:
#     answer = int(input("Главное меню : \n"
#                        "1 - Найти всех людей в обоих группах \n"
#                        "2 - Найти всех людей, которые одновременно и учатся, и работают \n"
#                        "3 - Найти всех людей, которые только учатся, но не работают \n"
#                        "4 - Найти Всех людей, которые либо только учатся, либо только работают, но не одновременно \n"
#                        "0 - Выйти из программы \n"
#                        "Ваш выбор: "))
#
#     if answer == 1:
#         print(all_people_in_groups(students, employees))
#     elif answer == 2:
#         print(all_people_together_students_and_employees(students, employees))
#     elif answer == 3:
#         print(all_people_students(students, employees))
#     elif answer == 4:
#         print(all_people_students_or_employees_no_together(students, employees))
#     elif answer == 0:
#         break

############################################### 2
# Напишите программу, которая получает на вход три слова и определяет, являются ли они анаграммами друг друга

# words = input("Введите 3 слова через пробел: ").lower().split(" ")
#
#
# def words_anagrams(text_1):
#     a = set(text_1[0])
#     b = set(text_1[1])
#     c = set(text_1[2])
#     if a == b == c:
#         print("Все три слова являются анаграммами друг друга")
#     else:
#         print("Слова НЕ являются анаграммами друг друга")
#
#
# words_anagrams(words)

############################################### 3
# Напишите программу, которая получает на вход строку, и определяет,
# является ли строка панграммой (т.е. содержатся ли в ней все 33 буквы русского алфавита).

# def azbuka(text_1):
#     count_1 = 0
#     x = set(text_1)
#     for i in range(len(x)):
#         count_1 += 1
#     if count_1 == 33:
#         return True
#     else:
#         return False
#
#
# print(azbuka("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"))

############################################### 4
# Напишите программу, которая получает n слов, и вычисляет количество уникальных символов во всех словах.

# def unik_words(set_1):
#     count_1 = 0
#     unik_word = []
#     for i in set_1:
#         unik_word += i
#     end = set(unik_word)
#     for j in range(len(end)):
#         count_1 += 1
#     return count_1
#
#
# print(unik_words(["олег", "опера"]))
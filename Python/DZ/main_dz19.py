############################################## 1
# Дано два текстовых файла. Выяснить, совпадают ли их строки. Если нет, то вывести несовпадающую строку
# из каждого файла.

# with open("file1.txt", "w", encoding="utf-8") as file:
#     file.write("Hello World!\n"
#                "Привет, как дела?")
# with open("file2.txt", "w", encoding="utf-8") as file:
#     file.write("Hello World!\n"
#                "Классная погодка!")
# try:
#     with open("file1.txt", "r", encoding="utf-8") as file_1, open('file2.txt', 'r', encoding="utf-8") as file_2:
#         equal_strings = set(file_1).symmetric_difference(file_2)
#         for i in equal_strings:
#             print(i)
#
# except FileNotFoundError:
#     print(f"No such file or direktory file1.txt or file2.txt")

############################################## 2
# Дан текстовый файл. Необходимо создать новый файл и записать в него следующую статистику по исходному файлу:
# ■ Количество символов;
# ■ Количество строк;
# ■ Количество гласных букв;
# ■ Количество согласных букв;
# ■ Количество цифр.

# symbol_glasnie = "уеыаоэяию"
# symbol_soglasnie = "йцкнгшщзхфвпрлджчсмтб"
# count_gl = 0
# count_sogl = 0
# count_digit = 0
#
# with open("file1.txt", "w", encoding="utf-8") as file:
#     file.write("Привет Мир!\n"
#                "Здорова, как дела?\n"
#                "Есть, что поесть?\n"
#                "123")
#
# try:
#     with open("file1.txt", "r", encoding="utf-8") as file:
#         content_1 = file.read()
#         count_length = len(content_1)
#         for j in content_1.lower():
#             if j in symbol_glasnie:
#                 count_gl += 1
#             elif j in symbol_soglasnie.lower():
#                 count_sogl += 1
#             elif j.isnumeric():
#                 count_digit += 1
#     content_2 = content_1.splitlines()
#
#     with open("file2.txt", "w", encoding="utf-8") as file:
#         file.write(f"Количество символов - {count_length}\n")
#         file.write(f"Количество строк - {len(content_2)}\n")
#         file.write(f"Количество гласных букв - {count_gl}\n"
#                      f"Количество согласных букв - {count_sogl}\n"
#                      f"Количество цифр - {count_digit}\n")
#
#     with open("file2.txt", "r", encoding="utf-8") as file:
#         print(file.read())
#
# except FileNotFoundError:
#     print(f"No such file or direktory file1.txt or file2.txt")

############################################## 3
# Дан текстовый файл. Удалить из него последнюю строку. Результат записать в другой файл.

# with open("file1.txt", "w", encoding="utf-8") as file:
#     file.write("Привет Мир!\n"
#                "Здорова, как дела?\n"
#                "Есть, что поесть?\n"
#                "123")
#
# with open("file1.txt", "r", encoding="utf-8") as file:
#     line_end = file.read().splitlines().pop()
#
# with open("file2.txt", "w", encoding="utf-8") as file:
#     file.write(line_end)

############################################## 4
# Дан текстовый файл. Найти длину самой длинной строки.

# with open("file1.txt", "w", encoding="utf-8") as file:
#     file.write("Привет Мир!\n"
#                "Здорова, как дела?\n"
#                "Есть, поесть?\n"
#                "123")
#
# with open("file1.txt", "r", encoding="utf-8") as file:
#     line_long = file.read().splitlines()
#     for j in range(len(line_long) - 1):
#         for i in range(len(line_long) - 1 - j):
#             if len(line_long[i]) > len(line_long[i+1]):
#                 line_long[i], line_long[i + 1] = line_long[i + 1], line_long[i]
#
# print(f'Самая длинная строка: "{line_long[len(line_long) - 1]}" - длина равна {len(line_long[len(line_long) - 1])} символов')

############################################## 5
# Дан текстовый файл. Посчитать сколько раз в нем встречается заданное пользователем слово

# word = input("Введите искомое слово: ").lower()
# count_word = 0
# symbols = "!?,.:;"
# with open("file1.txt", "w", encoding="utf-8") as file:
#     file.write("Привет Мир!\n"
#                "Здорова, мир!\n"
#                "Есть, поесть?\n"
#                "Мир")
#
# with open("file1.txt", "r", encoding="utf-8") as file:
#     line_long = file.read().splitlines()
#     for i in line_long:
#         s = i.lower().split(" ")
#         for j in s:
#             for k in range(len(j)):
#                 if j[k] in "!?,.:;":
#                     j = j[:k] + '' + j[k+1:]        #Удаляем !?,.:;
#             if word == j:
#                 count_word += 1
#
# print(f"Слово {word} встречается {count_word} раз(а)")

############################################## 6
# Дан текстовый файл. Найти и заменить в нем заданное слово. Что искать и на что заменять определяется
# пользователем.

# with open("file2.txt", "w", encoding="utf-8") as file:
#     file.write("Привет Мир\n"
#                "Здорова Мир\n"
#                "Есть поесть\n"
#                "Мир\n")
# word = input("Введите искомое слово: ").lower()
# word_new = input("Введите новое слово: ").lower()
#
# with open("file2.txt", "r", encoding="utf-8") as file, open("file3.txt", "w", encoding="utf-8") as file_new:
#     for i in file:
#         line = i.lower().replace(word, word_new)
#         file_new.write(line)
#
# with open("file3.txt", "r", encoding="utf-8") as file, open("file2.txt", "w", encoding="utf-8") as file_old:
#     line = file.read()
#     file_old.write(line.lower())

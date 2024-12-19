############################################## 1
# Дан текстовыйфайл. Необходимо создать новый файл убрав из него все неприемлемые слова.
# Список неприемлемых слов находится в другом файле.

# with open("file2.txt", "w", encoding="utf-8") as file:
#     file.write("Чувак\n"
#                "Пижон\n"
#                "Дурь\n"
#                "чайник\n")
#
# with open("file3.txt", "w", encoding="utf-8") as file:
#     file.write("Привет\n"
#                "Чувак\n"
#                "Здорова\n"
#                "пижон\n"
#                "Есть\n"
#                "Дурь\n"
#                "чайник\n")
#
#
# def censura(file1, file2):
#     try:
#         with open(file1, "r", encoding="utf-8") as file_1, open(file2, "r", encoding="utf-8") as file_2, \
#                 open("file4.txt", "w", encoding="utf-8") as file_new:
#             line = set(file_1.read().lower().splitlines()) ^ set(file_2.read().lower().splitlines())
#             for i in line:
#                 file_new.write(str(i + "\n"))
#     except FileNotFoundError:
#             print("Файл не найден!")
#
#
# censura("file2.txt", "file3.txt")

############################################## 2
# Написать программу транслитерации с русского на английский и наоборот. Данные для транслитерации
# берутся из файла и записываются в другой файл. Направление перевода определяется через меню пользователя.

# import json
#
# rus_eng = {
#     "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ж": "j", "з": "z", "и": "i", "й": "y", "к": "k", "л": "l",\
#     "м": "m", "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f", "х": "h", "ц": "c",\
#     "ч": "ch", "ш": "sh", "щ": "sh`", "ы": "i", "ь": "`", "э": "e", "ю": "yu", "я": "ya", " ": " ", "a": "а", "b": "б",\
#     "c": "ц", "d": "д", "e": "е", "f": "ф", "g": "г", "h": "х", "i": "i", "j": "ж", "k": "к", "l": "л",\
#     "m": "м", "n": "н", "o": "о", "p": "п", "q": "ку", "r": "р", "s": "с", "t": "т", "u": "у", "v": "в", "w": "в",\
#     "x": "икс", "y": "ай", "z": "з`"
#     }
#
# with open("files1.txt", "w", encoding="utf-8") as file:
#     json.dump(rus_eng, file)
#
#
# def rus_en(texts):
#     end = []
#     word = input("Введите текст для транслитерации: ").lower()
#     with open("files1.txt", "r", encoding="utf-8") as file:
#         for i in word:
#             end.append(rus_eng[i])
#     print("".join(end))
#
#
# def en_rus(texts):
#     end = []
#     word = input("Введите текст для транслитерации: ").lower()
#     with open("files1.txt", "r", encoding="utf-8") as file:
#         for i in word:
#             end.append(rus_eng[i])
#     print("".join(end))
#
#
# def main():
#     transcription = {}
#     while True:
#         menu = input(f"Главное меню:\n"
#                      "1 - перевести с русский - английский\n"
#                      "2 - перевести с английского на русский\n"
#                      "0 - выход\n"
#                      "Выбор:")
#
#         if menu == "1":
#             rus_en(transcription)
#         elif menu == "2":
#             en_rus(transcription)
#         elif menu == "0":
#             print("*** ВЫХОД ***")
#             break
#         else:
#             print("Неверные данные")
#
# main()

import os

# os.mkdir("new_dir") #Создание директории
# os.makedirs("oleg/piton") #Создание директории в дериктории

# if os.path.exists("kontrol.py"):    # Проверяем есть ли такой файл или папка в корневом католге
#     print("Yes")
# else:
#     print("No")
#
# print(f"Размер в байтах - {os.path.getsize('kontrol.py')}")  # Проверяем размер файла

# print(f"Расположение каталога - {os.getcwd()}")  # Проверяем Расположение каталога файла

# os.rename('oleg/piton/oleg.xml', 'oleg/piton/oleg2.xml')  #Переименовываем файл

#################################### 1
# Вывести текущую директорию.
# print("Текущая деректория:", os.getcwd())

#################################### 2
# 2. Создать новую папку в текущей директории.
# os.mkdir("new_dir2")

# 3. Переименовать папку.
# os.rename('new_dir2', '7777')

# 4. Создать новый файл в текущей директории.
# open('oleg/piton/bob.txt', 'a').close()

# 5. Удалить файл.
# os.remove('oleg/piton/bob.txt')

# 6. Перейти в другую директорию.
# directory = "P:/Студенты/ГК Python41/Лукашов/Python"
# files = os.listdir(directory)
# print(files)

# 7. Вывести список файлов и папок в текущей директории.

# directory = "P:/Студенты/ГК Python41/Лукашов/Python"
# files = os.listdir(directory)
# print(files)


# 8. Получить размер файла.
# print(f"Размер в байтах - {os.path.getsize('oleg/piton/oleg2.xml')}")

# 9. Проверить существование файла или папки.
# if os.path.exists('oleg/piton/oleg2.xml'):
#     print("Yes")
# else:
#     print("No")

# 10. Получить абсолютный путь до файла.
# relative_path = "oleg/piton/oleg2.xml"
# absolute_path = os.path.abspath(relative_path)
# print(absolute_path)

# 11. Вывести список файлов в текущей директории.

# for koren, directory, files in os.walk('P:/Студенты/ГК Python41/Лукашов/Python'):
#     if koren == "P:/Студенты/ГК Python41/Лукашов/Python":
#         print(files)


#СТАРЫЙ МЕТОД
###### Создаем и записываем в файл данные

# file = open("oleg/piton/file.txt", "w")
# file.write("Hello world!")
# file.close()
#НОВЫЙ МЕТОД
# with open("oleg/piton/file2.txt", "w") as file:
#     file.write("QQQQQQQQQQQQQQQQQQQQQQQQ!!!")

###### Изменяем данные в файле

# file = open("oleg/piton/file.txt", "a")
# file.write(" Hello user!")
# file.close()
#НОВЫЙ МЕТОД
# with open("oleg/piton/file2.txt", "a") as file:
#     file.write(" Привет моя принцесса!!!")

###### Чтение данных в файле
# file = open("oleg/piton/file.txt", "r")
# print(file.read())
# file.close()
#НОВЫЙ МЕТОД
# with open("oleg/piton/file2.txt", "r") as file:
#     print(file.read())



########################################## 1
# Запись в файл: попросите пользователя ввести текст, а затем сохраните этот текст в файл
# text_1 = input("Введите любой тексе: ")
# with open("oleg/piton/file3.txt", "w", encoding="utf-8") as file:
#     file.write(text_1)
# with open("oleg/piton/file3.txt", "r", encoding="utf-8") as file:
#     print(file.read())

########################################## 2
# Чтение файла и вывод его содержимого: запросите у пользователя имя файла и выведите его содержимое на экран
# filename = input("Введите имя файла с расширением: ")
# text = input("Введите текст для файла: ")
# with open(f"P:/Студенты/ГК Python41/Лукашов/Python/oleg/piton/{filename}", "w", encoding="utf-8") as file:
#     file.write(text)
# with open(f"P:/Студенты/ГК Python41/Лукашов/Python/oleg/piton/{filename}", "r", encoding="utf-8") as file:
#     print(file.read())

########################################## 3
# Копирование файла: попросите пользователя ввести имя файла, который нужно скопировать, и имя нового файла, в который нужно
# скопировать содержимое.
# filename = input("Введите имя файла с расширением: ")
# new_filename = input("Введите имя нового файла с расширением: ")
# try:
#     with open(f"P:/Студенты/ГК Python41/Лукашов/Python/oleg/piton/{filename}", "r", encoding="utf-8") as file:
#         content = file.read()
#     with open(f"P:/Студенты/ГК Python41/Лукашов/Python/oleg/piton/{new_filename}", "w", encoding="utf-8") as new_file:
#         new_file.write(content)
# except FileNotFoundError:
#     print(f"No such file or direktory {filename}.txt")

########################################## 4
# Подсчет строк в файле: подсчитайте количество строк в текстовом файле и выведите результат.

# filename = input("Введите имя файла с расширением: ")
#
# try:
#     with open(f"P:/Студенты/ГК Python41/Лукашов/Python/oleg/piton/{filename}", "r", encoding="utf-8") as file:
#         content = file.readlines()
#         print(f"Количество строк равно {len(content)}")
#
# except FileNotFoundError:
#     print(f"No such file or direktory {filename}.txt")


########################################## 5
# Поиск слова в файле: попросите пользователя ввести слово, а затем проверьте, есть ли это слово в файле. Если да, выведите
# сообщение о том, что слово найдено, иначе сообщение о том, что слово не найдено
filename = input("Введите имя файла с расширением: ")
txt = input("Введите искоемое слово: ")

try:
    with open(f"P:/Студенты/ГК Python41/Лукашов/Python/oleg/piton/{filename}", "r", encoding="utf-8") as file:
        content = file.read()
        if txt in content:
            print(f"Слово {txt} есть в файле")
        else:
            print(f"Слово {txt} ОТСУТСТВУЕТ в файле")

except FileNotFoundError:
    print(f"No such file or direktory {filename}.txt")

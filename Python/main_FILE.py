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
# filename = input("Введите имя файла с расширением: ")
# txt = input("Введите искоемое слово: ")
#
# try:
#     with open(f"P:/Студенты/ГК Python41/Лукашов/Python/oleg/piton/{filename}", "r", encoding="utf-8") as file:
#         content = file.read()
#         if txt in content:
#             print(f"Слово {txt} есть в файле")
#         else:
#             print(f"Слово {txt} ОТСУТСТВУЕТ в файле")
#
# except FileNotFoundError:
#     print(f"No such file or direktory {filename}.txt")

########################################## 1
# Дан текстовыйфайл. Необходимо создать новыйфайл, в который требуется переписать из исходного файла все
# слова, состоящие не менее чем из семи букв

# with open("file1.txt", "w", encoding="utf-8") as file:
#     file.write("Приветствие\n"
#                "Здравсвуйте\n"
#                "Еда\n"
#                "Миропорядок")
#
# def filter_words(input_file, output_file):
#     try:
#         with open(input_file, "r", encoding="utf-8") as file, \
#                 open(output_file, "w", encoding="utf-8") as new_file:
#             filtered_words = []
#             for i in file:
#                 words = i.split()
#                 for j in words:
#                     if len(j) > 7:
#                         filtered_words.append(j)
#             filtered_line = " ".join(filtered_words)
#             new_file.write(filtered_line + "\n")
#
#     except FileNotFoundError:
#         print("Файл не найден!")
#
# filter_words("file1.txt", "new_file.txt")

########################################## 2
# Дан текстовый файл. Необходимо переписать его строки в другой файл. Порядок строк во втором файле
# должен совпадать с порядком строк в заданном файле.

# with open("file1.txt", "w", encoding="utf-8") as file:
#     file.write("Приветствие\n"
#                "Здравсвуйте\n"
#                "Еда\n"
#                "Миропорядок")
#
# def filter_words(input_file, output_file):
#     try:
#         with open(input_file, "r", encoding="utf-8") as file, \
#                 open(output_file, "w", encoding="utf-8") as new_file:
#             for line in file:
#                 new_file.write(line)
#
#     except FileNotFoundError:
#         print("Файл не найден!")
#
# filter_words("file1.txt", "new_file.txt")

########################################## 3
# Дан текстовый файл. Необходимо переписать его строки в другой файл. Порядок строк во втором файле
# должен быть обратным по отношению к порядку строк в заданном файле.

# with open("file1.txt", "w", encoding="utf-8") as file:
#     file.write("Приветствие\n"
#                "Здравсвуйте\n"
#                "Еда\n"
#                "Колегга \n"
#                "Миропорядок \n")
#
# def filter_words(input_file, output_file):
#     try:
#         with open(input_file, "r", encoding="utf-8") as file, \
#                 open(output_file, "w", encoding="utf-8") as new_file:
#             lines = file.readlines()
#             reversed_lines = reversed(lines)
#             for line in reversed_lines:
#                 new_file.write(line)
#
#     except FileNotFoundError:
#         print("Файл не найден!")
#
# filter_words("file1.txt", "new_file.txt")

########################################## 5
# Дан текстовый файл. Подсчитать количество слов, начинающихся с символа, который задаёт пользователь.

# with open("file1.txt", "w", encoding="utf-8") as file:
#     file.write("Приветствие Дар\n"
#                "Здравсвуйте Мама\n"
#                "Еда Лимон\n"
#                "Колегга Саша\n"
#                "Миропорядок Добро\n")
#
# def filter_words(input_file, char):
#     try:
#         count = 0
#         with open(input_file, "r", encoding="utf-8") as file:
#             for line in file:
#                 words = line.split()
#                 for word in words:
#                     if word.lower().startswith(char):
#                         count += 1
#         print(f"кол-во слов {count}")
#
#     except FileNotFoundError:
#         print("Файл не найден!")
#
# filter_words("file1.txt", input("Введите символ с которого ничанается: ")[0].lower())

########################################## 6
# Дан текстовыйфайл. Переписать в другойфайл все его строки с заменой в них символа * на символ & и наоборот.

# with open("file1.txt", "w", encoding="utf-8") as file:
#     file.write("Приветствие * Дар\n"
#                "Здравсвуйте & Мама\n"
#                "Еда * Лимон\n"
#                "Колегга & Саша\n"
#                "Миропорядок * Добро\n")
#
# def filter_words(input_file, output_file):
#     try:
#         with open(input_file, "r", encoding="utf-8") as file, \
#                 open(output_file, "w", encoding="utf-8") as new_file:
#             for line in file:
#                 new_line = line.replace("*", "1").replace("&", "*").replace("1", "&")
#                 new_file.write(new_line)
#
#     except FileNotFoundError:
#         print("Файл не найден!")
#
# filter_words("file1.txt","new_file.txt")

########################################## 7
# Дан массив строк. Записать их в файл, расположив каждый элемент массива на отдельной строке с сохранением порядка.

# with open("file1.txt", "w", encoding="utf-8") as file:
#     file.write("Приветствие * Дар\n"
#                "Здравсвуйте & Мама\n"
#                "Еда * Лимон\n"
#                "Колегга & Саша\n"
#                "Миропорядок * Добро\n")
#
# def filter_words(input_file, words):
#     try:
#         with open(input_file, "w", encoding="utf-8") as file:
#             for word in words:
#                 file.write(word + "\n")
#
#     except FileNotFoundError:
#         print("Файл не найден!")
#
# filter_words("file1.txt",["привет", "магазин", "привет", "магазин", "привет", "магазин"])

########################################## 9
# Дан текстовый файл. Подсчитать количество символов в нём.

# with open("file1.txt", "w", encoding="utf-8") as file:
#     file.write("Приветствие * Дар\n"
#                "Здравсвуйте & Мама\n"
#                "Еда * Лимон\n"
#                "Колегга & Саша\n"
#                "Миропорядок * Добро\n")
#
# def filter_words(input_file):
#     try:
#         with open(input_file, "r", encoding="utf-8") as file:
#             content = file.read()
#         print(f"кол-во симовлов {len(content)}")
#
#     except FileNotFoundError:
#         print("Файл не найден!")
#
# filter_words("file1.txt")

########################################## 10
# Дан текстовый файл. Подсчитать количество строк в нём

# with open("file1.txt", "w", encoding="utf-8") as file:
#     file.write("Приветствие * Дар\n"
#                "Здравсвуйте & Мама\n"
#                "Еда * Лимон\n"
#                "Колегга & Саша\n"
#                "Миропорядок * Добро\n")
#
# def filter_words(input_file):
#     try:
#         with open(input_file, "r", encoding="utf-8") as file:
#             content = file.readlines()
#         print(f"кол-во симовлов {len(content)}")
#
#     except FileNotFoundError:
#         print("Файл не найден!")
#
# filter_words("file1.txt")

########################################## 11
# Напишите информационную систему «Сотрудники».
# Программа должна обеспечивать ввод данных, редактирование данных сотрудника, удаление сотрудника, поиск
# сотрудника по фамилии, вывод информации обо всех сотрудниках, указанного возраста, или фамилия которых
# начинается на указанную букву. Организуйте возможность сохранения найденной информации в файл. Также весь
# список сотрудников сохраняется в файл (при выходе из программы — автоматически, в процессе исполнения
# программы — по команде пользователя). При старте программы происходит загрузка списка сотрудников из
# указанного пользователем файла

def load_employee_list(file):
    employee_list = []
    try:
        with open(file, "r", encoding="utf-8") as file:
            for line in file:
                print(line)
                last_name, first_name, age = line.strip().split(",")
                employee_list.append({"Фамилия": last_name,
                                      "Имя": first_name,
                                      "Возраст": int(age)})

    except FileNotFoundError:
        print("Такого файла нет!")
    return employee_list


def add_employee(employee_list):
    if not employee_list:
        print("База пуста!")
        return
    last_name = input("Введите фамилию сотрудника")
    first_name = input("Введите имя сотрудника")
    age = int(input("Введите возраст сотрудника"))
    employee_list.append({"Фамилия": last_name,
                          "Имя": first_name,
                          "Возраст": int(age)})
    print("Сотрудник успешно добавлен")


def edit_employee(employee_list):
    last_name = input("Введите фамилию сотрудника")
    for employee in employee_list:
        if employee["Фамилия"] == last_name:
            first_name = input("Введите имя сотрудника")
            age = int(input("Введите возраст сотрудника"))
            employee["Имя"] = first_name
            employee["Возраст"] = age
            print("Данные успешно обновлены!")
    print("Сотрудник с такой фамилией не найден!")


def delete_employee(employee_list):
    if not employee_list:
        print("База пуста!")
        return
    last_name = input("Введите фамилию сотрудника для удаления")
    for employee in employee_list:
        if employee["Фамилия"] == last_name:
            employee_list.remove(employee)
            print("Сотрудник успешно удален!")
            return
    print("Сотрудник с такой фамилией не найден!")


def search_by_last_name(employee_list):
    if not employee_list:
        print("База пуста!")
        return
    last_name = input("Введите фамилию сотрудника для поиска")
    for employee in employee_list:
        if employee["Фамилия"] == last_name:
            print(f'Фамилия: {employee["Фамилия"]}, Имя: {employee["Имя"]}, Возраст: {employee["Возраст"]}')
            return
    print("Сотрудник с такой фамилией не найден!")


def search_by_age(employee_list):
    if not employee_list:
        print("База пуста!")
        return
    age = int(input("Введите возраст сотрудника для поиска"))
    found = False
    for employee in employee_list:
        if employee["Возраст"] == age:
            print(f'Фамилия: {employee["Фамилия"]}, Имя: {employee["Имя"]}, Возраст: {employee["Возраст"]}')
            found = True
    if not found:
        print("Сотрудник с такой возрастом не найден!")


def search_by_letter(employee_list):
    if not employee_list:
        print("База пуста!")
        return
    letter = input("Введите первую букву фамилии сотрудника для поиска")
    found = False
    for employee in employee_list:
        if employee["Имя"].startswith(letter):
            print(f'Фамилия: {employee["Фамилия"]}, Имя: {employee["Имя"]}, Возраст: {employee["Возраст"]}')
            found = True
    if not found:
        print("Сотрудник с такой именем не найден!")


def print_all(employee_list):
    if not employee_list:
        print("База пуста!")
        return
    print("Список всех сотрудников:")
    for employee in employee_list:
        print(f'Фамилия: {employee["Фамилия"]}, Имя: {employee["Имя"]}, Возраст: {employee["Возраст"]}')


def save_employee_list(employee_list, file):
    with open(file, "w", encoding="utf-8") as file:
        for employee in employee_list:
            file.write(f'{employee["Фамилия"]},{employee["Имя"]},{employee["Возраст"]}\n')
    print("Файл успешно сохранен!")

def main():
    filename = input("Введите название файла для загрузки данных: ")
    employees = load_employee_list(filename)
    while True:
        choice = input("Меню \n"
              "1 - Добавить сотрудника\n"
              "2 - Редактировать данные сотрудника\n"
              "3 - Удалить сотрудника\n"
              "4 - Поиск сотрудника по фамилии\n"
              "5 - Поиск сотрудника по возарсту\n"
              "6 - Поиск сотрудника по первой букве в имя\n"
              "7 - Вывести полностью список сотрудников \n"
              "8 - Сохранить список сотрудников в файл\n"
              "9 - Выход из программы\n"
              "Выбор: ")
        if choice == 1:
            add_employee(employees)
        elif choice == 2:
            edit_employee(employees)
        elif choice == 3:
            delete_employee(employees)
        elif choice == 4:
            search_by_last_name(employees)
        elif choice == 5:
            search_by_age(employees)
        elif choice == 6:
            search_by_letter(employees)
        elif choice == 7:
            print_all(employees)
        elif choice == 8:
            save_employee_list(employees, filename)
        elif choice == 9:
            save_employee_list(employees, filename)
            break
        else:
            print("Неверный выбор")

main()
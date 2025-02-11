# import json
#
#
# data = {
#     "name": "Alex",
#     "surname": "Pupkin",
#     "age": 23,
#     "sex": "male",
#     "skils": ["JS", "Python", "C++"],
#     "adress": {
#         "city": "Moscow",
#         "street": "Zubkova"
#     }
# }
#
##### Создаем JSON строку
# json_str = json.dumps(data, indent=4)
# print(type(json_str))
# print(json_str)
#
##### Создаем JSON файл
# with open("data.json", "w") as file:
#     json.dump(data, file, indent=4)

##### Из строки получаем словарь
# json_str = '''
# {
#     "name": "Alex",
#     "surname": "Pupkin",
#     "age": 23,
#     "sex": "male",
#     "skils": ["JS", "Python", "C++"],
#     "adress": {
#         "city": "Moscow",
#         "street": "Zubkova"
#     }
# }
# '''

# data = json.loads(json_str)
# print(type(data))
# print(data)


##### Из JSON получаем словарь
# try:
#     with open("data.json", "r") as file:
#         data_2 = json.load(file)
# except FileNotFoundError as e:
#     print(e)
# else:
#     print(type(data_2))
#     print(data_2)
# finally:
#     print("Done!")

############################################ 1
# Напишите программу, которая создает словарь с информацией
# о студенте (имя, возраст, курсы). Сериализуйте этот словарь в строку
# формата JSON и сохраните его в файл. Затем прочитайте файл,
# десериализуйте данные и выведите их на экран.

import json


def add_student(students):
    name = input("Введите имя студента: ").strip().lower()
    age = int(input("Введите возраст студента: "))
    course = input("Введите название курса: ").strip().lower()

    if name in students:
        print(f'Студент: "{name}" уже существует!')
        return

    if name not in students:
        students[name] = {"age": age, "course": course}
    print("*** Студент успешно добавлен! ***\n")


def del_student(students):
    if not students:
        print("*** Список пуст! ***\n")
        return

    name = input("Введите имя студента: ").strip().lower()
    if name not in students:
        print("*** Такого студента не существует! ***\n")
        return

    del students[name]
    print(f'Студент "{name}" успешно удален!\n')


def info_student(students):
    if not students:
        print("*** Список пуст! ***\n")
        return
    for name, details in students.items():
        print(f'Студент: {name} | Возраст: {details["age"]} | Курс: {details["course"]}')
        print()


def seruliz_in_str(students):
    json_str = json.dumps(students, indent=4)
    print("Done!")
    return json_str


def seruliz_in_json(students):
    with open("data.json", "w") as file:
        json.dump(students, file, indent=4)
    print("Done!")


def deseruliz_in_json(students):
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError as e:
        print(e)
    else:
        print(data)
    finally:
        print("Done!")


def main():
    students = {}
    while True:
        menu = input(f"Главное меню:\n"
                     "1 - создать студента\n"
                     "2 - удалить студента\n"
                     "3 - вывести список студентов\n"
                     "4 - Сериализвать словарь в строку\n"
                     "5 - Cохранить словарь в файл data.json\n"
                     "6 - Прочитать файл, десериализовать данные и вывести их на экран"
                     "0 - выход\n"
                     "Выбор: ")

        if menu == "1":
            add_student(students)
        elif menu == "2":
            del_student(students)
        elif menu == "3":
            info_student(students)
        elif menu == "4":
            seruliz_in_str(students)
        elif menu == "5":
            seruliz_in_json(students)
        elif menu == "6":
            deseruliz_in_json(students)
        elif menu == "0":
            print("*** ВЫХОД ***")
            break
        else:
            print("Неверные данные")


main()


# Практические задания
# 1. Напишите программу, которая создает словарь с информацией
# о студенте (имя, возраст, курсы). Сериализуйте этот словарь в строку
# формата JSON и сохраните его в файл. Затем прочитайте файл,
# десериализуйте данные и выведите их на экран.
# 2. Создайте вложенный словарь, представляющий информацию о
# книге (название, автор, информация об издателе). Сериализуйте этот
# словарь в строку формата JSON и сохраните его в файл. Затем
# прочитайте файл, десериализуйте данные и выведите их на экран.
# 3. Создайте класс Employee, который содержит информацию о
# сотруднике (имя, должность, зарплата). Напишите методы для
# сериализации объекта Employee в JSON и десериализации из JSON.
# Сохраните объект в файл и затем прочитайте его, выведя данные на
# экран.
# Словарь  это структура данных, которая представляет собой коллекцию пар ключ-значение, где каждый ключ связан с
# определенным значением.
# -Уникальность
# -Неупорядочность
# -Изменяемость
# -Использование различных типов ключей и значений

# frutis_1 = {
#     "apple": 5,
#     "banana": 4,
#     "orange": 6,
# }
#
# frutis_2 = dict([("apple", 5), ("banana", 4), ("orange", 6)])
#
# print(frutis_1)
# print(frutis_2)

###########################################

# numbers = {i: i*2 for i in range(10)}
# print(numbers)

# frutis_1 = {
#     "apple": 5,
#     "banana": 4,
#     "orange": 6,
#     "mandarin": 2,
# }
# x = frutis_1.copy()                 #Копируем
# frutis_1["pinapple"] = 20           #Добавляем ключ - элемент
# frutis_1["orange"] = 200            #Изменяем  значение элемента
#
# if "apple" in frutis_1:
#     del frutis_1["apple"]           #Удаляем ключ и элемент
# frutis_1.pop("banana")              #Удаляем по ключу
# # frutis_1.clear("orange")            #Очищает словарь
# value = frutis_1.get("pinapple", 0)     #Возращает значение ключа
# keys = frutis_1.keys()               #Возращает список из ключей

# for i in keys:                  #Возращает ключи
#     print(i)
# for i in value:                  #Возращает элементы
#     print(i)

# items_1 = frutis_1.items()        #Возращает ключи
# print(items_1)
#
# for key, value in frutis_1.items():   #Возращает ключи и элементы
#     print(f"key: {key}, value: {value}")

# frutis_1.update(x)      #Обновляет словари
# print(frutis_1)

# print(frutis_1["orange"])
# print(frutis_1)
# print(value)
# print(keys)
# print("mandarin" in keys)

#########################################################


# def info(name, age):                    #РАСПАКОВКА
#     print(f"Name: {name}\n"
#           f"Age: {age}")
#
#
# person = {
#     "name": "Alex",
#     "age": 25,
# }
#
# info(**person)

#########################################################1
# Напишите функцию для обновления словаря новыми значениями из другого словаря. Если ключи уже существуют,
# значения должны быть обновлены.

# person = {
#     "name": "Alex",
#     "age": 25,
# }
# person_add   = {
#     "job": "programmer",
#     "age": 30,
# }
# person.update(person_add)
#
# print(person)

######################################################### 2
# Напишите функцию для удаления элементов из словаря по заданному списку ключей.
# def delete_keys_from_list(dictionaty, key_list):
#     for k in key_list:
#         if k in dictionaty:
#             del dictionaty[k]
#             # dictionaty.pop(k, NONE)
#     return dictionaty
#
#
# person = {
#     "a": 2,
#     "b": 3,
#     "c": 4,
#     "d": 5,
# }
#
# list_of_keys = ["a", "b", "w"]
#
# print(delete_keys_from_list(person, list_of_keys))

######################################################### 3
# Напишите функцию, которая создает словарь из двух списков: один список для ключей, другой для значений. Если списки разной
# длины, использовать минимальную длину.
# def create_dict_from_lists(value_list, key_list):
#     new_dict = {}
#     for i in range(min([len(value_list), len(key_list)])):
#         new_dict[value_list[i]] = key_list[i]
#     return new_dict
#
# list_1 = ["a", "b", "c", "d"]
# list_2 = [1, 2, 3]
#
#
#
# print(create_dict_from_lists(list_1, list_2))

##### ПРИ ПОМОЩИ ZIP тоже самое

# def create_dict_from_lists(value_list, key_list):
#     return dict(zip(value_list, key_list))
#
#
# list_1 = ["a", "b", "c", "d"]
# list_2 = [1, 2, 3, 4, 5, 6]
#
#
# print(create_dict_from_lists(list_1, list_2))

######################################################### 4
#
# def add_player(players):
#     name = input("Введите имя баскетболиста: ")
#     if name in players:
#         print("Баскетболист с таким имененм уже сущесвтует! ")
#     else:
#         try:
#             height = float(input("Введите рост баскетболиста: "))
#         except ValueError:
#             print("Введите корректное значение!")
#         else:
#             players[name] = height
#             print(f"Баскетболист {name} успешно добавлен")
#
#
# def remove_player(players):
#     name = input("Введите имя баскетболиста: ")
#     if name not in players:
#         print("Баскетболист с таким имененм не сущесвтует! ")
#     else:
#         del players[name]
#         print(f"Баскетболист {name} успешно удален")
#
#
# def get_player(players):
#     name = input("Введите имя баскетболиста: ")
#     find_player = players.get(name, "Не сущесвтует! ")
#     print(f"{name}: {find_player}")
#
#
# def replace_player(players):
#     name = input("Введите имя баскетболиста для замены данных: ")
#     if name not in players:
#         print("Баскетболист с таким имененм не сущесвтует! ")
#     else:
#         try:
#             height = float(input("Введите рост баскетболиста: "))
#         except ValueError:
#             print("Введите корректное значение!")
#         else:
#             players[name] = height
#             print(f"Данные об игроке {name} успешно обновлены")
#
#
# def show_all(players):
#     for name, height in players.items():
#         print(f"Имя: {name}, Рост: {height} м")
#
#
# def menu():
#     basketball_players = {}
#     while True:
#         answer = input(f"Mеню:\n"
#                        f"1 - Добавить баскетболиста\n"
#                        f"2 - Удалить баскетболиста\n"
#                        f"3 - Найти баскетболиста\n"
#                        f"4 - Заменить данные баскетболиста\n"
#                        f"5 - Показать всех баскетболистов\n"
#                        f"0 - Выход\n")
#         if answer == "1":
#             add_player(basketball_players)
#         elif answer == "2":
#             remove_player(basketball_players)
#         elif answer == "3":
#             get_player(basketball_players)
#         elif answer == "4":
#             replace_player(basketball_players)
#         elif answer == "5":
#             show_all(basketball_players)
#         elif answer == "0":
#             break
#         else:
#             print("Такого пункта нет в меню")
#
# menu()

######################################################### 7
# Напишите функцию, которая принимает словарь и ключ, а затем возвращает значение, соответствующее этому ключу. Если
# ключ отсутствует в словаре, функция должна вернуть значение по умолчанию.

# words = {
#     "name": "Oleg",
#     "age": 40
# }
# def dict_input(dict_1, key):
#     return dict_1.get(key, "No")
#
# print(dict_input(words, input("Введите ключ: ")))

######################################################### 4
# Напишите функцию, которая принимает словарь и список ключей, а затем проверяет, содержит ли словарь все эти ключи

# def get_value(dictionary, keys):
#     for k in keys:
#         if k not in dictionary:
#             return False
#
#     return True
#
# words = {
#     "a": 1,
#     "b": 2,
#     "c": 2,
#     "d": 2,
# }
#
# key_to_chek = ["a", "d", "w"]
#
# print(get_value(words, key_to_chek))
#

###################### 2ой метод ALL
# def get_value(dictionary, keys):
#     return all(k in dictionary for k in keys) #Проверяет что все элементы в последовательности True
#
# words = {
#     "a": 1,
#     "b": 2,
#     "c": 2,
#     "d": 2,
#
# }
#
# key_to_chek = ["a", "d", "w"]
#
# print(get_value(words, key_to_chek))

################################################ 5
# Напишите функцию, которая принимает список элементов и возвращает словарь, где ключами являются уникальные элементы
# списка, а значениями - количество повторений каждого элемента.

# list_values = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5]
#
# def count_elements(lst):
#     counts = {}
#     for i in lst:
#         # counts[i] = lst.get(i, 0) + 1
#         counts[i] = lst.count(i)
#     return counts
#
# print(count_elements(list_values))

################################################ 6
# Напишите функцию, которая принимает словарь и значение, а затем возвращает список ключей, соответствующих этому значению.

# dict_1 = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
#     "d": 4,
#     "e": 3,
#     "f": 2,
# }
#
# value = 2
#
# def found_same_values(dictionaty, val):
#     return [key for key, value in dictionaty.items() if val == value]
#
# print(found_same_values(dict_1, value))

################################################ 8
# Напишите функцию для обращения словаря, то есть создания нового словаря, где ключи и значения поменяны местами

# dict_1 = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
#     "d": 4,
#     "e": 3,
#     "f": 2,
# }
#
# def found_same_values(dictionaty):
#     return {value: key for key, value in dictionaty.items()}
#
# print(found_same_values(dict_1))
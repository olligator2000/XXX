# Неупорядочную коллекцию уникальных элементов. Можно удалять и добавлять.
# Сво-ва  - уникальность,
# - неупорядочность и не имеют индексов и может изменятся при каждой операции.
# Создаются в {}
# set_1 = {1, 3, -5, 6, 6, -6, 6, 8, 0}
# set_2 = {"f", "g", "y"}
# print(set_1)
# print(set_2)
# set_3 = set()
# set_4 = {i for i in range(10)}
# set_4 = {"hello", "green", "red"}
# set_6 = {"123", "333", "444"}

#######################################МЕТОДЫ
# set_4.add(100)     #Добавляет новый элемент внутрь множеста рандомно в разные места, работает как append
# set_4.remove(100)     #Удаляет элемент, если нет, выдает ошибку
# set_4.discard(100)     #Удаляет элемент, если нет, НЕ выдает ошибку
# popped_element = set_4.pop(2)     #Удаляет элемент рандмоный и это значение сохраняет в другом месте
# set_4.update([1, 2, 3])     #Обновляет множество с помощью нескольких значений , работает как extend
# set_4.clear()                  #удаляет элемент
# set_5 = set_4.copy()                #Копирует элемент
# print(set_4.issubset(set_6))        #Проверяем явлется ли другая переменная подмножеством, есть ли там такой элемент

# set_4.union(set_6)               #Объеденение множеств
# print(set_4 | set_6)              #Объеденение множеств

# print(set_4.intersection(set_6))            #Выводит общий элемент который есть и там и там
# print(set_4 & set_6)                        #Выводит общий элемент который есть и там и там

# print(set_4.difference(set_6))    #Нахождение разности множеств  выводит новое множество содержащее элементы присутствующие только в одном множестве
# print(set_6 - set_4)    #Нахождение разности множеств  выводит новое множество содержащее элементы присутствующие только в одном множестве
# print(set_6 - set_4 | set_4 - set_6)
# print(set_4.symmetric_difference((set_6)))   # Возращает новое множество содержащее элементы, присутствующие только в одном из множеств, но не в обоих
# print(set_4 ^ set_6)   # Возращает новое множество содержащее элементы, присутствующие только в одном из множеств, но не в обоих

# print(set_4.isdisjoint(set_6))       #Проверяет отсутсвтует ли общий элекмент. Если нет совпадений возвращает True
# print(set_4 == set_6)       #Проверяем есть ли равенство в присутсвии элментов

##########################################################1
# Уникальные элементы в списке: Напишите функцию unique_elements, которая принимает список в качестве аргумента и
# возвращает множество уникальных элементов этого списка.

# def unique_elements(list_1):
#     return set(list_1)
#
# print(unique_elements([5, 5, 6, 5, 8, 9, 6]))

##########################################################2
# Пересечение двух списков: Напишите функцию common_elements, которая принимает два списка в качестве
# аргументов и возвращает множество общих элементов этих списков

# def common_elements(list_1, list_2):
#     return set(list_1) | set(list_2)
#
# print(common_elements([5, 5, 6, 5, 7, 9, 6], [5, 5, 6, 3, 8, 9, 6]))

##########################################################3
# Разность двух множеств: Напишите функцию set_difference, которая принимает два множества в качестве аргументов и
# возвращает множество элементов, которые есть в первом множестве, но отсутствуют во

# def set_difference(set_1, set_2):
#     return set_1 - set_2
#
# print(set_difference({5, 10, 6, 5, 7, 9, 6}, {5, 5, 6, 3, 8, 9, 6}))

##########################################################4
# Объединение списка и множества: Напишите функцию union_list_set, которая принимает список и множество в качестве
# аргументов и возвращает множество, содержащее все уникальные элементы из списка и множества.

# def union_list_set(list_1, set_1):
#     x = set(list_1)
#     return x | set_1
#
# print(union_list_set([1, 2, 3], {1, 1, 5, 7}))

##########################################################5
# Удаление из списка элементов, содержащихся в множестве: Напишите функцию remove_items_in_set, которая принимает список
# и множество в качестве аргументов и возвращает новый список, не содержащий элементы, которые присутствуют в множестве.

# def remove_items_in_set(list_1, set_1):
#
#     for i in set_1:
#         list_1.remove(i)
#     return list_1
#
#
# print(remove_items_in_set([1, 2, 3, 4, 5], {3, 4}))

##########################################################6
# Симметрическая разность списков: Напишите функцию symmetric_difference_lists, которая принимает два списка в качестве
# аргументов и возвращает список, содержащий элементы, присутствующие только в одном из списков

# def symmetric_difference_lists(list_1, list_2):
#     a = set(list_1)
#     b = set(list_2)
#     c = a - b
#     return list(c)
#
# print(symmetric_difference_lists([1, 2, 3, 4], [5, 6, 3, 4]))

##########################################################7
# Получение элементов из списка, не присутствующих в множестве: Напишите функцию get_items_not_in_set, которая
# принимает список и множество в качестве аргументов и возвращает множество элементов из списка, которые не содержатся в множестве

# def get_items_not_in_set(list_1, set_1):
#     x = []
#     for i in list_1:
#         if i not in set_1:
#             x.append(i)
#     return set(x)
#
# print(get_items_not_in_set([1, 2, 3, 4, 5], {6, 7, 8, 9, 1, 2}))

##########################################################8
# Поиск общих элементов в нескольких списках: Напишите функцию common_elements_multiple_lists, которая принимает
# произвольное количество списков в качестве аргументов и возвращает множество, содержащее все общие элементы из всех
# переданных списков


def common_elements_multiple_lists(*list_x):
    x = set(list_x[0])
    for i in list_x[1:]:
        x = x & set(list_x)

    return x

print(common_elements_multiple_lists([4, 2, 3, 1], [1, 2, 3, 5], [6, 2, 3, 1]))

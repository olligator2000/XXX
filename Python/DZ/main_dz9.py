##################################################### 1
# Напишите функцию, вычисляющую произведение элементов списка целых. Список передаётся в качестве параметра.
# Полученный результат возвращается изфункции.

# def composition(list_1):
#     p = 1
#     for i in list_1:
#         p *= i
#     return p
# print(composition([2, 3, 4]))

##################################################### 2
# Напишите функцию для нахождения минимума в списке целых. Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.

# def mini(list_1):
#     return min(list_1)
# print(mini([20, 3, 4]))

##################################################### 3
# Напишите функцию, определяющую количество простых чисел в списке целых. Список передаётся в качестве
# параметра.Полученныйрезультат возвращаетсяизфункции

# numbers = []
# for i in range(1, 101):
#     numbers.extend([i])
#
#
# def simple(list_1):
#     simple_list = []
#     for j in range(1, len(list_1)):
#         if j == 1 or j == 2:
#             continue
#         for a in range(2, j):
#             if j % a == 0:
#                 break
#         else:
#             simple_list.extend([j])
#     return simple_list
#
#
# print(simple(numbers))

##################################################### 4
# Напишите функцию, удаляющую из списка целых некоторое заданное число. Из функции нужно вернуть
# количество удаленных элементов.

# def del_func(n, list_1):
#     counter = 0
#     list_copy = list_1.copy()
#     for i in list_1:
#         if n == i:
#             list_copy.remove(i)
#             counter += 1
#         list_1 = list_copy
#     return counter, list_1
#
#
# print(del_func(3, [2, 3, 5, 3, 6, 3, 9, 3, 4]))

##################################################### 5
# Напишите функцию, которая получает два списка в качестве параметра и возвращает список, содержащий
# элементы обоих списков.

# def double_list(list_1, list_2):
#     all_list = []
#     for i in list_1:
#         all_list.append(i)
#     for j in list_2:
#         all_list.append(j)
#     return all_list
#
#
# print(double_list([2, 3, 5, 6, 7], [5, 8, 9, 10, 12]))

##################################################### 6
# Напишитефункцию, высчитывающуюстепень каждого элемента списка целых. Значение для степени передаётся
# в качестве параметра, список тоже передаётся в качестве параметра. Функция возвращает новый список,
# содержащий полученные результаты

# def stepen(n, list_1):
#     return [i ** n for i in list_1]
#
#
# print(stepen(2, [1, 2, 3, 4]))
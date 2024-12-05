############################################### 1
# Есть четыре списка целых. Необходимо их объединить в пятом списке. Полученный результат в зависимости от
# выбора пользователя отсортировать по убыванию или возрастанию. Найти значение, введенное пользователем,
# с использованием линейного поиска.

# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# c = [9, 4, 4, 14]
# d = [12, 23, 23, 34]
# e = []
# for i in a, b, c, d:
#     e.extend(i)
#
#
# def look_list(x):
#     print(f"Список: {x}")
#     print()
#
#
# def sort_down(x):
#     print(f"Список: {sorted(x, reverse=True)}")
#     print()
#
#
# def sort_up(x):
#     print(f"Список: {sorted(x)}")
#     print()
#
#
# def search_element(x):
#     find_number = int(input("Введите число для поиска: "))
#     for j in range(len(x)):
#         if x[j] == find_number:
#             print(f"Элемент {find_number} найден в списке")
#             print()
#             return
#     print(f"Элемент {find_number} не найден в списке")
#     print()
#
#
# def main():
#     global e
#     while True:
#         answer = input(f"Mеню:\n"
#                        f"1 - Посмотреть список\n"
#                        f"2 - Отсортировать по убыванию\n"
#                        f"3 - Отсортировать по возрастанию\n"
#                        f"4 - Найти значение\n"
#                        f"0 - Выход\n")
#         if answer == "1":
#             look_list(e)
#         elif answer == "2":
#             sort_down(e)
#         elif answer == "3":
#             sort_up(e)
#         elif answer == "4":
#             search_element(e)
#         elif answer == "0":
#             print("КОНЕЦ ПРОГРАММЫ!")
#             break
#         else:
#             print("*** Неверные данные ***")
#             print()
#
#
# main()

############################################### 2
# Есть четыре списка целых. Необходимо объединить в пятом списке только те элементы, которые уникальны
# для каждого списка. Полученный результат в зависимости от выбора пользователя отсортировать по убыванию или
# возрастанию. Найти значение, введенное пользователем, с использованием бинарного поиска

# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# c = [9, 4, 4, 14]
# d = [12, 23, 23, 34]
# e = set()
# for i in a, b, c, d:
#     e.update(i)
# f = list(e)
#
#
# def look_list(x):
#     print(f"Список: {x}")
#     print()
#
#
# def sort_down(x):
#     print(f"Список: {sorted(x, reverse=True)}")
#     print()
#
#
# def sort_up(x):
#     print(f"Список: {sorted(x)}")
#     print()
#
#
# def search_element(x):
#     find_number = int(input("Введите число для поиска: "))
#     left = 0
#     right = len(x) - 1
#     s = sorted(x)
#     while left <= right:
#         midle = (left + right) // 2
#         if s[midle] == find_number:
#             print(f"Элемент {find_number} найден в списке")
#             print()
#             return
#         elif s[midle] < find_number:
#             left = midle + 1
#         else:
#             right = midle - 1
#     print(f"Элемент {find_number} не найден в списке")
#     print()
#
#
# def main():
#     global f
#     while True:
#         answer = input(f"Mеню:\n"
#                        f"1 - Посмотреть список\n"
#                        f"2 - Отсортировать по убыванию\n"
#                        f"3 - Отсортировать по возрастанию\n"
#                        f"4 - Найти значение\n"
#                        f"0 - Выход\n")
#         if answer == "1":
#             look_list(f)
#         elif answer == "2":
#             sort_down(f)
#         elif answer == "3":
#             sort_up(f)
#         elif answer == "4":
#             search_element(f)
#         elif answer == "0":
#             print("КОНЕЦ ПРОГРАММЫ!")
#             break
#         else:
#             print("*** Неверные данные ***")
#             print()
#
#
# main()

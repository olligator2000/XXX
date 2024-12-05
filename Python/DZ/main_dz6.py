# ######################################################## Это доделал последнюю задачу с урока в четверг
# number_list = []
# while True:
#     number = input(f"Введите элемент: ")
#     if number == 'стоп':
#         break
#     number_list.append(int(number))
#
# sum_otricat = [i for i in number_list if i < 0]     #Сумма отрицательных чисел
#
# sum_chet = [i for i in number_list if i % 2 == 0]   #Сумма четных чисел
#
# sum_nechet = [i for i in number_list if i % 2 == 1] #Сумма нечетных чисел
#
# umnogenie_3 = 1                                     #Произведение эл.с индексами кратным 3
# for i in number_list:
#     if i % 3 == 0:
#         umnogenie_3 *= i
#
# umnogenie_min_max = min(number_list) * max(number_list) #Произведение между мин и макс элементом
#
# for i in range(len(number_list)):                       #Находим первый положительный индекс
#     if number_list[i] > 0:
#         start_index = i
#         break
# number_list.reverse()                                   #Делаем реверс списка
# for a in range(len(number_list)):                       #Находим первый положительный индекс с конца
#     if number_list[a] > 0:
#         end_index = a
#         break
# number_list.reverse()                                   #Делаем реверс списка обратно
# sum_start_end = 0
# for j in number_list[start_index: len(number_list) - end_index: 1]:     #Сумма элекментов между первым и последним положительным элементом
#     sum_start_end += j
#
# print(f"Сумма отрицательных чисел =: {sum(sum_otricat)} \n"
#     f"Сумма четных чисел =: {sum(sum_chet)} \n"
#     f"Сумма нечетных чисел =: {sum(sum_nechet)} \n"
#     f"Произведение эл.с индексами кратным 3: {umnogenie_3} \n"
#     f"Произведение между мин и макс элементом: {umnogenie_min_max} \n"
#     f"Сумма элекментов между первым и последним положительным элементом: {sum_start_end}")

######################################################## 1
# Пользователь вводит с клавиатуры арифметическое выражение. Например, 23+12. Необходимо вывести на экран результат выражения.
# В нашем примере это 35. Арифметическое выражение может состоять только из трёх частей: число, операция,
# число. Возможные операции: +, -,*,/
# text = input("Input txt: ")
# for i in text:
#     if i == "+":
#         text = text.split("+")
#         print(f"Сумма чисел = {int(text[0] + text[1])}")
#     elif i == "-":
#         text = text.split("-")
#         print(f"Разница чисел = {int(text[0]) - int(text[1])}")
#     elif i == "*":
#         text = text.split("*")
#         print(f"Произведение чисел = {int(text[0]) * int(text[1])}")
#     elif i == "/":
#         text = text.split("/")
#         if text[1] == "0":
#             print("На ноль делить нельзя")
#         else:
#             print(f"Деление чисел = {int(text[0]) / int(text[1])}")

######################################################## 2
# # В списке целых, заполненном случайными числами, определить минимальный и максимальный элементы,
# # посчитать количество отрицательных элементов, посчитать количество положительных элементов, посчитать
# # количество нулей. Результаты вывести на экран.
# import random
# number = int(input(f"Введите количество чисел: "))
# number_list = []
# i = 0
# while i < number:
#     number_list.append(random.randint(-10, 10))
#     i += 1
# mini = 0
# maxi = 0
# minus = 0
# plus = 0
# nulls = 0
# for i in number_list:
#     if i < mini:
#         mini = i
#     if i > maxi:
#         maxi = i
#     if i < 0:
#         minus += 1
#     if i > 0:
#         plus += 1
#     if i == 0:
#         nulls += 1
# print(f"В списке {number_list}" "\n"
#       f"Минимальное число = {mini}" "\n"
#       f"Максимальное число = {maxi}" "\n"
#       f"Колличество отрицательных чисел = {minus}" "\n"
#       f"Колличество положительных чисел = {plus}" "\n"
#       f"Колличество нулей = {nulls}")


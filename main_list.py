# category = [15, 20, 56]
# category2 = [6]
# min(category)
# max(category)
# sum(category)
# sorted(category, reverse=True)      #Реверс списка
# category.append(100)     # Добавляем в конец списка значение
# category.extend([200, 500])     # Добавляем в конец списка несколько значений
# category.insert(1, category2)     # Заеняем элемент по индексу
# category.remove(20)     #Удаление элемента по значению при первом вхождении
# category.pop(1)     #Удаление элемента по индексу, если пустой, то последний
# category.clear()    #Удалит весь список
# category.index(15)    #Поиск индекса по значению
# category.count(15)    #Посчитает количество элементов по значению
# category.reverse()     #Меняет порядок сортировки элементов на обратный
# category.sort()     #Сортирует список по возрастанию
# category.sort(reverse=True)     #Сортирует список по убыванию
#######ГЕНЕРАТОРЫ************
from random import randint
# list2 = [2, 3, 5, 6]
# list1 = [i*i for i in range(6)]
# list1 = [i*i for i in list2]
# list1 = [i for i in list2 if i % 2 == 0]
# list1 = [i for i in list2 if i % 2 == 0]

##############################################
# n = int(input("Введите кол-во чисел: "))
# number_list = []
# for i in range(n):
#     number = int(input(f"Введите {i + 1} элемент "))
#     number_list.append(number)
# print(number_list)
##############################################
# number_list = []
# while True:
#     number = input(f"Введите элемент: ")
#     if number == 'стоп':
#         break
#     number_list.append(int(number))
# print(number_list)
##############################################
# number_list = []
# while True:
#     number = input(f"Введите элемент: ")
#     if number == 'стоп':
#         break
#     number_list.append(int(number))
# n = int(input("Введите число: "))
# print(number_list.count(n))
##############################################
# number_list = []
# while True:
#     number = input(f"Введите элемент: ")
#     if number == 'стоп':
#         break
#     number_list.append(int(number))
# print(f"Сумма всех элементов: {sum(number_list)} \n"
#       f"Среднее арифметичеяское: {sum(number_list) / len(number_list)}")

##############################################
# number_list = []
# while True:
#     number = input(f"Введите элемент: ")
#     if number == 'стоп':
#         break
#     number_list.append(int(number))
#
# sum_otricat = [i for i in number_list if i < 0]
# sum_chet = [i for i in number_list if i % 2 == 0]
# sum_nechet = [i for i in number_list if i % 2 == 1]
# umnogenie_3 = 1
# for i in number_list:
#     if i % 3 == 0:
#         umnogenie_3 *= i
# umnogenie_min_max = min(number_list) * max(number_list)
#
# sum_start_end = 0
# start_index = 0
# end_index = 0
# for i in range(len(number_list) - 1):
#     if i > 0:
#         start_index = i
#         break
# for a in range(len(number_list.reverse()) - 1):
#     if a > 0:
#         end_index = a
#         break
# for j in range(start_index, end_index):
#     sum_start_end += j
#
#
# print(f"Сумма отрицательных чисел =: {sum(sum_otricat)} \n"
#     f"Сумма четных чисел =: {sum(sum_chet)} \n"
#     f"Сумма нечетных чисел =: {sum(sum_nechet)} \n"
#     f"Произведение эл.с индексами кратным 3: {umnogenie_3} \n"
#     f"Произведение между мин и макс элементом: {umnogenie_min_max} \n"
#     f"Сумма элекментов между первым и последним положительным элементом: {sum_start_end}")

############################################## РАНДОМНОЕ ЗАПОЛНЕНИЕ СПИСКА
from random import randint
# numbers = [randint(-10,10) for i in range(10)]
# numbers = [10, -1, -2]
# print(numbers)
# first_index = None
# last_index = None
# for i in range(len(numbers)):
#     if numbers[i] > 0 and first_index is None:
#         first_index = i
#     if numbers[i] > 0:
#         last_index = i
# if first_index is not None and last_index is not None:
#     sum_between = sum(numbers[first_index + 1: last_index])
#     print(sum_between)
#     print(first_index)
#     print(last_index)
# else:
#     print(False)

#############################################
# numbers1 = [10, 3, 34]
# numbers2 = numbers1.copy()
# list(numbers1)




number_list = []
while True:
    number = input(f"Введите элемент: ")
    if number == 'стоп':
        break
    number_list.append(int(number))

############################################# 1
# Сумма списка: Напишите программу, которая принимает список чисел от пользователя и выводит их сумму
# print(sum(number_list))

############################################# 2
# Поиск минимума и максимума: Напишите программу, которая принимает список чисел от пользователя и выводит минимальное и максимальное
# значение в списке
# print(min(number_list), max(number_list))

############################################# 3
# Сортировка списка: Напишите программу, которая принимает список
# чисел от пользователя и выводит его отсортированным в порядке возрастания.
# number_list.sort()
# print(number_list)

############################################# 4
# Поиск среднего значения списка: Напишите программу, которая принимает список чисел от пользователя и выводит их среднее значение
# print(sum(number_list) / len(number_list))

############################################# 5
# Подсчет количества отрицательных и положительных чисел: Напишите программу, которая принимает список чисел от пользователя и выводит
# количество отрицательных и положительных чисел в списке
# pol = 0
# otr = 0
# for i in number_list:
#     if i > 0:
#         pol += 1
#     if i < 0:
#         otr += 1
# print(f"Количество положительных чисел равно: {pol} \n"
#       f"Количество отрицательных чисел равно: {otr}")

############################################# 6
# Умножение всех элементов списка на заданное число: Напишите программу, которая принимает список и число, а затем умножает каждый элемент
# списка на это число и выводит результат.
# n = int(input("Введите число: "))
# new = []
# for i in number_list:
#     i *= n
#     new.append(i)
# print(new)

############################################# 7
# Проверка наличия элемента в списке: Напишите программу, которая принимает список и значение элемента, а затем выводит сообщение о том,
# присутствует ли этот элемент в списке или нет.
# znak = int(input("Введите искомое значение: "))
# if number_list.count(znak) == 1:
#     print(f"Значение: {znak} присутвствует в списке")
# else:
#     print(f"Значение: {znak} отсуствует в списке")

############################################# 8
# Поиск индекса первого вхождения элемента: Напишите программу, которая принимает список и значение элемента, а затем выводит индекс первого
# вхождения этого элемента в списке.
# znak = int(input("Введите искомое значение: "))
# print(number_list.index(znak))

############################################# 9
# Сумма элементов списка с заданным шагом: Напишите программу, которая принимает список и шаг, а затем суммирует элементы списка с заданным
# шагом и выводит результат.
# znak = int(input("Введите шаг: "))
# summa = 0
# for i in number_list[::znak]:
#     summa += i
# print(summa)

############################################# 10
# Удаление элемента по значению: Напишите программу, которая принимает список и значение элемента, а затем удаляет все вхождения этого
# элемента из списка и выводит список без него
# znak = int(input("Введите значение: "))
# for i in range(len(number_list) - 1):
#     if number_list[i] == znak:
#         number_list.pop(i)
# print(number_list)

############################################# 11
# Количество повторений элемента: Напишите программу, которая принимает список и значение элемента, а затем выводит количество повторений
# этого элемента в списке. Если такого элемента нет в списке, то вывести соответствующее сообщение.
# znak = int(input("Введите значение: "))
# count = 0
# for i in number_list:
#     if i == znak:
#         count += 1
# if count == 0:
#     print("Такого значение нету в списке")
# else:
#     print(f"Количество повторений равно {count}")

############################################# 12
# Подсчет четных и нечетных чисел: Напишите программу, которая принимает список чисел от пользователя и выводит количество четных и нечетных
# # чисел в списке
# chet = 0
# nechet = 0
# for i in number_list:
#     if i % 2 == 0:
#         chet += 1
#     if i % 2 == 1:
#         nechet += 1
# print(f"Четных = {chet} \n"
#       f"Нечетных = {nechet}")

############################################# 13
# Поиск всех индексов элемента: Напишите программу, которая принимает список и значение элемента, а затем выводит все индексы этого
# элемента в новый список. Если такого элемента нет в списке, то вывести соответствующее сообщение.
# znak = int(input("Введите значение: "))
# new = []
# for i in range(len(number_list)):
#     if number_list[i] == znak:
#         new.append(i)
# if new:
#     print(new)
# else:
#     print(f"Такого элекмента нет в списке")

############################################# 14
# Сдвиг элементов списка влево: Напишите программу, которая принимает список и число, а затем сдвигает все элементы списка на указанное
# число позиций влево
# znak = int(input("Введите значение: "))
#
# for i in range(znak):
#     index = number_list.pop(0)
#     number_list.append(index)
# print(number_list)

############################################# 15
# Сдвиг элементов списка вправо: Напишите программу, которая принимает список и число, а затем сдвигает все элементы списка на указанное
# число позиций вправо
znak = int(input("Введите значение: "))

for i in range(znak):
    index = number_list.pop()
    number_list.insert(0, index)
print(number_list)

############################################# 16
# Объединение списков с сохранением порядка: Напишите программу, которая принимает несколько списков от пользователя и объединяет их в один
# список, сохраняя порядок их следования.
# number_list1 = []
# while True:
#     number1 = input(f"Введите элемент: ")
#     if number1 == 'стоп':
#         break
#     number_list1.append(int(number1))
#
#
# print(number_list + number_list1)
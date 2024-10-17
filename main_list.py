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
number_list = []
while True:
    number = input(f"Введите элемент: ")
    if number == 'стоп':
        break
    number_list.append(int(number))

sum_otricat = [i for i in number_list if i < 0]
sum_chet = [i for i in number_list if i % 2 == 0]
sum_nechet = [i for i in number_list if i % 2 == 1]
umnogenie_3 = 1
for i in number_list:
    if i % 3 == 0:
        umnogenie_3 *= i
umnogenie_min_max = min(number_list) * max(number_list)

sum_start_end = 0
start_index = 0
end_index = 0
for i in range(len(number_list) - 1):
    if i > 0:
        start_index = i
        break
for a in range(len(number_list.reverse()) - 1):
    if a > 0:
        end_index = a
        break
for j in range(start_index, end_index):
    sum_start_end += j


print(f"Сумма отрицательных чисел =: {sum(sum_otricat)} \n"
    f"Сумма четных чисел =: {sum(sum_chet)} \n"
    f"Сумма нечетных чисел =: {sum(sum_nechet)} \n"
    f"Произведение эл.с индексами кратным 3: {umnogenie_3} \n"
    f"Произведение между мин и макс элементом: {umnogenie_min_max} \n"
    f"Сумма элекментов между первым и последним положительным элементом: {sum_start_end}")

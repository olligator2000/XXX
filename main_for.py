# rub = float(input("rub: "))
# while True:
#     answer = int(input("Меню конвертер валют: \n"
#                        "1 - доллары \n"
#                        "2 - евро \n"
#                        "3 - юани \n"
#                        "4 - выход \n: "))
#     if answer == 1:
#         print(rub * 94)
#     elif answer == 2:
#         print(rub * 100)
#     elif answer == 3:
#         print(rub * 13)
#     elif answer == 4:
#         print("Выход из программы")
#         break
#     else:
#         print("")
#
#########################################################Задача 1: Вывод чисел от 1 до N
#Напишите программу, которая выводит числа от 1 до N.
# for i in range(1, int(input("Введите число n: "))):
#     print(i)

#########################################################Задача 2: Перевернуть числа от 1 до N
#Напишите программу, которая выводит числа от 1 до N в обратном порядке
# for i in range(int(input("Введите число n: ")), 0, -1):
#     print(i)

#########################################################Задача 3: Сумма чисел
# Напишите программу, которая считает сумму всех чисел от 1 до N (N вводит пользователь)
# sum = 0
# for i in range(1, int(input("Введите число n: "))):
#     sum += i
# print(sum)

#########################################################Задача 4: Четные и нечетные числа
# Создайте программу, которая выводит четные и нечетные числа в диапазоне от 1 до N (N вводит пользователь).
# for i in range(1, int(input("Введите число n: "))):
#     if i % 2 == 0:
#         print("Четные числа равны: ", i)
#     if i % 2 == 1:
#         print("Нечетные числа равны: ", i)

#########################################################Задача 5: Сумма четных чисел
# Напишите программу, которая вычисляет сумму всех четных чисел от 1 до N.
# sum_even = 0
# sum_odd = 0
# n = int(input("Введите число n: "))
# for i in range(1, n):
#     if i % 2 == 0:
#         sum_even += i
# for j in range(1, n):
#     if j % 2 == 1:
#         sum_odd += j
# print("Сумма четных равны: ", sum_even, "Сумма нечетных равны: ", sum_odd)

#########################################################Задача 6: Факториал числа
# Напишите программу, которая находит факториал числа N (N вводит пользователь). Факториал числа — это произведение всех чисел от 1 до N.
# factorial = 1
# n = int(input("Введите число n: "))
# for i in range(1, n):
#     factorial *= i
# print(factorial)

#########################################################Задача 7: Произведение чисел от N до M
# Напишите программу, которая находит произведение всех чисел от N до M.
# factorial = 1
# n = int(input("Введите число n: "))
# m = int(input("Введите число m: "))
# if n > m:
#     n, m = m, n
# for i in range(n, m):
#     factorial *= i
# print(factorial)

#########################################################Задача 8: Сумма квадратов чисел
# Напишите программу, которая вычисляет сумму квадратов всех чисел от 1 до N.
# sum = 0
# for i in range(1, int(input("Введите число n: ")) + 1):
#     i *= i
#     sum += i
# print(sum)

#########################################################Задача 9: Сумма чисел, кратных 3 и 5
# Напишите программу, которая находит сумму всех чисел от 1 до N, кратных 3 и 5.
# sum = 0
# for i in range(1, int(input("Введите число n: ")) + 1):
#     if i % 3 == 0 or i % 5 == 0:
#         sum += i
# print(sum)

#########################################################Задача 10: Найти наибольшее и наименьшее число
# Напишите программу, которая находит наибольшее и наименьшее число среди введенных N чисел
# mn = float("inf")
# mx = float("-inf")
# for i in range(int(input("Введите сколько раз будем вводить n чисел: "))):
#     n = int(input("Введите число: "))
#     if n < mn:
#         mn = n
#     if n > mx:
#         mx = n
# print("Минимальное число равно: ", mn, "Максимальное число равно: ", mx)

#########################################################Задача 11: Таблица умножения NxM
# Создайте программу, которая выводит таблицу умножения для чисел от N до M
# n = int(input("Введите число N: "))
# m = int(input("Введите число M: "))
# for i in range(n, m):
#     for j in range(n, m):
#         print(i * j, end="\t")
#     print("\n")

#########################################################Задача 12: Поиск первого делителя
# Напишите программу, которая находит первый делитель введенного числа N (кроме 1) и останавливается
# n = int(input("Введите N: "))
# for i in range(2, n + 1):
#     if n % i == 0:
#         print(i)
#         print("END")
#         break

#########################################################Задача 13: Поиск числа, превышающего заданную сумму
# Напишите программу, которая суммирует числа от 1 до N. Как только сумма превышает 100, программа завершает цикл и выводит текущее число.
# sum = 0
# for i in range(1, int(input("Введите число n: ")) + 1):
#     sum += i
#     if sum > 100:
#         print("END")
#         break
# print(i)

#########################################################Задача 14: Пропуск нечетных чисел
# Напишите программу, которая выводит все четные числа от 1 до N, пропуская нечетные с помощью continue.
# for i in range(1, int(input("Введите число n: ")) + 1):
#     if i % 2 == 1:
#         continue
#     print(i)

#########################################################Задача 15: Пропуск чисел, кратных 3
# Напишите программу, которая выводит числа от 1 до N, пропуская все числа, которые делятся на 3
# for i in range(1, int(input("Введите число n: ")) + 1):
#     if i % 3 == 0:
#         continue
#     print(i)

#########################################################Задача 16: Пропуск отрицательных чисел
# Напишите программу, которая вычисляет сумму только положительных чисел, введенных пользователем. Если пользователь вводит отрицательное
# число, программа игнорирует его с помощью continue.
# sum = 0
# for i in range(int(input("Введите сколько будет чисел: "))):
#     n = int(input("Введите число: "))
#     if n < 0:
#         continue
#     sum += n
# print(sum)

#########################################################Задача 17: Пирамида из символов
# Создайте программу, которая выводит пирамиду из символов *. Пользователь вводит количество строк (высоту пирамиды).
n = int(input("Введите высоту пирамиды: "))
for i in range(n + 1):
    for j in range(n + 1):
        print("\t", "*" * i)


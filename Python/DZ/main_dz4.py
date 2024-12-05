######################################Задание 1
# # Пользователь вводит с клавиатурыдва числа. Нужно посчитать отдельно сумму четных, нечетных и чисел,
# # кратных 9 в указанном диапазоне, а также среднеарифметическое каждой группы.
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# sum_even = 0
# sum_odd = 0
# sum_nine = 0
# sr_ar_even = 0
# sr_ar_odd = 0
# sr_ar_nine = 0
# counter_even = 0
# counter_odd = 0
# counter_nine = 0
# if num1 > 0 and num2 > 0:             #Работаем только с числами больше 0
#     if num1 > num2:                   #Меняем вводные числа, если первое больше второго
#         num1, num2 = num2, num1
#     while num1 <= num2:               #Пока первое число меньше второго выполняем код ниже
#         if num1 % 2 == 0:             #Оставляем для работы четные числа
#             if num1 % 9 == 0:         #Оставляем для работы числа кратные 9
#                 sum_nine += num1      #Считаем сумму чисел кратных 9
#                 counter_nine += 1     #Считаем количество чисел кратных 9
#             sum_even += num1          #Считаем сумму четных чисел
#             counter_even += 1         #Считаем количество четных чисел
#             if num1 == num2:          #Сравниваем числа, чтобы счетчик не выходил за пределы диапазона
#                 break
#             else:
#                 num1 += 1             #Прибавляем счетчик
#         if num1 % 2 == 1:             #Оставляем для работы нечетные числа
#             if num1 % 9 == 0:         #Оставляем для работы числа кратные 9
#                 sum_nine += num1      #Считаем сумму чисел кратных 9
#                 counter_nine += 1     #Считаем количество чисел кратных 9
#             sum_odd += num1           #Считаем сумму нечетных чисел
#             counter_odd += 1          #Считаем количество нечетных чисел
#             if num1 == num2:          #Сравниваем числа, чтобы счетчик не выходил за пределы диапазона
#                 break
#             else:
#                 num1 += 1             #Прибавляем счетчик
#     try:
#         sr_ar_even = sum_even / counter_even      #Считаем среднее арифметическое четных чисел
#     except ZeroDivisionError:                     #Если сумма чисел равна 0 перехыватываем ошибку и оставляем 0
#         counter_even = 0
#     try:
#         sr_ar_odd = sum_odd / counter_odd         #Считаем среднее арифметическое нечетных чисел
#     except ZeroDivisionError:                     #Если сумма чисел равна 0 перехыватываем ошибку и оставляем 0
#         counter_odd = 0
#     try:
#         sr_ar_nine = sum_nine / counter_nine      #Считаем среднее арифметическое чисел кратных 9
#     except ZeroDivisionError:                     #Если сумма чисел равна 0 перехыватываем ошибку и оставляем 0
#         counter_nine = 0
#     print('\n', "Количество четных чисел = ", counter_even, '\n', "Количество нечетных чисел = ", counter_odd, '\n',
#           "Количество кратных 9 чисел = ", counter_nine,
#           '\n', "Cумма четных чисел = ", sum_even, '\n', "Cумма нечетных чисел = ", sum_odd, '\n',
#           "Cумма кратных 9 чисел = ", sum_nine,
#           '\n', "Cреднеарифметическое четных чисел = ", sr_ar_even, '\n', "Cреднеарифметическое нечетных чисел = ",
#           sr_ar_odd, '\n',
#           "Cреднеарифметическое кратных 9 чисел = ", sr_ar_nine)
# else:
#     print("Числа должны быть больше нуля")

#####################################Задание 2
# Пользователь вводит с клавиатуры длину линии и символ для заполнения линии. Нужно отобразить на экране вертикальную линию из введенного символа,
# указанной длины. Например, если было введено 5 и символ %, тогда вывод на экран будет такой:
# line = int(input("Введите длину линиии: "))
# symbol = input("Введите символ: ")
# i = 0
# while i < line:
#     print(symbol)
#     i += 1

#####################################Задание 3
# Пользователь вводит с клавиатурычисла. Если число больше нуля нужно вывести надпись «Numberis positive», если меньше нуля «Numberis negative», если равно нулю
# «Number is equal to zero». Когда пользователь вводит число 7 программа прекращает свою работу и выводит на экран надпись «Good bye!»
# num = int(input("Введите число: "))
# while True:
#     if num > 0:
#         if num == 7:
#             print("Good bye!")
#             break
#         print("Numberis positive")
#         break
#     elif num < 0:
#         print("Numberis negative")
#         break
#     elif num == 0:
#         num += 1
#         print("Number is equal to zero")
#         break

# #####################################Задание 4
# # Пользователь вводит с клавиатуры числа. Программа должна подсчитывать сумму, максимум и минимум, введенных чисел. Когда пользователь вводит число 7
# # программа прекращает свою работу и выводит на экран надпись «Good bye!»
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = int(input("Введите третье число: "))
# num4 = int(input("Введите четвертое число: "))
# num5 = int(input("Введите пятое число: "))
# amount = 0
# min_num = 0
# max_num = 0
# while True:
#     if num1 and num2 and num3 and num4 and num5 == 7:                       #Если одно из чисел равно 7, программа прекращает работу
#         print("Good bye!")
#         break
#     amount = num1 + num2 + num3 + num4 + num5                               #Считаем сумму чисел
#     if num1 > 0 and num2 > 0 and num3 > 0 and num4 > 0 and num5 > 0:        #Работаем с числами больше 0
#         if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:     #Находим максимальное число через num1
#             max_num = num1
#         elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:   #Находим максимальное число через num2
#             max_num = num2
#         elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:   #Находим максимальное число через num3
#             max_num = num3
#         elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:   #Находим максимальное число через num4
#             max_num = num4
#         elif num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4:   #Находим максимальное число через num5
#             max_num = num5
#         if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:     #Находим минимальное число через num1
#             min_num = num1
#         elif num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5:   #Находим минимальное число через num2
#             min_num = num2
#         elif num3 < num1 and num3 < num2 and num3 < num4 and num3 < num5:   #Находим минимальное число через num3
#             min_num = num3
#         elif num4 < num1 and num4 < num2 and num4 < num3 and num4 < num5:   #Находим минимальное число через num4
#             min_num = num4
#         elif num5 < num1 and num5 < num2 and num5 < num3 and num5 < num4:   #Находим минимальное число через num5
#             min_num = num5
#         print('\n', "Сумма чисел равна: ", amount, '\n', "max = ", max_num, '\n', "min = ", min_num)
#         break
#     else:
#         print("Должны быть числа натуральные и больше 0")
#         break
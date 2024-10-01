# import random
# import tkinter
#
#
# bot_number = random.randint(1, 10)
# user_number = int(input("Введите число 1- 10: "))
# counter = 1
# while user_number != bot_number:
#     if user_number > bot_number:
#         print("Введите число поменьше")
#     else:
#         print("Введите число побольше")
#     user_number = int(input("Введите число 1- 10: "))
#     counter += 1
#
# else:
#     print("Вы угадали число", bot_number)
################################
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# while num1 <= num2:
#     if num1 % 2 == 0:
#         print(num1)
#     num1 += 1
# else:
#     print("End")
################################
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# while num1 <= num2:
#     if num1 % 2 == 1:
#         print(num1)
#     num1 += 1
# else:
#     print("End")
################################
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# while num2 >= num1:
#     print(num2)
#     num2 -= 1
# else:
#     print("End")
################################
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# if num1 > num2:
#     num1, num2 = num2, num1
# while num1 <= num2:
#     if num1 % 2 == 1:
#         print(num1)
#     num1 += 1
# else:
#     print("End")

################################
# num1 = int(input("Введите число: "))
# sum1 = 1
# sum2 = 1
# while sum1 <= num1:
#     sum2 *= sum1
#     sum1 += 1
# print(sum2)
################################
# num1 = int(input("Введите число: "))
# sum = 0
# while sum < num1:
#     print("*", end = " ")
#     sum += 1
################################
# num = int(input("Введите число: "))
# symbol = input("Введите символ: ")
# sum = 0
# while sum < num:
#     print(symbol, end="")
#     sum += 1
################################
# num = int(input("Введите число: "))
# symbol = input("Введите символ: ")
# while num > 0:
#     print(symbol * num)
#     num -= 1
################################
# num = int(input("Введите число: "))
# i = 1
# while i < 10:
#     print(num, "+", i, "=", num * i)
#     i += 1
################################
num = input("Введите валюту какая у вас имеется: 1 - доллары, 2 - евро, 3 - рубли: ")
num = input("Введите валюту в какую конвертировать: 1 - доллары, 2 - евро, 3 - рубли: ")

num = int(input("Введите число: "))

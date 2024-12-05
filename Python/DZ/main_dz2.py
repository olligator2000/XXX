#---------------------------------------------- Задание 1
# Пользователь вводит с клавиатуры число в диапазоне от 1 до 100. Если число кратно 3 (делится на 3 без
# остатка) нужно вывести слово Fizz. Если число кратно 5
# нужно вывести слово Buzz. Если число кратно 3 и 5 нужно
# вывести Fizz Buzz. Если число не кратно не 3 и 5 нужно
# вывести само число.
# Если пользователь ввел значение не в диапазоне от 1
# до 100 требуется вывести сообщение об ошибке.
# a = int(input("Введите число в диапазоне от 1 до 100: "))
# if 0 < a <= 100:
#     if a % 3 == 0 and a % 5 == 0:
#         print("Fizz Buzz")
#     elif a % 3 == 0:
#         print("Fizz")
#     elif a % 5 == 0:
#         print("Buzz")
#     elif a % 3 != 0 or a % 5 != 0:
#         print(a)
# else:
#     print("Error")

#---------------------------------------------- Задание 2
# Написать программу, которая по выбору пользователя возводит введенное им число в степень от нулевой
# до седьмой включительно.
# num = int(input("Введите число: "))
# degree = int(input("Введите степень от 0 до 7: "))
# if degree == 0:
#     print(num ** 0)
# elif degree == 1:
#     print(num ** 1)
# elif degree == 2:
#     print(num ** 2)
# elif degree == 3:
#     print(num ** 3)
# elif degree == 4:
#     print(num ** 4)
# elif degree == 5:
#     print(num ** 5)
# elif degree == 6:
#     print(num ** 6)
# elif degree == 7:
#     print(num ** 7)
# else:
#     print("Error")

#---------------------------------------------- Задание 3
# Написать программу подсчета стоимости разговора для разных мобильных операторов. Пользователь вводит
# стоимость разговора и выбирает с какого на какой оператор он звонит. Вывести стоимость на экран
# mts_inside = 2.2
# mts_other = 4.5
# beeline_inside = 2.3
# beeline_other = 4.2
# t2_inside = 2.5
# t2_other = 4
# megafon_inside = 2.7
# megafon_other = 3.5
# minutes = int(input("Введите сколько минут нужно для общения: "))
# operators_out = int(input("Выберите оператора для исходящего звонка. 1 - mts, 2 - beeline, 3 - t2, 4 - megafon: "))
# operators_in = int(input("Выберите оператора для входящего звонка. 1 - mts, 2 - beeline, 3 - t2, 4 - megafon: "))
# if (operators_out == 1) and (operators_in == 1):
#     print("Стоимость за", minutes, "минут разговора равна", mts_inside * minutes, "руб.") #Считаем стоимость для звонков внутри сети mts
# elif (operators_out == 1) and (operators_in == 2 or 3 or 4):
#     print("Стоимость за", minutes, "минут разговора равна", mts_other * minutes, "руб.") #Считаем стоимость для звонков вне сети mts
# elif (operators_out == 2) and (operators_in == 2):
#     print("Стоимость за", minutes, "минут разговора равна", beeline_inside * minutes, "руб.") #Считаем стоимость для звонков внутри сети beeline
# elif (operators_out == 2) and (operators_in == 1 or 3 or 4):
#     print("Стоимость за", minutes, "минут разговора равна", beeline_other * minutes, "руб.") #Считаем стоимость для звонков вне сети beeline
# elif (operators_out == 3) and (operators_in == 3):
#     print("Стоимость за", minutes, "минут разговора равна", t2_inside * minutes, "руб.") #Считаем стоимость для звонков внутри сети t2
# elif (operators_out == 3) and (operators_in == 1 or 2 or 4):
#     print("Стоимость за", minutes, "минут разговора равна", t2_other * minutes, "руб.") #Считаем стоимость для звонков вне сети t2
# elif (operators_out == 4) and (operators_in == 4):
#     print("Стоимость за", minutes, "минут разговора равна", megafon_inside * minutes, "руб.") #Считаем стоимость для звонков внутри сети megafon
# elif (operators_out == 4) and (operators_in == 1 or 2 or 3):
#     print("Стоимость за", minutes, "минут разговора равна", megafon_other * minutes, "руб.") #Считаем стоимость для звонков вне сети megafon

#---------------------------------------------- Задание 4
# Зарплата менеджера составляет 200$ + процент от продаж, продажи до 500$ — 3%, от 500 до 1000 — 5%, свыше 1000 — 8%. Пользователь вводит с клавиатуры уровень
# продаж для трех менеджеров. Определить их зарплату, определить лучшего менеджера, начислить ему премию 200$, вывести итоги на экран.
salary = 200
percent_1 = 3
percent_2 = 5
percent_3 = 8
salary_manager_1 = 0
salary_manager_2 = 0
salary_manager_3 = 0
sales_manager_1 = int(input("Введите сумму продаж первого менеджера: "))
sales_manager_2 = int(input("Введите сумму продаж второго менеджера: "))
sales_manager_3 = int(input("Введите сумму продаж третьего менеджера: "))
if sales_manager_1 <= 500:
    salary_manager_1 = salary + (sales_manager_1 / 100 * percent_1)
elif sales_manager_1 > 500 or sales_manager_1 <= 1000:
    salary_manager_1 = salary + (sales_manager_1 / 100 * percent_2)
elif sales_manager_1 > 1000:
    salary_manager_1 = salary + (sales_manager_1 / 100 * percent_3)
else:
    print("Error1")
if sales_manager_2 <= 500:
    salary_manager_2 = salary + (sales_manager_2 / 100 * percent_1)
elif sales_manager_2 > 500 or sales_manager_1 <= 1000:
    salary_manager_2 = salary + (sales_manager_2 / 100 * percent_2)
elif sales_manager_2 > 1000:
    salary_manager_2 = salary + (sales_manager_2 / 100 * percent_3)
else:
    print("Error2")
if sales_manager_3 <= 500:
    salary_manager_3 = salary + (sales_manager_3 / 100 * percent_1)
elif sales_manager_3 > 500 or sales_manager_1 <= 1000:
    salary_manager_3 = salary + (sales_manager_3 / 100 * percent_2)
elif sales_manager_3 > 1000:
    salary_manager_3 = salary + (sales_manager_3 / 100 * percent_3)
else:
    print("Error3")

if salary_manager_1 > salary_manager_2 and salary_manager_3:
    salary_manager_1 += 200
    print("Лучший менеджер №1, его ЗП равна", salary_manager_1, "ЗП менеджера №2 равна", salary_manager_2,
          "ЗП менеджера №3 равна", salary_manager_3)
elif salary_manager_2 > salary_manager_1 and salary_manager_3:
    salary_manager_2 += 200
    print("Лучший менеджер №2, его ЗП равна", salary_manager_2, "ЗП менеджера №1 равна", salary_manager_1,
          "ЗП менеджера №3 равна", salary_manager_3)
elif salary_manager_3 > salary_manager_1 and salary_manager_2:
    salary_manager_3 += 200
    print("Лучший менеджер №3, его ЗП равна", salary_manager_3, "ЗП менеджера №1 равна", salary_manager_1,
          "ЗП менеджера №2 равна", salary_manager_2)



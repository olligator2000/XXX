# def hello():
#     return "Hello word"
# print(hello())

####################### Позиционные параметры

# def info(name, age):
#     print(f"Name: {name}\n"
#           f"Age: {age}")
# info("Oleg", 30)

####################### Именованные параметры

# def info(name, age):
#     print(f"Name: {name}\n"
#           f"Age: {age}")
# info(name="Oleg", age=30)

####################### Параметры по умолчанию пишем вконце
#
# def info(age, name="Unknown"):
#     print(f"Name: {name}\n"
#           f"Age: {age}")
# info(25, "Oleg")

####################### Находим среднее значение
# my_list = input(": ").split()
# num_list = [int(i) for i in my_list]
# def calculate_average(numbers):
#     total = sum(numbers)
#     average = total / len(numbers)
#     return average
# print(calculate_average(num_list))

####################### Функция для объеденения с указанным разделителем

# def merge_strings(str1, str2, sep):
#     return str1 + sep + str2
# print(f"бъедененная строка {merge_strings('Oleg', 'Anna', '+')}")

############################### 1 Напишите функцию concat_names, которая принимает на вход две
# строки - имя и фамилию, и возвращает их объединенными через пробел
# def concat_names(name, syrname, sep):
#     return name + sep + syrname
# print(concat_names(name='Oleg', syrname='Lukashov', sep=" "))

############################### 2 Напишите функцию is_palindrome, которая принимает строку и
# возвращает True, если строка является палиндромом, и False в противном случае.
# def is_palindrome(str1):
#     a = str1.lower()
#     b = str1[::-1].lower()
#     if a == b:
#         return True
#     else:
#         return False
# print(is_palindrome("Апа"))

############################### 3  Создайте функцию compute_discount, которая принимает на вход
# сумму покупки и процент скидки, а затем возвращает сумму с учетом скидки.

# def compute_discount(sum1, sale):
#     return sum1 - sum1 * sale / 100
# print(compute_discount(100, 10))

############################### 4 Напишите функцию count_words, которая принимает строку в
# качестве аргумента и возвращает количество слов в этой строке.

# def count_words(str1):
#     count1 = 1
#     for i in str1:
#         if i == " ":
#             count1 += 1
#     return count1
# print(count_words("Привет Олег, как дела?"))

############################### 5 Напишите функцию generate_random_list, которая принимает
# длину списка и диапазон случайных чисел в качестве позиционных параметров и возвращает список указанной длины, заполненный случайными
# числами из указанного диапазона
# import random
# def generate_random_list(lengs, num1, num2):
#     return [random.randint(num1, num2) for i in range(lengs)]
# print(generate_random_list(10, -10, 10))

############################### 6 Напишите функцию find_common_elements, которая принимает
# два списка и возвращает список элементов, которые есть в обоих списках

# def find_common_elements(list1, list2):
#     arr = []
#     for i in list1:
#         if i in list2 and i not in arr:
#             arr.append(i)
#     return arr
# print(find_common_elements([1, 2, 3, 8], [4, 2, 7, 8]))

############################### 7 Напишите функцию calculate_total_price, которая принимает цену
# товара и процент налога в качестве именованных параметров со значениями по умолчанию и возвращает общую стоимость товара с учетом налога

# def calculate_total_price(price, proc1 = "Unknown"):
#     return price - price * proc1 / 100
# print(f"Стоимость товара с учетом налога равна {calculate_total_price(100, proc1=10)}")

################################ 8 Напишите функцию generate_password, которая принимает длину
# пароля в качестве параметра со значением по умолчанию и возвращает случайно сгенерированный пароль указанной длины

# import random
# def generate_password(lengs="Unknown"):
#     return [random.randint(0, 10) for i in range(int(lengs))]
# print(generate_password(lengs="8"))

################################ 9 Напишите функцию, которая отображает на экран
# форматированный текст, указанный ниже:
# “Don't let the noise of others' opinions
# drown out your own inner voice.”
# Steve Jobs

# def jobs():
#     print("Don't let the noise of others opinions \n"
#             "drown out your own inner voice.\n"
#             "Steve Jobs")
# jobs()

################################ 10 Напишите функцию, которая принимает два числа
# в качестве параметра и отображает все нечетные числа между ними.

# def numbers(a, b):
#     nums = []
#     for i in range(a, b):
#         if i % 2 == 1:
#             nums.append(i)
#     return nums
# print(numbers(-10,11))

################################ 11 Напишите функцию, которая отображает горизонтальную или вертикальную линию из некоторого символа.
# Функция принимает в качестве параметра: длину линии, направление, символ
# def lines(dlina, napravlenie, symbol):
#     s = ""
#     if napravlenie == "-":
#         print(symbol*dlina)
#     if napravlenie == "|":
#         for i in range(dlina):
#             print(symbol)
# lines(dlina=5, napravlenie="-", symbol="*")

#***********  ГЛОБАЛЬНЫЕ И НЕ ГЛОБЛАЛЬНЫЕ ПЕРЕМЕННЫЕ

# x = 10
# def info():
#     global x
#     x += 10
#     print(f"глобальная переменная х: {x}")
# print(x)
# info()

########################

# def outer():
#     f = 10
#     print(f"Локальная переменная f: {f}")
#
#     def inner():
#         nonlocal f
#         f += 10
#         print(f"Не локальная переменная f: {f}")
#     inner()
#     print(f"Локальная переменная f: {f}")
# outer()

#####################               Практические задания

################################### 1
# Функция для расчета площади и периметра прямоугольника:
# Напишите функцию calculate_rectangle_properties, которая принимает длину и
# ширину прямоугольника в качестве аргументов и возвращает два значения -
# площадь и периметр этого прямоугольника.

# def calculate_rectangle_properties(a, b):
#     p = (a * 2) + (b * 2)
#     s = a * b
#     print(f"Периметр прямоугольника = {p}\n"
#           f"Площадь прямоугольника = {s}")
# calculate_rectangle_properties(4, 5)

################################### 2
# Функция для конвертации температуры: Создайте функцию
# convert_temperature, которая принимает температуру в градусах Цельсия и
# возвращает эту же температуру в градусах Фаренгейта и Кельвина.

# def convert_temperature(c):
#     return 9/5 * c + 32
# print(convert_temperature(10))

################################### 3
# Напишите программу, которая использует как локальные, так и
# глобальные переменные. Создайте глобальную переменную global_var со
# значением "global", а затем определите функцию local_function, которая
# создает локальную переменную local_var со значением "local". Выведите
# значения обеих переменных на экран
# global_var = "global"
# def local_function():
#     local_var = "local"
#     print(local_var)
# print(global_var)
# local_function()

################################### 4
# Напишите функцию outer_function, внутри которой определена
# переменная x. Затем внутри outer_function определите вложенную функцию
# inner_function, которая пытается изменить значение переменной x.
# Используйте ключевое слово nonlocal, чтобы указать, что переменная x
# находится в нелокальной области видимости.
# def outer_function():
#     x = 10
#     def inner_function():
#         nonlocal x
#         x += 100
#         print(x)
#
#     print(x)
#     inner_function()
# outer_function()

################################### 5
# Создайте глобальную переменную x и функцию outer_function,
# внутри которой определена переменная y. Затем внутри outer_function
# определите вложенную функцию inner_function, которая пытается изменить
# значения переменных x и y. Используйте ключевые слова global и nonlocal
# соответственно, чтобы указать, что переменные x и y находятся в глобальной
# и нелокальной областях видимости

# x = 10
# def outer_function():
#     global x
#     y = 20
#     def inner_function():
#         global x
#         nonlocal y
#         x += 5
#         y += 5
#
#     inner_function()
#     print(x)
#     print(y)
# outer_function()

#################################### Напишите функцию, вычисляющую произведение
# элементов списка целых. Список передаётся в качестве параметра. Полученный результат возвращается изфункци

# def proiz(list1):
#     ans = 1
#     for i in list1:
#         ans *= i
#     return ans
# print(proiz([1, 2, 3]))

############################################ Напишите функцию для нахождения минимума в
# списке целых. Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.
# def mini(list1):
#     return min(list1)
# print(mini([100, -1, 2, 10]))

############################################ Напишите функцию, определяющую количество простых чисел в списке целых. Список передаётся в качестве
# параметра.Полученныйрезультат возвращаетсяизфункции.
s = [i for i in range(0, 100)]
def prosto(list1):
    d = []
    for i in list1:
        if i < 2:
            break
        else:
            if i % 2 == 0:
                break
    else:
        d.append(i)
    return d
print(prosto(s))

############################################ Напишите функцию, удаляющую из списка целых
# некоторое заданное число. Из функции нужно вернуть количество удаленных элементов
# def delette(list1, a):
#     counts = 0
#     for i in list1:
#         if int(i) == a:
#             list1.remove(i)
#             counts += 1
#     print(list1, counts)
# delette([1,3,1,4,1], 1)

############################################ Напишите функцию, которая получает два списка в
# качестве параметра и возвращает список, содержащий элементы обоих списков.

# def spisok(a, b):
#     s1 = [i for i in a if i not in b]
#     s2 = [j for j in b if j not in a]
#     return s1 + s2
#
# print(spisok([2, 4, 5], [6, 2, 5]))

############################################ Напишитефункцию, высчитывающуюстепень каждого
# элемента списка целых. Значение для степени передаётся
# в качестве параметра, список тоже передаётся в качестве
# параметра. Функция возвращает новый список, содержащий полученные результаты

# def stepen(list1, s):
#     s = [i ** s for i in list1]
#     return s
# print(stepen([1, 2, 3], 2))


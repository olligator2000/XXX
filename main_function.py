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
def lines(dlina, napravlenie, symbol):
    for i in range(dlina):
        i += symbol
    if
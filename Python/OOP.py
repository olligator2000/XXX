# class Car:
#     default_model = "c835"  #Статические поля
#     def __init__(self, color, model, year):     #Динамические поля
#         self.color = color
#         self.model = model
#         self.year = year
#
#     def show_info(self, name):
#         print(f"Марка машины: {self.model}\n"
#               f"Цвет машины: {self.color}\n"
#               f"Год выпуска: {self.year}\n"
#               f"Модель по умолчанию: {self.default_model}\n"
#               f"Владелец: {name}")
#
# car_1 = Car("black", "Lada", 2018)
# car_2 = Car("red", "bmw", 2020)
#
# car_1.show_info("Alex")
# print()
# car_2.show_info("Oleg")

##################################### 1
# Класс "Товар": Создайте класс "Товар", который будет содержать атрибуты: название, цена и количество. Реализуйте
# методы для установки и получения значений атрибутов, а также для подсчета общей стоимости товара (цена * количество).

# class Product:
#
#     def __init__(self, name, pay, count):
#         self.name = name
#         self.pay = pay
#         self.count = count
#     def sum_unit(self):
#         summ = self.pay * self.count
#         print(summ)
#     def show_all(self):
#         print(f"Название: {self.name}\n"
#               f"Цена: {self.pay}\n"
#               f"Количество: {self.count}\n"
#               f"Общая стоимость: {self.pay * self.count}")
#
# apple = Product("Яблоко", 5, 20)
#
# apple.show_all()
# apple.sum_unit()

##################################### 2
# Класс "Круг": Напишите класс "Круг", у которого есть атрибуты радиус и цвет. Реализуйте методы для вычисления
# площади круга и его окружности

# class Circle:
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius
#
#     def square(self):
#         print(f"Площадь круга: {self.pi * self.radius ** 2}")
#
#     def long(self):
#         print(f"Длина окружности: {2 * self.pi * self.radius}")
#
#     def show_all(self):
#         print(f"Площадь круга: {self.pi * self.radius ** 2}\n"
#               f"Длина окружности: {2 * self.pi * self.radius}")
#
# circle_1 = Circle(10)
# circle_2 = Circle(20)
#
# circle_1.show_all()

##################################### 3
# Класс "Студент": Создайте класс "Студент", у которого есть атрибуты: имя, возраст и средний балл. Реализуйте метод для вывода
# информации о студенте и метод для проверки, сдал ли студент экзамен (средний балл выше 4)

# class Student:
#
#     def __init__(self, name, age, sr_bal):
#         self.name = name
#         self.age = age
#         self.sr_bal = sr_bal
#
#     def show_info(self):
#         print(f"Имя студента: {}\n"
#               f"Возраст студента: {}\n"
#               f"Средний бал")


##################################################################################################


# class Person:
#     def __init__(self,name, age):
#         self.name = name
#         self.__age = age
#
#     def info(self):
#         print(f"Имя: {self.name}\n"
#               f"Возраст: {self.__age}")
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, new_age):
#         self.__age = new_age

# person_1 = Person("Alex", 25)
# person_1.info()
# person_1.name = "Olga"
# person_1.info()
# person_1.set_age(13)
# person_1.info()

# class Rectangle:
#     def __init__(self,width, height):
#         self.__width = width
#         self.__height = height
#
#     def info(self):
#         print(f"Ширина: {self.__width}\n"
#               f"Высота: {self.__height}\n"
#               f"Площадь: {self.__width * self.__height}")
#
#     @property
#     def width(self):    #Геттер для width
#         return self.__width
#
#     @width.setter       # Сеттер для width
#     def width(self, new_width):
#         if new_width > 0:
#             self.__width = new_width
#         else:
#             print("Значение меньше нуля!")
#
#     @property
#     def height(self):  # Геттер для height
#         return self.__height
#
#     @height.setter
#     def height(self, new_height):   # Сеттер для height
#         if new_height > 0:
#             self.__height = new_height
#         else:
#             print("Значение меньше нуля!")
#
#
#
# rect = Rectangle(10, 20)
# rect.info()
# rect.width = 50
# rect.info()
# rect.height = 1000
# rect.info()

########################################################## 1
# Создайте класс "Банковский счет", который имеет приватные атрибуты
# "баланс" и "процентная ставка". Реализуйте методы для установки и
# получения значений этих атрибутов. Также добавьте метод для начисления
# процентов по счету.

# class BankSheet:
#
#     def __init__(self, balance, proc_rate):
#         self.__balance = balance
#         self.__proc_rate = proc_rate
#
#     def accrual_interest_account(self):
#         s = (self.__balance * self.__proc_rate * 365 / 365) / 100
#         print(f"Проценты по счету: {s}")
#
#     def info(self):
#         print(f"Баланс: {self.__balance}\n"
#               f"Процентная ставка: {self.__proc_rate}\n"
#               f"Начисленные проценты по счету: {(self.__balance * self.__proc_rate * 365 / 365) / 100}")
#
#     @property
#     def balance(self):
#         return self.__balance
#
#     @balance.setter
#     def balance(self, new_balance):
#         if new_balance > 0:
#             self.__balance = new_balance
#         else:
#             print("Значение меньше нуля!")
#
#     @property
#     def proc_rate(self):
#         return self.__proc_rate
#
#     @proc_rate.setter
#     def proc_rate(self, new_proc_rate):
#         if new_proc_rate > 0:
#             self.__proc_rate = new_proc_rate
#         else:
#             print("Значение меньше нуля!")
#
# sheet_1 = BankSheet(1000, 16)
# sheet_1.info()


########################################################## 2
# Создайте класс "Автомобиль", у которого есть приватные атрибуты "модель"
# и "год выпуска". Реализуйте методы для установки и получения значений
# этих атрибутов. Также добавьте метод для вывода информации об
# автомобиле.
import datetime

# class Car:
#
#     def __init__(self, model, age):
#         self.__model = model
#         self.__age = age
#
#     def info(self):
#         print(f"Модель: {self.__model}\n"
#               f"Год выпуска: {self.__age}\n")
#
#     @property
#     def model(self):
#         return self.__model
#
#     @model.setter
#     def model(self, new_model):
#         if new_model == str or 3 <= len(new_model) <= 10:
#             self.__model = new_model
#         else:
#             print("Название должно быть не меньше 3 и не более 10 символов!")
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, new_age):
#         if 1950 <= new_age <= datetime.datetime.now().year:
#             self.__age = new_age
#         else:
#             print("Неверное значение!")
#
#
# car_1 = Car("bmw", 1950)
# car_1.info()
# car_1.model = "dd"
# car_1.age = 2021
# car_1.info()

########################################################## 3
# Создайте класс "Библиотека", у которого есть приватные атрибуты
# "количество книг" и "список книг". Реализуйте методы для добавления и
# удаления книг из библиотеки, а также для вывода списка книг

class Library:

    def __init__(self):
        self.__count = 0
        self.__list_book = []

    def info(self):
        for i in self.__list_book:
            print(f"Список книг: {i}")
        print(f"Количество книг: {self.__count}")

    @property
    def list_book_add(self):
        return self.__list_book

    @list_book_add.setter
    def list_book_add(self, new_list_book):
        if type(new_list_book) == str:
            self.__list_book.append(new_list_book)
            self.__count += 1
        else:
            print("Неверное значение!")

    @property
    def list_book_del(self):
        return self.__list_book

    @list_book_del.setter
    def list_book_del(self, name_book):
        if type(name_book) == str:
            self.__list_book.remove(name_book)
            self.__count -= 1
        else:
            print("Неверное значение!")


book_1 = Library()
book_1.info()
book_1.list_book_add = "oleg"
book_1.info()
book_1.list_book_add = "dima"
book_1.info()
book_1.list_book_del = "oleg"
book_1.info()
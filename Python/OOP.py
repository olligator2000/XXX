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
#
# class Library:
#
#     def __init__(self):
#         self.__count = 0
#         self.__list_book = []
#
#     def info(self):
#         print("Список книг:")
#         for i in self.__list_book:
#             print(f"{i}")
#         print(f"Количество книг: {self.__count}")
#         print()
#
#     @property
#     def list_book_add(self):
#         return self.__list_book
#
#     @list_book_add.setter
#     def list_book_add(self, new_list_book):
#         if type(new_list_book) == str:
#             self.__list_book.append(new_list_book)
#             self.__count += 1
#         else:
#             print("Неверное значение!")
#
#     @property
#     def list_book_del(self):
#         return self.__list_book
#
#     @list_book_del.setter
#     def list_book_del(self, name_book):
#         if type(name_book) == str:
#             self.__list_book.remove(name_book)
#             self.__count -= 1
#         else:
#             print("Неверное значение!")
#
#
# book_1 = Library()
# book_1.info()
# book_1.list_book_add = "oleg"
# book_1.info()
# book_1.list_book_add = "dima"
# book_1.info()
# book_1.list_book_del = "oleg"
# book_1.info()

################################ НАСЛЕДОВАНИЕ

# class Phone:
#
#     # Инициализатор
#     def __init__(self):
#         self.is_on = False
#
#     # Включаем телефон
#     def turn_on(self):
#         self.is_on = True
#
#     # Если телефон включен, делаем звонок
#     def call(self):
#         if self.is_on:
#             print('Making call...')
#
#
# class MobilePhone(Phone):
#
#     # Добавляем новое свойство battery
#     def __init__(self):
#         super().__init__()
#         self.battery = 0
#
#     # Заряжаем телефон на величину переданного значения
#     def charge(self, num):
#         self.battery = num
#         print(f'Charging battery up to ... {self.battery}%')
#
# mobilePhone_1 = MobilePhone()
# print(dir(mobilePhone_1))
#
# #ПРоверяем является ли класс потомком родителя
# print(issubclass(MobilePhone, Phone))
# #ПРоверяем является ли объект экземпляром класса
# print(isinstance(mobilePhone_1, Phone))

#############################################

# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def drive(self):
#         print(f"{self.brand} {self.model} is driving...")
#
#
# class Car(Vehicle):
#     def __init__(self, brand, model, color, year, volume):
#         super().__init__(brand, model)
#         self.color = color
#         self.year = year
#         self.volume = volume
#
#     def reffil(self):
#         print(f"{self.volume} reffiling")
#
# class Bike(Vehicle):
#     def __init__(self, brand, model, price):
#         super().__init__(brand, model)
#         self.price = price
#
#     def ring(self):
#         print("RING! RING!")
#
# vehicle_1 = Vehicle(brand="X", model="Y")
# car_1 = Car(brand="LADA", model="VESTA", color="Red", year=2018, volume=1.6)
# bike_1 = Bike(brand="Stels", model="x12", price=10000)
#
# print(vehicle_1.brand, vehicle_1.model)
# print(car_1.brand, car_1.model, car_1.color, car_1.year, car_1.volume)
# print(bike_1.brand, bike_1.model, bike_1.price)
# car_1.drive()
# car_1.reffil()


#############################################

# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def drive(self):
#         print(f"{self.brand} {self.model} is driving...")
#
#
# class Car(Vehicle):
#     def __init__(self, brand, model, color, year, volume):
#         super().__init__(brand, model)
#         self.color = color
#         self.year = year
#         self.volume = volume
#
#     def reffil(self):
#         print(f"{self.volume} reffiling")
#
# class LightCar(Car):
#     def __init__(self, brand, model, color, year, volume, price):
#         super().__init__(brand, model, color, year, volume)
#         self.price = price
#
#     def ring(self):
#         print("RING! RING!")
#
# vehicle_1 = Vehicle(brand="X", model="Y")
# car_1 = Car(brand="LADA", model="VESTA", color="Red", year=2018, volume=1.6)
# lc_1 = LightCar(brand="LADA", model="VESTA", color="Red", year=2018, volume=1.6, price=20000)
#
# print(vehicle_1.brand, vehicle_1.model)
# print(car_1.brand, car_1.model, car_1.color, car_1.year, car_1.volume)
# print(lc_1.brand, lc_1.model, lc_1.color, lc_1.year, lc_1.volume, lc_1.price)

########################################### 1
# Создайте класс Human, который будет содержать информацию о человеке. Спомощью механизма наследования, реализуйте класс
# Builder (содержит информацию о строителе), класс Sailor (содержит информацию о моряке), класс Pilot (содержит
# информацию о летчике). Каждый из классов должен содержать необходимые для работы методы

# class Human:
#     def __init__(self, gender, age):
#         self.gender = gender
#         self.age = age
#
#     def live(self):
#         print(f"{self.gender} {self.age}  is living...")
#
# class Builder(Human):
#     def __init__(self, gender, age, name, post, experience):
#         super().__init__(gender, age)
#         self.name = name
#         self.post = post
#         self.experience = experience
#
#     def build(self):
#         print(f"{self.post} build...")
#
# class Sailor(Human):
#     def __init__(self, gender, age, name, rank, experience):
#         super().__init__(gender, age)
#         self.name = name
#         self.rank = rank
#         self.experience = experience
#
#     def attire(self):
#         print(f"{self.rank} wash floors...")
#
# class Pilot(Human):
#     def __init__(self, gender, age, name, rank, flight_hours):
#         super().__init__(gender, age)
#         self.name = name
#         self.rank = rank
#         self.experience = flight_hours
#
#     def attire(self):
#         print(f"{self.rank} controls the plane...")
#
# builder_1 = Builder(gender="Men", age=40, name="Oleg", post="Прораб", experience=15)
# print(builder_1.gender, builder_1.age, builder_1.name, builder_1.post, builder_1.experience)
#
# sailor_1 = Sailor(gender="Men", age=40, name="Alex", rank="Юнга", experience=1)
# print(sailor_1.gender, sailor_1.age, sailor_1.name, sailor_1.rank, sailor_1.experience)
#
# pilot_1 = Pilot(gender="Women", age=40, name="Olga", rank="Капитан", flight_hours=15000)
# print(pilot_1.gender, pilot_1.age, pilot_1.name, pilot_1.rank, pilot_1.experience)
#

# Задание 2
# Создайте класс Passport (паспорт), который будет
# содержать паспортную информацию о гражданине заданной страны.
# С помощью механизма наследования, реализуйте
# класс ForeignPassport (загран.паспорт) производный от
# Passport.
# Напомним, что заграничный паспорт содержит помимо паспортных данных, также данные о визах, номер
# заграничного паспорта.
# Каждый из классов должен содержать необходимые
# методы.
#
#
# Задание 3
# Создать базовый класс «Животное» и производные
# классы «Тигр», «Крокодил», «Кенгуру». С помощью конструктора установить имя каждого животного и его характеристики. Создайте для каждого класса необходимые
# методы и поля.



#################################### ПОСЛЕДОВАТЕЛЬНОСТЬ

# class A:
#     def action(self):
#         print("Action A")
#
# class B(A):
#     def action(self):
#         print("Action B")
#
# class C(A):
#     def action(self):
#         print("Action C")
#
# class D(B, C):
#     pass
#
# d = D()
# d.action()

#################################### КОМПОЗИЦИЯ

# class Engine:
#     def start(self):
#         print("Engine starts...")
#
#     def stop(self):
#         print("Engine stops...")
# class Car:
#     def __init__(self):
#         self.engine = Engine()
#
#     def drive(self):
#         self.engine.start()
#         print("Car is driving")
#
#     def stop(self):
#         self.engine.stop()
#         print("Car stoped")
#
# engine = Engine()
# car = Car()
# car.drive()
# car.stop()

####################################### 2
# Компьютер и его компоненты
# Ситуация: Компьютер состоит из процессора, оперативной памяти и
# видеокарты. Каждый компонент — это отдельный класс.


# class CPU:
#     def __init__(self, brend, cores):
#         self.brand = brend
#         self.cores = cores
#
#     def info(self):
#         return f"CPU: {self.brand}, Cores: {self.cores}"
#
# class RAM:
#     def __init__(self, size):
#         self.size = size
#
#     def info(self):
#         return f"RAM: {self.size}Gb"
#
# class GPU:
#     def __init__(self, brend, memory):
#         self.brand = brend
#         self.memory = memory
#
#     def info(self):
#         return f"GPU: {self.brand} Memory: {self.memory}"
#
# class PC:
#     def __init__(self):
#         self.cpu = CPU("Intel", 5)
#         self.ram = RAM(16)
#         self.gpu = GPU("nVIDIA", 4)
#
#     def info_details(self):
#         return f"{self.cpu.info()} \n" \
#                f"{self.ram.info()} \n" \
#                f"{self.gpu.info()}"
#
# computer_1 = PC()
# print(computer_1.info_details())

###############################
###############################
###############################
#Практические задания
############################### 1
# Система управления инвентарем. Создайте класс Inventory,
# который содержит методы add_item, remove_item и get_inventory_value. Также
# создайте статические методы calculate_item_value и validate_item. Используйте
# эти статические методы внутри обычных методов для выполнения
# вспомогательных операций.

# class Inventory:
#     def __init__(self):
#         self.item = {}
#
#     def add_item(self, name, price, quantity):
#         if Inventory.validate_item(name, price, quantity):
#             if name in self.item:
#                 self.item[name]['Количество'] += quantity
#             else:
#                 self.item[name] = {'Цена': price, 'Количество': quantity}
#         else:
#             print('Некорректные данные!')
#
#     def remove_item(self, name, price, quantity):
#         if name in self.item and self.item[name]['Количество'] >= quantity:
#             self.item[name]['Количество'] -= quantity
#             if self.item[name]['Количество'] == 0:
#                 del self.item[name]
#         else:
#             print(f'Невозможно удалить {quantity} единиц {name}')
#
#     def get_inventory_value(self):
#         total_value = 0
#         for details in self.item.values():
#             total_value += Inventory.calculate_item_value(details['Цена'], details['Количество'])
#         return total_value
#
#     @staticmethod
#     def calculate_item_value(price, quantity):
#         return price * quantity
#
#     @staticmethod
#     def validate_item(name, price, quantity):
#         return isinstance(name, str) and price > 0 and quantity > 0
#
# inv_1 = Inventory()
# inv_1.add_item('Molotok', 1, 10)
# inv_1.add_item('Kosa', 1, 10)
# print(inv_1.get_inventory_value())

############################################################
# from datetime import date
#
# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def from_date(cls, name, bd):
#         current_year = date.today().year
#         age = current_year - bd
#         return cls(name, age)
#
#
# person_1 = Person('Alex', 30)
# print(person_1.name, person_1.age)
#
# person_2 = Person('Oleg', 1984)
# print(person_2.name, person_2.age)

############################################################

# class User:
#
#     MIN_AGE = 18
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def is_valid_user(cls, age):
#         return age >= cls.MIN_AGE
#
# print(User.is_valid_user(15))
# print(User.is_valid_user(20))

############################################################ 1
# Создайте класс Student с методом класса from_dict, который создает
# экземпляр студента из словаря с ключами 'name', 'age' и 'grade'

# class Student:
#
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#
#     @classmethod
#     def from_dict(cls, data_student):
#         return cls(data_student['name'],
#                    data_student['age'],
#                    data_student['grade']
#                    )
#
# data = {'name': 'Alex', 'age': 30, 'grade': 5}
# std = Student.from_dict(data)
# print(std.name)

############################################################ 2
# Создайте класс Pizza с методом класса margherita и pepperoni, которые
# создают объекты пиццы с фиксированными ингредиентами

class Pizza:
    def __init__(self, name, size, dough, sauce, vegetables, cheese, herbs, sausage):
        self.name = name
        self.size = size
        self.dough = dough
        self.sauce = sauce
        self.vegetables = vegetables
        self.cheese = cheese
        self.herbs = herbs
        self.sausage = sausage

    @classmethod
    def margherita(cls):
        return cls("margherita", 45, "тесто-хрустящее", "соус-фигоус", "овощи-помидоры", "сыр-мацарелла", "травы-итальянские")

    @classmethod
    def pepperoni(cls):
        return cls("pepperoni", 45, "тесто-хрустящее", "колбаски-пепперони")

    def info(self):
        print(f"Название: {self.name}"
              f"Размер: {self.size}"
              f"Тесто: {self.dough}"
              f"Соус: {self.sauce}"
              f"Овощи: {self.vegetables}"
              f"Сыр: {self.cheese}"
              f"Травы: {self.herbs}"
              f"Колбаски: {self.sausage}")


pizza_1 = Pizza("Три сыра", 45, "Хрустящее", "Сливочный", "Помидоры", "Венский")
pizza_1.info()
pizza_2 = Pizza()


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

class Student:

    def __init__(self, name, age, sr_bal):
        self.name = name
        self.age = age
        self.sr_bal = sr_bal

    def show_info(self):
        print(f"Имя студента: {}\n"
              f"Возраст студента: {}\n"
              f"Средний бал")
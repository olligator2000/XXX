# class OrderQueue:
#     def __init__(self):
#         self.queue = []
#
#     def add_order(self, order):
#         self.queue.append(order)
#         print("Заказ принят")
#
#     def is_empty(self):
#         print("Очередь еще есть") if len(self.queue) != 0 else print("NO")
#         return len(self.queue) == 0
#
#     def process_order(self):
#         if self.is_empty():
#             return "Заказов нет"
#         order = self.queue.pop(0)
#         return f"Заказ {order} готов"
#
#     def display_orders(self):
#         return f"Список заказов {self.queue}"
#
# orders = OrderQueue()
#
# #Добавление
# orders.add_order("Пицца")
# orders.add_order("Бургер")
# orders.add_order("Колла")
#
# #Просмотр
# print(orders.display_orders())
#
# #Выполнение
# orders.process_order()
#
# #Просмотр
# print(orders.display_orders())

#Проверка
# orders.is_empty()

###################################################### библиотека COLLECTION
# from collections import deque
#
#
# class OrderQueue:
#     def __init__(self):
#         self.queue = deque()
#
#     def add_order(self, order):
#         self.queue.append(order)
#         print("Заказ принят")
#
#     def is_empty(self):
#         print("Очередь еще есть") if len(self.queue) != 0 else print("NO")
#         return len(self.queue) == 0
#
#     def process_order(self):
#         if self.is_empty():
#             return "Заказов нет"
#         order = self.queue.popleft()
#         return f"Заказ {order} готов"
#
#     def display_orders(self):
#         return f"Список заказов: {','.join([i for i in self.queue])}"
#
# orders = OrderQueue()
#
# #Добавление
# orders.add_order("Пицца")
# orders.add_order("Бургер")
# orders.add_order("Колла")
#
# #Просмотр
# print(orders.display_orders())
#
# #Выполнение
# orders.process_order()
#
# #Просмотр
# print(orders.display_orders())

###################################################### 2.
# Очередь в банке
# Создайте класс BankQueue, который моделирует очередь клиентов в банке. Класс должен иметь методы для добавления клиента
# в очередь (enqueue), обслуживания клиента (dequeue) и просмотра следующего клиента в очереди (peek). Также добавьте метод для
# отображения текущего состояния очереди (display_queue).
# from collections import deque
#
#
# class BankQueue:
#     def __init__(self):
#         self.queue = deque()
#
#     def enqueue(self, client):
#         self.queue.append(client)
#         print(f'Клиент {[i for i in self.queue]} добавлен')
#         print()
#
#     def is_empty(self):
#         print("Очередь еще есть") if len(self.queue) != 0 else print("NO")
#         return len(self.queue) == 0
#
#     def dequeue(self):
#         if self.is_empty():
#             return "Клиентов нет"
#         client = self.queue.popleft()
#         return f"Клиент {client} обслужен"
#
#     def peek(self):
#         return f"Следующий клиент: {self.queue[0]}"
#
#     def display_queue(self):
#         return f"Список клиентов: {[i for i in self.queue]}"
#
#
# clients = BankQueue()
#
#
# def main():
#     while True:
#         menu = input(f"Главное меню:\n"
#                      "1 - Добавить клиента\n"
#                      "2 - Обслужить клиента\n"
#                      "3 - Просмотра следующего клиента в очереди\n"
#                      "4 - Отображения текущего состояния очереди\n"
#                      "0 - Выход\n"
#                      "Выбор: ")
#
#         if menu == "1":
#             clients.enqueue(input("Введите id клиента: "))
#         elif menu == "2":
#             clients.dequeue()
#         elif menu == "3":
#             print(clients.peek())
#         elif menu == "4":
#             print(clients.display_queue())
#         elif menu == "0":
#             print("*** ВЫХОД ***")
#             break
#         else:
#             print("Неверные данные")
#
#
# main()

###################################################### 3
# Обработка запросов к серверу
# Создайте систему обработки запросов к серверу. Запросы
# добавляются в очередь по мере их поступления, и сервер
# обрабатывает их по очереди. Напишите класс ServerQueue с методами
# для добавления запроса, обработки запроса и отображения текущей
# очереди запросов
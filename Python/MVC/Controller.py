# from Model import Product
# from View import ProductView
#
#
# class ProductController:
#     def __init__(self, model, view):
#         self.model = model
#         self.view = view
#
#     def set_discount(self, percentage):
#         self.model.apply_discount(percentage)
#         self.view.show_discount(percentage)
#         self.view.show_product(self.model)
#
#
# #Создание модели
# product = Product("Laptop", 1500.00)
#
# #Создание представления
# view = ProductView()
#
# #Создание контроллера
# controller = ProductController(product, view)
#
# #Отображение продукта до применения скидки
# view.show_product(product)
#
# #Применение скидки через контроллер
# controller.set_discount(10)



###################################################################################

from Model import Book, Library
from View import LibraryView


class LibraryController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_book(self, title, author, year):

        title, author, year = self.view.get_book_details()
        book = Book(title, author, year)
        if title and author and year in Library():
            print("Такая книга уже существует!")
            return
        self.model.add_book(book)
        self.view.show_message("Книга добавлена")

    def view_books(self):
        books = self.model.get_books()
        self.view.show_books(books)

    def find_books(self):
        title = self.view.get_search_book()
        books = self.model.find_books_by_title(title)
        self.view.show_books_search(books)



def main():
    library = Library()
    view = LibraryView()
    controller = LibraryController(library, view)

    while True:
        choice = input(f"Меню: \n"
                       f"1 - Добавить книгу\n"
                       f"2 - Просмотреть все книги\n"
                       f"3 - Найти книгу по названию\n"
                       f"4 - Выход\n"
                       f"Выбирите пункт: ")

        if choice == "1":
            controller.add_book()
        elif choice == "2":
            controller.view_books()
        elif choice == "3":
            controller.find_books()
        elif choice == "4":
            break
        else:
            view.show_message("Неверный ввод")

main()
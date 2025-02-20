# class ProductView:
#     def show_product(self, product):
#         print(f"Product: {product.name}")
#         print(f"Price: {product.price:.2f}")
#
#     def show_discount(self, discount):
#         print(f"Discount applied: {discount}%")

###################################################################################

class LibraryView:
    def show_books(self, books):
        if not books:
            print("Библиотека пуста\n")
            return
        for book in books:
            print(f"Загловок: {book.title}\n"
                  f"Автор: {book.author}\n"
                  f"Год выпуска: {book.year}\n")

    def show_books_search(self, books):
        if not books:
            print("Такой книги нет\n")
            return
        for book in books:
            print(f"Загловок: {book.title}\n"
                  f"Автор: {book.author}\n"
                  f"Год выпуска: {book.year}\n")


    def show_message(self, message):
        print(message)

    def get_book_details(self):
        title = input("Введите название книги: ")
        author = input("Введите имя автора книги: ")
        year = input("Введите год выпуска книги: ")
        return title, author, year

    def get_search_book(self):
        return input("Введите название книги для поиска: ")

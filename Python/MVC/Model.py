# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def apply_discount(self, percentage):
#         self.price -= self.price * (percentage / 100)



###################################################################################



class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books

    def find_books_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]


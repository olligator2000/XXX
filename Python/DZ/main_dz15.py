############################################### 1
# Создайте программу «Книжная коллекция». Нужно хранить информацию о книгах: автор, название книги,
# жанр, год выпуска, количество страниц, издательство. Требуется реализовать возможность добавления, удаления,
# поиска, замены данных. Используйте словарь для хранения информации.

############################################### 1
# Создайте программу «Книжная коллекция». Нужно хранить информацию о книгах: автор, название книги,
# жанр, год выпуска, количество страниц, издательство. Требуется реализовать возможность добавления, удаления,
# поиска, замены данных. Используйте словарь для хранения информации.

def add_book(book):
    author = input("Введите имя автора: ").strip().lower()
    name = input("Введите название книги: ").strip().lower()

    if author in book and name in book[author]:
        print(f'Такая книга: "{name}" с таким автором: "{author}" уже существует!')
        return

    genre = input("Введите жанр книги: ").strip().lower()
    year = input("Введите год выпуска книги: ").strip().lower()
    pages = input("Введите количество страниц: ").strip().lower()
    publishing_house = input("Введите имя издательства: ").strip().lower()

    if author not in book:
        book[author] = {}
    book[author][name] = [genre, year, pages, publishing_house]
    print("*** Книга успешно добавлена! ***\n")


def del_book(book):
    if not book:
        print("*** Коллекция пуста! ***\n")
        return

    author = input("Введите имя автора: ").strip().lower()
    if author not in book:
        print("*** Такого автора не существует! ***\n")
        return

    name = input("Введите название книги: ").strip().lower()
    if name not in book[author]:
        print("*** Такой книги не существует! ***\n")
        return

    del book[author][name]
    print(f'Книга "{name}" автора "{author}" успешно удалена!\n')

    if not book[author]:
        del book[author]


def get_book(book):
    if not book:
        print("*** Коллекция пуста! ***\n")
        return

    author = input("Введите имя автора: ").strip().lower()
    if author not in book:
        print("*** Такого автора не существует! ***\n")
        return

    name = input("Введите название книги: ").strip().lower()
    if name not in book[author]:
        print("*** Такой книги не существует! ***\n")
        return

    details = book[author][name]
    print(f'Автор: "{author.capitalize()}"\n'
          f'Название книги: "{name.capitalize()}" | Жанр: {details[0].capitalize()} | Год: {details[1]} | '
          f'Страниц: {details[2]} | Издательство: {details[3].capitalize()}\n')


def replace_book(book):
    if not book:
        print("*** Коллекция пуста! ***\n")
        return

    author = input("Введите имя автора: ").strip().lower()
    if author not in book:
        print("*** Такого автора не существует! ***\n")
        return

    name = input("Введите название книги: ").strip().lower()
    if name not in book[author]:
        print("*** Такой книги не существует! ***\n")
        return

    new_name = input("Введите новое название книги: ").strip().lower()
    genre = input("Введите жанр книги: ").strip().lower()
    year = input("Введите год выпуска книги: ").strip().lower()
    pages = input("Введите количество страниц: ").strip().lower()
    publishing_house = input("Введите имя издательства: ").strip().lower()

    del book[author][name]
    book[author][new_name] = [genre, year, pages, publishing_house]
    print("*** Книга успешно изменена! ***\n")


def show_all(book):
    if not book:
        print("*** Коллекция пуста! ***\n")
        return

    for author, books in book.items():
        print(f'Автор: {author.capitalize()}')
        for name, details in books.items():
            print(f'Название: "{name.capitalize()}" | Жанр: {details[0].capitalize()} | Год: {details[1]} | '
                  f'Страниц: {details[2]} | Издательство: {details[3].capitalize()}')
        print()



def main():

    collection_books = {}
    while True:
        answer = input(f"Mеню:\n"
                               f"1 - Добавить книгу\n"
                               f"2 - Удалить книгу\n"
                               f"3 - Найти книгу\n"
                               f"4 - Заменить книгу\n"
                               f"5 - Показать все книги\n"
                               f"0 - Выход\n")
        if answer == "1":
            add_book(collection_books)
        elif answer == "2":
            del_book(collection_books)
        elif answer == "3":
            get_book(collection_books)
        elif answer == "4":
            replace_book(collection_books)
        elif answer == "5":
            show_all(collection_books)
        elif answer == "0":
            pass
        else:
            print("*** Неверные данные ***")
            print()

main()


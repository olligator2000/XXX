############################################### 1
# Создайте программу «Книжная коллекция». Нужно хранить информацию о книгах: автор, название книги,
# жанр, год выпуска, количество страниц, издательство. Требуется реализовать возможность добавления, удаления,
# поиска, замены данных. Используйте словарь для хранения информации.
import dataclasses


def add_book(book):
    author = input("Введите имя автора: ").lower()
    name = input("Введите название книги: ").lower()
    if author not in book:
        genre = input("Введите жанр книги: ").lower()
        year = input("Введите год выпуска книги: ").lower()
        pages = input("Введите количество страниц: ").lower()
        publishing_house = input("Введите имя издательства: ").lower()
        if name not in author:
            book[author] = {name: [genre, year, pages, publishing_house]}
            print("*** Книга успешно добавлена! ***")
    elif name not in book[author]:
        genre = input("Введите жанр книги: ").lower()
        year = input("Введите год выпуска книги: ").lower()
        pages = input("Введите количество страниц: ").lower()
        publishing_house = input("Введите имя издательства: ").lower()
        book[author].update({name: [genre, year, pages, publishing_house]})
        print("*** Книга успешно добавлена! ***")
    else:
        print(f'Такая книга: "{name}" с таким автором: "{author}" уже сущесвтует!!!')


def del_book(book):
    author = input("Введите имя автора: ").lower()
    name = input("Введите название книги: ").lower()
    if author not in book and name not in book:
        print("*** Такой книги не существует! ***")
    else:
        del book[author]
        print("*** Книга успешно добавлена! ***")


def get_book(book):
    if not book:
        print("*** Коллекция пуста! ***")
        return
    author = input("Введите имя автора: ").lower()
    name = input("Введите название книги: ").lower()
    find_author = book.get(author, "Не сущесвтует! ")
    find_book = find_author.get(name, "Не сущесвтует! ")
    print(f'Автор: {find_author}, Название книги: {find_book}')
    for name, details in find_author.items():
        print(f'Жанр: {details[0].capitalize()} | Год: {details[1]} | '
              f'Страниц: {details[2]} | Издательство: {details[3].capitalize()}')
    print()


# name = input("Введите имя баскетболиста: ")
#     find_player = players.get(name, "Не сущесвтует! ")
#     print(f"{name}: {find_player}")
#

def show_all(book):
    if not book:
        print("*** Коллекция пуста! ***")
        return
    for author, books in book.items():
        print(f'Автор: {author.capitalize()}')
        for name, details in books.items():
            print(f'  Название: "{name.capitalize()}" | Жанр: {details[0].capitalize()} | Год: {details[1]} | '
                  f'Страниц: {details[2]} | Издательство: {details[3].capitalize()}')
        print()


def show_alls(book):
    print(book)


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
            show_alls(collection_books)
        elif answer == "5":
            show_all(collection_books)
        elif answer == "0":
            pass
        else:
            print("Неверные данные")

main()

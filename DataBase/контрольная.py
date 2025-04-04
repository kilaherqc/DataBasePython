import random
import sqlite3

library = sqlite3.connect("library.db")
cursor = library.cursor()

"""cursor.execute("CREATE TABLE books (book_id INTEGER, "
               "title TEXT, "
               "author TEXT, "
               "year INTEGER, "
               "available INTEGER )")

cursor.execute("CREATE TABLE readers (reader_id INTEGER, "
               "name TEXT, "
               "phone TEXT, "
               "book_id INTEGER )")"""

library.commit()
library.close()

def add_book():
    library = sqlite3.connect("library.db")
    cursor = library.cursor()
    book_id = random.randint(1, 100)
    title = input("Название книги:")
    author = input("Автор книги:")
    year = input("Год выпуска:")
    available = input("Наличее книги:")
    cursor.execute("INSERT INTO books (book_id, title, author, year, available)"
                   "VALUES (?, ?, ?, ?, ?)", (book_id, title, author, year, available))

    library.commit()
    library.close()

def add_reader():
    library = sqlite3.connect("library.db")
    cursor = library.cursor()
    reader_id = random.randint(1, 100)
    name = input("ФИО:")
    phone = int(input("Номер телефона:"))
    cursor.execute("INSERT INTO readers (reader_id, name, phone)"
                   "VALUES (?, ?, ?)", (reader_id, name, phone))

    library.commit()
    library.close()

def give_book():
    pass

def return_book():
    pass

while True:
    print("1. Добавить книгу\n"
          "2. Добавить читателя\n"
          "3. Выдать книгу\n"
          "4. Получить книгу")
    actions = input("Выберите действие: ")

    match actions:
        case "1":
            add_book()
        case "2":
            add_reader()
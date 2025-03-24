import sqlite3

users = sqlite3.connect("users.db")

#создание курсора
cursor = users.cursor()

#создание таблицы в бд
# cursor.execute("CREATE TABLE users (name TEXT, "
#                "id INTEGER, "
#                "age INTEGER )")

#записать в таблицу
#cursor.execute("INSERT INTO users VALUES('Vlasov Vlad', 32434, 17)")

#сохранить БД
users.commit()

#вытащить всех юзеров
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())
#вытащить имена юзеров
cursor.execute("SELECT name FROM users")
print(cursor.fetchall())

#вытащить номера строк
cursor.execute("SELECT rowid, name, id FROM users")
print(cursor.fetchall())

#вытащить n количество строк
cursor.execute("SELECT * FROM users")
print(cursor.fetchmany(2))

#вытащить n количество строк
cursor.execute("SELECT * FROM users")
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())


cursor.execute("DELETE FROM users WHERE id = '32434'")
users.commit()
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

users.close()
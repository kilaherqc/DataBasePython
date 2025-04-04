import sqlite3
from items import *
from users import *

users_db = sqlite3.connect("shop_users.db")
cursor = users_db.cursor()

statuses = ["заказан", "в пути", "готов", "завершён"]

cursor.execute("CREATE TABLE IF NOT EXISTS Users "
               "( id INTEGER,"
               "name TEXT,"
               "username TEXT,"
               "age INTEGER,"
               "email TEXT)")

cursor.execute("CREATE TABLE IF NOT EXISTS Orders "
               "(id INTEGER,"
               "name TEXT,"
               "price INTEGER,"
               "articul INTEGER,"
               "status TEXT,"
               "order_ID INTEGER)")

users_db.commit()
users_db.close()

user1 = Users(24332342, "Андрей", "Andrew", 25, "lol@gmail.com")
user2 = Users(43543545, "Таня", "Tati", 25, "lol1@gmail.com")

item1 = Items("Zahar", 10, 432434)
item2 = Items("Dima", 100, 435455)

def add_user_DB(user: Users):
    users_db = sqlite3.connect("shop_users.db")
    cursor = users_db.cursor()

    cursor.execute("INSERT INTO Users ("
                   "id, "
                   "name, "
                   "username,"
                   "age,"
                   "email"
                   ") VALUES (?, ?, ?, ?, ?)",
                   user.get_info())

    users_db.commit()
    users_db.close()

def buy_item(user: Users, item: Items):
    item.buy_item(user.id)

    users_db = sqlite3.connect("shop_users.db")
    cursor = users_db.cursor()

    cursor.execute("INSERT INTO Orders ("
                   "id, "
                   "name, "
                   "price,"
                   "articul,"
                   "status,"
                   "order_ID"
                   ") VALUES (?, ?, ?, ?, ?, ?)",
                   (user.id, item.name, item.price,
                    item.aricul, item.status, item.order_ID))

    users_db.commit()
    users_db.close()

def show_orders(user: Users):
    with sqlite3.connect("shop_users.db") as users_db:
        cursor = users_db.cursor()
        cursor.execute("SELECT * FROM Orders WHERE id=?", (user.id, ))

        orders = cursor.fetchall()
        if orders:
            for order in orders:
                if order[4] != statuses[len(statuses) - 1]:
                    print(f"название {order[1]} \n"
                      f"цена {order[2]} \n"
                      f"артикул {order[3]} \n"
                      f"статус {order[4]} \n"
                      f"id заказа {order[5]}")

def up_status(user:Users, order_ID):
    with sqlite3.connect("shop_users.db") as users_db:
        cursor = users_db.cursor()
        cursor.execute("SELECT status FROM Orders WHERE order_ID=?", (order_ID, ))

        order_status = cursor.fetchone()[0]
        if order_status != "завершён":
            next_status = statuses[statuses.index(order_status) + 1]
        else:
            next_status = order_status

        cursor.execute("UPDATE Orders SET status=? WHERE order_ID=?", (next_status, order_ID,))

        users_db.commit()

# add_user_DB(user1)
# add_user_DB(user2)
# buy_item(user1, item1)
# buy_item(user1, item2)
up_status(user1, 8292)
show_orders(user1)






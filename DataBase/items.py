import random
class Items:
    def __init__(self, name, price, articul):
        self.name = name
        self.price = price
        self.aricul = articul

        self.id = None
        self.status = None
        self.order_ID = None

    def show_info(self):
        print(f'название {self.name} \n'
              f'цена {self.price} \n'
              f'артикул {self.aricul}')

        if self.id:
            print(f'статус {self.status} \n'
                  f'номер заказа {self.order_ID}')

    def buy_item(self, id):
        self.id = id
        self.status = "заказан"
        self.order_ID = random.randint(1, 10000)



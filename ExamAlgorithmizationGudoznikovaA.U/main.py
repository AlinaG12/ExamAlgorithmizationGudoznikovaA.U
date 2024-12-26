import random
import datetime

class Product:
    def __init__(self):
        self.manufacture_date = self.generate_manufacture_date()
        self.price = random.uniform(10, 100)
        self.shelf_life_days = random.randint(1, 10)

    def generate_manufacture_date(self):
        today = datetime.datetime.now()
        random_days = random.randint(1, 7)
        return today - datetime.timedelta(days=random_days)

    def calculate_price(self):
        today = datetime.datetime.now()
        expiration_date = self.manufacture_date + datetime.timedelta(days=self.shelf_life_days)
        
        if self.manufacture_date.date() == today.date():
            final_price = self.price
        elif today < expiration_date:
            final_price = self.price * 0.8
        else:
            final_price = 0
        
        return final_price

    def display_product_info(self):
        print(f"Дата изготовления: {self.manufacture_date.date()}")
        print(f"Цена: {self.price:.2f}")
        print(f"Срок годности: {self.shelf_life_days} дней")
        final_price = self.calculate_price()
        print(f"Итоговая цена: {final_price:.2f}")


product = Product()
product.display_product_info()
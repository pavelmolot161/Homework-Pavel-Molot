
###  Задача "Учёт товаров":  ###

class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name                           ### - название продукта (строка)
        self.weight = float(weight)                ### - общий вес товара (дробное число)
        self.category = category                   ### - категория товара (строка).

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}.'

from pprint import pprint

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            return "Файл не найден"

    def add(self, *products):
        existing_products = self.get_products().split('\n') if self.get_products() else []
        for product in products:
            if f"{product.name}, {product.weight}, {product.category}" not in existing_products:
                with open(self.__file_name, 'a') as file:
                    file.write(f"{product.name}, {product.weight}, {product.category}\n")
            else:
                print(f"Продукт {product.name}, {product.weight}, {product.category} уже есть в магазине")

   #     Пример работы программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

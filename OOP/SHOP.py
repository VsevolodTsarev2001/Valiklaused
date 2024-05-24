from itertools import product
from math import fabs
from socket import CAN_J1939

class Product:
    def __init__(self, name, price):
        self.name = name 
        self.price = price
        self.id = id

    def __eq__(self, other):
        if isinstance(other, Product) and other.id == self

class Shop:
    def __init__(self, name):
        self.name = name 
        self.products = {}
        self.products_counts = {}
        self.carts = []

    def add_product(self, product: Product, count: int = 1) ->bool:
        if not product.id:
            return False
        if product.name not in self.products:
            self.products[product.id] = product 
            self.products[product.name] = count
        else:
            self.products_counts[product.id] += count
            return True
    def get_product_count(self, product: Product) ->int:
        if product.id not in self.products:
            return -1 
        return self.product_counts[product.id]
    def move_to_cart(self, product: Product, count=1) -> bool:
        if product.id not in self.products:
            return False
        if count> self.products_counts[product.id]:
            return False
        self.products_counts[product.id] -=count
        return True

class Cart:
    def __init__ (self):
        self.products = {}
        self.shop = shop 
    def add_product (self, product: Product, count = 1)-> int:
        count_in_store=self.shop.get_product_count(product)
        if count_in_store <= 0:
            return count_in_store
        if count_in_store < count:
            count = count_in_store
        self.shop.move_to_cart(product, count)
        self.products[product.id] = \
            self.products.get(product.id, 0) + count
        return count
    def get_total_price(self):
        total_price=0
        for pid, count in self.products.items():
            total_price += self.shop.products[pid].price * count
        return total_price
            


if __name__ == '__main__':
    shop1 = Shop("Rama")
    shop2 = Shop("Selma")

    p1 = Product ("Milk", 80, 1)
    p2 = Product ("Bread", 120, 2)
    
    shop1.add_product(p1, 10)
    shop1.add_product(p2, 10)
    print(shop1.products)
    print(shop1.product_counts)
    c1= Cart(shop1)
    print (c1.add_product(p1,4))
    print(shop1.product_counts)
    print(c1.products)
    print(c1.add_product(p1,4))
    print(shop1.product_counts)
    print(c1.products)
    c1.add_product(p2, 3)
    print(c1.get_total_price())
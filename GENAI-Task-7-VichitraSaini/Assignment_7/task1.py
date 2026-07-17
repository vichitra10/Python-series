## Basic Class and Object Creation
class Product:
    def __init__(self ,name, price, category):
        self.name = name
        self.price = price
        self.category = category
        
    def get_info(self):
        print(f"The product name is {self.name}, and price is {self.price}. The Product belongs to {self.category}")
        

obj1 = Product('SamsungMobile',50000,'Electornic')
obj2 = Product('Laptop',75000,'Electornic')

obj1.get_info()
obj2.get_info()
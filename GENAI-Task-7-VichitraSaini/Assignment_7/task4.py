## Polymorphism

class Laptop:
    def __init__(self, name, price , category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print(f"The name of the product {self.name} and the price will be {self.price}. This product belongs to the {self.category} Category")


class Mobile:
    def __init__(self,name, price, category):
        self.name = name
        self.price = price
        self.category = category 

    def get_info(self):
        print(f"The name of the product {self.name} and the price will be {self.price}. This product belongs to the {self.category} Category")


lapi_obj = Laptop('Samsung',80000,'Electronics')  
mobi_obj = Mobile('Apple',150000,'Electronice')

products = [lapi_obj,mobi_obj]
for product in products:
    product.get_info()

      



     
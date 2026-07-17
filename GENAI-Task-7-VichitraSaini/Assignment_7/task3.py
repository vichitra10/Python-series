## Inheritance (Single-Level)
class Product:
          def __init__(self, name, price, category):
           self.name = name
           self.price = price
           self.category = category

          def get_info(self):
                print(f"The name of product {self.name} and the price of this product {self.price} and its belongs to {self.category} category")
        
class ElectronicProduct(Product):
           def __init__(self, name, price, category, warrenty_years):
              super().__init__(name, price, category)
            
           def get_warrenty_details(self):
                print(f"The warrenty of this product will be 3 years")


child_obj = ElectronicProduct('Laptop',80000,'Eletronic',1)
child_obj.get_info()    ## this function define in Product Class but we can call this in our child class with the help of Inheritance
child_obj.get_warrenty_details()                
## Constructor and Encapsulation
class Product:
     def __init__(self,name,price,category):
     
        self.name = name
        self.__price = price  ## Private Attributs
        self.category = category
   

     def get_price(self):
      return self.__price


     def set_price(self,new_price):
      if new_price > 0:
           self.__price = new_price
      else:
         print("Price must be greater than 0")     
  
obj_1 = Product('LCD',80000,'Electronics')
print("Current Price:", obj_1.get_price())
obj_1.set_price(90000)
print(f"Updated Price: {obj_1.get_price()}")
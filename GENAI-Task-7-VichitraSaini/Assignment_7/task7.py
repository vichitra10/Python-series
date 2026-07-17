## Mini Project: Simple Inventory System (OOP Only)
class Product:
          def __init__(self, name, price, category):
           self.name = name
           self.price = price
           self.category = category

          def get_info(self):
                print(f"The name of product {self.name} and the price of this product {self.price} and its belongs to {self.category} category")

          def __str__(self):
            return f"Product({self.name}, {self.price}, {self.category})"  

          def __add__(self, other):
            return self.price + other.price  


class Inventory:
    def __init__(self):
        self.products = []   # list to store Product objects

    def add_product(self, product):
        self.products.append(product)
        print(product.name, "added successfully.")

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(name, "removed successfully.")
                return

        print("Product not found.")

    def get_total_value(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def show_all_products(self):
        print("\nProducts in Inventory:")
        for product in self.products:
            product.get_info()


class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        category = input("Enter Product Category: ")

        product = Product(name, price,category)
        self.inventory.add_product(product)

    def show_summary(self):
        print("\n========== Store Summary ==========")
        print("Store Name:", self.store_name)
        print("Total Products:", len(self.inventory.products))
        print("Total Value: $", self.inventory.get_total_value())
        self.inventory.show_all_products()


# Create Store object
store = Store("Tech Shop")

# Add 3 products
store.add_new_product()
store.add_new_product()
store.add_new_product()

# Show summary
store.show_summary()

# Using __add__
print("\nTesting __add__ method:")

p1 = store.inventory.products[0]
p2 = store.inventory.products[1]

print(f"{p1.name} + {p2.name} = ${p1 + p2}")

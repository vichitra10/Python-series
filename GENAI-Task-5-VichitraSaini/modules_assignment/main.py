import math_utils
import string_utils
from math_utils import square
from shop_package import calculate_total,apply_discount,apply_tax,flat_discount

addition = math_utils.add(1,4)  
print(addition) 
subtration = math_utils.subtract(5,4)
print(subtration)
square_result = math_utils.square(5)
print(square_result)

# Here i am using another method to import function directly

square1  = square(7)
print(square1)


## String funtion
word = string_utils.capitalize_words('vichitra')
print(word)


my_text = string_utils.reverse_string("Learning Python")
print(my_text)

my_txt = string_utils.word_count("I love Python")
print(my_txt)



## funcion included from the shoppackage
# prices = [100, 200, 300]
total = calculate_total([100, 200, 300])
print("Total Price:", total)


tax_price = apply_tax(total)
print("After Tax:", tax_price)

# discounted_price = apply_discount(tax_price,10)
discounted_price = apply_discount(1000,10)

print(f"Discounted Price: {discounted_price}")

flat = flat_discount(discounted_price)
print("After Flat Discount:", flat)
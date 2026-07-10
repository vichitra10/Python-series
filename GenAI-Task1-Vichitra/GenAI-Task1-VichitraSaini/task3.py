## Product Pricing (Dictionaries)
price_dict = [{'name':'UrbanFlex_Hoodie', 'price': 500},
              {'name':'LuxeWeave_Shirt', 'price': 800},
              {'name':'AeroFit_Joggers', 'price': 1200},
              {'name':'VelvetAura_Dress', 'price': 1800},
              {'name': 'Classic_Edge_Sneakers', 'price': 2500},
              {'name':'PureRadiance_Cream', 'price': 650},
              {'name':'BloomLip_Tint', 'price': 450}   
              ]

print(price_dict)
price_dict.append({
    'name': 'HydraGlow_Serum',
    'price': 950
})
print(price_dict)
price_dict[-1]['price']= 1000
print(price_dict)

# Here I am removing the product from the dictionary 
for product in price_dict:
    if product['name'] == 'LuxeWeave_Shirt':
        price_dict.remove(product)
        break
print(price_dict)

## Average price of all Price
total_price = 0
# max_price = price_dict[1]['price']
# min_price = price_dict[1]['price']

max_price = min_price = price_dict[1]['price']

# print(f" the max price is {max_price}")

for product in price_dict:
    total_price += product['price']
    avg_price = round(total_price / len(price_dict),2)

    if(product['price']) >=max_price:
        max_price = product['price']

    if(product['price']) <=min_price:
        min_price = product['price']    

print(f"The average price of the product is {avg_price}")
print(f"The max price of the products {max_price}")
print(f"The min price of the products {min_price} ")


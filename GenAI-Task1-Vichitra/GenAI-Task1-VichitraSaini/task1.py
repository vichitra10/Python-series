#taks1: Product Collection (Lists and Tuples)
products = ['UrbanFlex_Hoodie','LuxeWeave_Shirt','AeroFit Joggers','VelvetAura Dress','Classic Edge Sneakers'] ## Create a list
sample_products = ('UrbanFlex_Hoodie', 500, 'Fashion') ## Create a tuple
print(products[-1]) ## Here I am getting last product from the list
print(products[1]) ## Here I am getting second product from the list
products.append('PureRadiance Cream') ## Adding 1st Product
products.append('BloomLip Tint')      ## Adding 2nd Product
print(products)   # new Product List

sample_products_list = list(sample_products) # Here I am converting the tuple into the list with the help of list
print(sample_products_list) 
sample_products_list[1] = 1000 ## Changes the price of the product

sample_product_list_tuple = tuple(sample_products_list) ## Convert again into a tuple
print(sample_product_list_tuple) ## and here again i am printing the value of tuple with new price

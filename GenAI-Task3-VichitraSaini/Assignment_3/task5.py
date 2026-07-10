## Using filter(): Filter Expensive Products
prices = [100,250,400,1200,50,2000,850]
lowest_price_list = list(filter(lambda price: price < 500, prices))
highest_price_list = list(filter(lambda price:price>=500,prices))
print(lowest_price_list)
print(highest_price_list)


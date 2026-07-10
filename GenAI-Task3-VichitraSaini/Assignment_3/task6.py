## Command Utility Funciton 
def process_price(prices):

    discounted_prices = list(map(lambda price: price - (price * 10/100), prices))
    filtered_prices = list(filter(lambda price:price > 300 ,prices ))

    return discounted_prices,filtered_prices

prices = [100,500,900,50,750]
discounted_prices , filtered_prices = process_price(prices)
print(f"\n The Discounted Price are: {discounted_prices}")
print(f"\n The Filtered Price are: {filtered_prices}")
## apply discount
## Apply percentage discount
def apply_discount(price, percent):
    discounted_price = lambda p: p - (p * percent / 100)
    return discounted_price(price)


## Apply flat discount of 50
def flat_discount(price):
    flat_discount = lambda p: p - 50
    return flat_discount(price)
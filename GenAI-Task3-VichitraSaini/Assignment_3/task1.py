## Basic Function : Price After Discount
def apply_discount(price,discount_percent = 5):
    if discount_percent > 60:
     return "Discount never exceeds 60%"
    discount_amount = price*discount_percent/100
    price_after_discount = price - discount_amount
    final_price = price_after_discount
    return final_price

print(apply_discount(1000,10)) ## use discount amount

print(apply_discount(500)) ## use default discount amount

print(apply_discount(20000, 70)) ## Discount never exceeds 60%~``
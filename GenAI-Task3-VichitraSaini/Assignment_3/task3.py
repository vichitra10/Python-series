## Lambda Function : GST Calculator
gst = lambda price: price + (price * 0.18)

print(gst(100)) ## GST Calculator

final_price = lambda price,discount: (price + (price * 0.18)) - (price*discount/100) ## Without Using GST function
final_price_1 = lambda price,discount:gst(price-(price*discount/100)) ## With Using GST Function

print(final_price(5000,10)) ## Final price with gst and discount
print(final_price_1(5000,10))




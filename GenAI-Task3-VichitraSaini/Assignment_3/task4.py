## Using Map(): Apply GST to List of Prices
gst = lambda price: price + (price * 0.18)
prices = [100,250,400,1200,50]
print(prices)
price_with_gst = list(map(gst,prices))
print(price_with_gst)



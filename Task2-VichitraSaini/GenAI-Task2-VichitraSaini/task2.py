## Process Multiple Orders (for Loop)
orders = [1200,2500,800,1750,3000]
discount = 0
discount_amount = 0
final_amount = 0
total_revenue = 0
discounted_orders = 0
for order_amount in orders:
        ## print(order)
        if order_amount >=2000:
            discount = 15
        elif 1500 <= order_amount < 2000 :
            discount = 10 
        elif 1000 <= order_amount < 1500 :
            discount = 7
        else:
            discount = 0 
        if(discount > 0):
                discounted_orders += 1

        discount_amount = order_amount * discount / 100
        final_amount = order_amount - discount_amount
        total_revenue += final_amount

        print(f"Order Amount: {order_amount}")
        print(f"Discount: {discount}")
        print(f"Final Amount: {final_amount}")

print(f"\nTotal Revenue: {total_revenue}")
print(f"Discounted orders: {discounted_orders} ")
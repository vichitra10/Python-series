# Write a program that reads an integer order_amount from the user using input()

order_amount = input("Enter amount: ")
print(order_amount)

if order_amount.isdigit():
    print("Amount is valid and its integer")


    order_amount = int(order_amount)   # Convert string to integer
    tax = 5
    subtotal = 0
    

    if order_amount >= 2000:
        discount = 15
    elif  1500 <= order_amount < 2000 :
        discount = 10

    elif 1000 <= order_amount < 1500 :
        discount = 7
    else:
        discount = 0

    print("Discount:", discount, "%")

    discount_amount = order_amount*discount/100
    print(f"Discount Amount: {discount_amount}")
    tax_amount = order_amount*tax/100
    subtotal = order_amount - discount_amount
    print(f"SubTotal: {subtotal}")
    print(f"Tax amount: {tax_amount}")
    
    finalTotal = subtotal + tax_amount
 
    print(f"Final Total Amount: {finalTotal}")

else:
    print("Its not a valid integer value")


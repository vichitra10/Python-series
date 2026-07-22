# Task 3 : User Menu (while loop + break/continue)

orders = []

while True:
    print("\n1: Add Order Amount")
    print("2: Show all orders and totals after applying discounts")
    print("q: Quit")

    choice = input("Enter Your Choice: ")

    if choice == "1":

        amount = input("Enter Order Amount: ")

        if amount.isdigit():
            orders.append(int(amount))
            print("Order added successfully.")
        else:
            print("Invalid Order Amount")
            continue

    elif choice == "2":

        if len(orders) == 0:
            print("No orders available.")
            continue

        total_revenue = 0
        discounted_orders = 0

        for order_amount in orders:

            if order_amount >= 2000:
                discount = 15
            elif 1500 <= order_amount < 2000:
                discount = 10
            elif 1000 <= order_amount < 1500:
                discount = 7
            else:
                discount = 0

            if discount > 0:
                discounted_orders += 1

            discount_amount = order_amount * discount / 100
            final_amount = order_amount - discount_amount
            total_revenue += final_amount

            print("\n-----------------------")
            print(f"Order Amount: {order_amount}")
            print(f"Discount: {discount}%")
            print(f"Final Amount: {final_amount}")

        print("\n=======================")
        print(f"Total Revenue: {total_revenue}")
        print(f"Discounted Orders: {discounted_orders}")

    elif choice == "q":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
        continue
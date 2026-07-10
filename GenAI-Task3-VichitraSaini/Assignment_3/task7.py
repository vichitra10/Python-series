def add_price(price_list, price):
    price_list.append(price)


def get_average_price(price_list):
    average_price = 0
    for price in price_list:
        average_price += price
    return average_price / len(price_list)


def get_max_price(price_list):
    max_price = price_list[0]
    for price in price_list:
        if price > max_price:
            max_price = price
    return max_price


price_list = []

while True:
    print("\n1: Add Price")
    print("2: Show Average Price")
    print("3: Show Highest Price")
    print("q: Quit")

    choice = input("Select Menu: ")

    if choice == '1':
        price = int(input("Enter Price: "))
        add_price(price_list, price)

    elif choice == '2':
        if len(price_list) == 0:
            print("No prices available.")
        else:
            print("Average Price:", get_average_price(price_list))

    elif choice == '3':
        if len(price_list) == 0:
            print("No prices available.")
        else:
            print("Highest Price:", get_max_price(price_list))

    elif choice == 'q':
        print("Thank You")
        break

    else:
        print("You Have Entered Invalid Choice")
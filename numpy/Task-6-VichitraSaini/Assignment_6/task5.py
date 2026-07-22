class NegativePriceError(Exception):
    pass

cart = []
while True:
    try:
        user_input = input("Enter price (or q to quit): ")

        # Check for q
        if user_input.lower() == "q":
            break

        # Convert to float
        price = float(user_input)

        # Raise custom exception
        if price < 0:
            raise NegativePriceError("Price cannot be negative")

        # Add to cart
        cart.append(price)

    except ValueError:
        print("Invalid input. Please enter a number.")

    except NegativePriceError as e:
        print(e)

print("Total Items:", len(cart))
print("Total Bill:", sum(cart))
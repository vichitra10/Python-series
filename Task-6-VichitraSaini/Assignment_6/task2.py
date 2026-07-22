## Task 2: Bill Calculator with Error Handling

prices = [120, 350, "abc", "bca", 500, -200, 800]
total = 0

for price in prices:
    try:
        if isinstance(price, str):
            raise TypeError("String value found")

        if price < 0:
            raise ValueError("Negative number found")

        total += price

    except TypeError:
        print(f"Skipping string: {price}")

    except ValueError:
        print(f"Skipping negative number: {price}")

print("Total Bill:", total)
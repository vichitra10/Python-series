## Mini Project - Export Discounted Price

prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

discount = int(input("Enter Discount Percentage: "))

if discount > 70:
    print("Discount cannot be above 70%.")
else:
    total_items = 0
    total_discounted_price = 0

    file = open("discount_report.txt", "w")

    file.write("Product | Original Price | Discounted Price\n")
    file.write("-" * 45 + "\n")

    for product, price in prices.items():

        discounted_price = price - (price * discount / 100)

        file.write(f"{product} | {price} | {discounted_price:.2f}\n")

        total_items += 1
        total_discounted_price += discounted_price

    average_discounted_price = total_discounted_price / total_items

    file.write("\n")
    file.write(f"Total Items: {total_items}\n")
    file.write(f"Average Discounted Price: {average_discounted_price:.2f}\n")

    file.close()

    # Read the file
    file = open("discount_report.txt", "r")
    print(file.read())
    file.close()
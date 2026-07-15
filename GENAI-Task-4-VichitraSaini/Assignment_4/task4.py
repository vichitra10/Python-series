## Generate Summary Report from file

file = open("sales_data.txt", "r")
data = file.readlines()
file.close()

sales = []
total_sales = 0

for value in data:
    sales.append(int(value.strip()))

highest_sales = sales[0]
lowest_sales = sales[0]

for sale in sales:
    total_sales += sale

    if sale > highest_sales:
        highest_sales = sale

    if sale < lowest_sales:
        lowest_sales = sale

average_sales = total_sales / len(sales)

print("Total Sales:", total_sales)
print("Highest Sale:", highest_sales)
print("Lowest Sale:", lowest_sales)
print("Average Sale:", average_sales)
## Create Produuct Info File (User Input)
product_info = []

file = open("products.txt", "w")

for i in range(3):
    product_name = input("Enter Product Name: ")
    product_price = input("Enter Product Price: ")

    product_info.append({
        "name": product_name,
        "price": product_price
    })

    file.write(f"{product_name} | {product_price}\n")

file.close()

file = open("products.txt", "r")

print("Product Details:")
for line in file:
    print(line.strip())

file.close()
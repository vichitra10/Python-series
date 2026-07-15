new_sales = [5000,2500,1700]
file = open('sales_data.txt','a')

for sale in new_sales:
    file.write(str(sale) + "\n")
file.close()
file = open('sales_data.txt','r')
print(file.read())
file.close()
## Write Sales Records to a file
sales = [1200,450,980,1500,3000]
file = open('sales_data.txt','w')
for sale in sales:
    file.write(str(sale) + "\n") 
    # file.write(str(sale )+ ",")
file.close()
file = open('sales_data.txt','r')
print(file.read())
file.close()



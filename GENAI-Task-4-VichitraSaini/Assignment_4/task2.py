## Read File in Different Ways
file = open('sales_data.txt','r')
# print(file.read())
file.close()
file = open('sales_data.txt','r')
# print(file.readline())
file.close()

## convert each sales to string
file = open('sales_data.txt','r')
lines = file.readlines()
file.close()

sales = []

for line in lines: 
    sales.append(int(line.strip()))
print(sales)    
    




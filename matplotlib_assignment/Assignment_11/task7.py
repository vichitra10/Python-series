## Pie Chart (Market Share)
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
sales = pd.read_csv('Chocolate Sales.csv')
print(sales.head())

sales['Amount'] = (
    sales['Amount']
    .str.replace('$', '', regex=False)
    .str.replace(',', '', regex=False)
    .astype(float)
)

product_sales = sales.groupby('Product')['Amount'].sum()
# print(country_sales)

plt.figure(figsize=(8,8))
plt.title('Product Market Share')
plt.pie(product_sales.values, labels = product_sales.index , autopct='%1.1f%%')
plt.show()

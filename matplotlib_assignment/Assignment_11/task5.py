## Stacked Bar Chart ()
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
sales = pd.read_csv('Chocolate Sales.csv')
# print(sales)

sales['Date'] = pd.to_datetime(sales['Date'], format='%d/%m/%Y')
sales['Year'] = sales['Date'].dt.year
sales['Month'] = sales['Date'].dt.month_name()

month_order = [
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
]

sales['Month'] = pd.Categorical(
    sales['Month'],
    categories=month_order,
    ordered=True
)

sales['Amount'] = (
    sales['Amount']
    .str.replace('$', '', regex=False)
    .str.replace(',', '', regex=False)
    .astype(float)
)

yearly_sales = sales.groupby(['Month', 'Year'])['Amount'].sum().unstack()
# print(yearly_sales)

# x = yearly_sales.index
# y = yearly_sales.values

yearly_sales.plot(
    kind='bar',
    stacked=True,
    figsize=(12,6)
)

plt.title('Year-wise Sales Comparison (Stacked Bar Chart)')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.legend(title='Year')
plt.tight_layout()
plt.show()
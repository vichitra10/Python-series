## Line Plot (Sales Trend)
import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv('Chocolate Sales.csv')
sales['Date'] = pd.to_datetime(sales['Date'], format='%d/%m/%Y') ## Convert Date to Datetime

## create a seperate month column
sales['Month'] = sales['Date'].dt.month_name()

## Arrange month in Correct order
month_order = ['January','February','March','April','May','June','July','August','September','October','November','December']
sales['Month'] = pd.Categorical(sales['Month'],categories=month_order,ordered=True)

## Calculate total sales for each month
# monthly_sales = sales.groupby('Month')['Amount'].sum()

## First we have to remove extra spaces and dolor sign from the Amount column

# sales['Amount'] = (
#     sales['Amount']
#     .str.replace('$', '', regex=False)
#     .str.replace(',', '', regex=False)
#     .astype(float)
# )

# ## Now calculate the amount based on Month
# monthly_sales = sales.groupby('Month')['Amount'].sum()
# print(monthly_sales)

## here I am removing decimal number from the Amount , want to use only integer

sales['Amount'] = (
    sales['Amount']
    .str.replace('$', '', regex=False)
    .str.replace(',', '', regex=False)
    .astype(float)
    .astype(int)
)

## Again Calculating the total amount based on Month
monthly_sales = sales.groupby('Month')['Amount'].sum()

# print(monthly_sales)
x = monthly_sales.index
y = monthly_sales.values

## Draw a line plot for sales visualization
plt.figure(figsize=(10,5))
plt.title('Sales Trend Over Month')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.plot(x,y, color='blue',linestyle='--',marker='o',linewidth='2')
plt.grid(True)
plt.show()
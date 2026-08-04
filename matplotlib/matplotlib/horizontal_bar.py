import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Student Depression Dataset.csv')  ## Data Gathering 


### Horizontal , Multiple and Stacked Bar Charts

## Horizontal Bar Chart: Bars are going to be Horizontal 
## barh() ---> Horizontal Bar Chart
data  = df['Gender'].value_counts()
# print(data)

x =  data.index
y = data.values

## Plotting bar plot ---- bar()---->plt.bar()

data = df[(df['Dietary Habits'] == 'Healthy') | (df['Dietary Habits'] == 'Moderate') | (df['Dietary Habits'] == 'Unhealthy')]
# data['Dietary Habits'].value_counts().plot(kind='bar')
plt.title('Dietary Habits Distribution')
plt.xlabel('Dietary Habits')
plt.ylabel('Count')
plt.barh(x,y)
plt.grid(axis='y')
# plt.show()

## Multiple Bar Charts
## Dataset ----> Product Sales over the Months
## Mobiles ----> Sales on Month on Month Basis
## AC      -----> Sales on Month on Month Basis
## Television ----> Sales on Month on Month Basis


cho_df = pd.read_csv('Chocolate Sales.csv')

## remove $ and extra spaces from the amount column
cho_df['Amount'] = (
    cho_df['Amount']
    .str.replace('$', '', regex=False)
    .str.replace(',', '', regex=False)
    .astype(float)
    .astype(int)
)

## Add new column from the data column for handle month data seperately
cho_df['Date'] = pd.to_datetime(cho_df['Date'], format='%d/%m/%Y') 

# Find the position of the Date column
date_index = cho_df.columns.get_loc('Date')

# Insert Month column after Date
cho_df.insert(date_index + 1, 'Month', cho_df['Date'].dt.month_name())

top_five_records = cho_df.head()
# print(top_five_records)

month_order = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]


cho_df['Month'] = pd.Categorical(cho_df['Month'],categories=month_order,ordered=True)


choco_month_sales = cho_df[cho_df['Product'] =='Mint Chip Choco']
dark_bars_month_sales = cho_df[cho_df['Product'] =='85% Dark Bars']
peanut_butter_month_sales = cho_df[cho_df['Product'] =='Peanut Butter Cubes']


total_choco = choco_month_sales.groupby('Month')['Amount'].sum()
total_dark_bars = dark_bars_month_sales.groupby('Month')['Amount'].sum()
total_peanut_butter = peanut_butter_month_sales.groupby('Month')['Amount'].sum()


## convert the Month column to an ordered categorical 

# x = total_choco.index
# y = total_choco.values

x = np.arange(len(month_order))
width = 0.25

## or we can use directly values in the bar chart , instead of managing to a different variable
plt.figure(figsize=(10,5))
plt.title('Product Based Total Boxes Shipped')
plt.xlabel('Total Boxes Shipped')
plt.ylabel('Product')
## plt.bar(x,y, color='green)
# plt.bar(total_choco.index,total_choco.values, color = 'green', label='Mint Chip Choco')
# plt.bar(total_dark_bars.index,total_dark_bars.values, color = 'brown', label='Total Dark Bars')
# plt.bar(total_peanut_butter.index,total_peanut_butter.values, color = 'grey', label='Total Peanut Butter')
plt.bar(x - width, total_choco.reindex(month_order, fill_value=0), width,
        color='green', label='Mint Chip Choco')

plt.bar(x, total_dark_bars.reindex(month_order, fill_value=0), width,
        color='brown', label='85% Dark Bars')

plt.bar(x + width, total_peanut_butter.reindex(month_order, fill_value=0), width,
        color='grey', label='Peanut Butter Cubes')
plt.xticks(x, month_order, rotation=45)
plt.legend()
plt.show()


## xticks ---> This specific function can helps us out with Replacing the Original Label with the New Label ---> xticks(original_labels,new_label)

## Stacked Bar Chart
## Instead of keeping the Bars in Side by Side Direction, we can keep the Bars in the stacked manner i.e One of top of Other and in order to Figure out which category is having maximum sales , we can have a look over the Length of the Bar.

## Stacked Bar Chart: ---> bar()----> parameter ---> bottom ----> THis bottom parameter specific that what bar i want to keep below my current bar 
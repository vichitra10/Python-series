import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Student Depression Dataset.csv')  ## Data Gathering 

### Pie Chart and Changing Style

## Pie chart is being used for Bivariate Analysis and is being used for relating Categorical - Numerical Columns in Pie Chart , we will look to percentage Distrubution (Univariate Analysis) and Bivariate Analysis  (Categorical- Numerical) as in terms of Category by Category Percentage Distribution in Aggregation of Numerical Data .

## Total Sales ----> 5 crore Rupess  ----> Percentage contribution of 7 Countries where I had the sales

## Pie Chart ---> Bivariate Analysis
## Categorical - Numerical Column
## Numerical Aggregation as per Categories
## Percentage Contribution of Categories in Total Numeric Value
## univariate Analysis ---> categorical Column Value Data Contribution in percentage

# print(df.head().columns)
## Univaritae Analysis ---> value_counts()

data = df['Dietary Habits'].value_counts()

print(data)
print(type(data))
print(data.dtype)

plt.figure(figsize=(6,6))
plt.pie(
    data.values,
    labels=data.index,
    autopct='%1.1f%%'
)
plt.title('Dietary Habits Distribution')
plt.legend()
plt.show()



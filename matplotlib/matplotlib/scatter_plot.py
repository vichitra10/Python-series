import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Student Depression Dataset.csv')  ## Data Gathering 


## Scatter Plot

## Types of Plot
## Line Plot: Time Series Analysis ----> How values are varying as per Time
## Scatter Plot: Scatter Plot is being used for bivariate Analysis: Two Numerical Columns ----> We Check that based on the changes in one Numerical Column Value: How it affects the other Numerical Column Value.
## for example: ---> x ---------> Age -----> 10,15,20,50,36
##              ----> y ---------> Cholestrol Level ----> 50,60,70,80 .....90


## Scatter Plot: It will figure out that based on the increment in Age Value ----> If cholestrol level is increasing or Decresing or is Steady

## Scatter Plot: It figure out the corelation between the two numerical values 
## function to create a scatter plot -----> plt.scatter(x,y)

data = df.groupby('Age')['CGPA'].mean().head(10)
# print(data)

x = data.index ## get the index value
y = data.values ## get the value of data

x = np.linspace(-10,10,50)
y = 10+x+3  + np.random.randint(0,300,50)

plt.title('Average CGPA Variation as per AGE')
plt.xlabel('Age')
plt.ylabel('Average CGPA')
plt.scatter(x,y , color='red', marker='*')
plt.grid()
# plt.show()

sales = pd.read_csv('Chocolate Sales.csv')
top_five_records = sales.head()
print(top_five_records)

x = sales['Boxes Shipped']
y = sales['Amount']

plt.title('Total Amount Variation as per Total Boxes Shipped')
plt.xlabel('Number of Boxes')
plt.ylabel('Amount')
plt.scatter(x,y , color='red', marker='*')
plt.grid()
plt.show()

## If there is any way in which we can create a scatter plot from line plot only 
## Line Plot ----> Special case of scatter plot as soon as we will join the points of scatter plot we will get the line plot.
## If you want to come up with a scatter Plot from a Line Plot
## plt.plot(x,y, 'o')
## Large DataSet: ----> Crores of Rows -----> plot('o') ---> Scatter Plot ----> Faster
## Small Dataset: ----> Hundered or Thousands of Rows -----> Scatter()----> Scatter Plot ---> Faster























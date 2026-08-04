### Matplotlib 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Student Depression Dataset.csv')  ## Data Gathering 
records = print(df.sample(5))


## groupby()---> DataSet---> Country ----> Sales Info
   #### Country Sales
   #### India   150
   #### China   5000
   #### USA     1000
   #### India   5000
   #### USA     4000

## Total sales I am getting Country Wise
   ### group1 --------> India -----> 5150
   ### group2 --------> USA -------> 5000
   ### group3 --------> China ------> 5000   

## groupby: It helps to group the rows based on the row values and the values associated with the group, onto those values some mathematical function can be applied like (sum(),mean(), and more)
# syntax for groupby: df.groupby('categorical Column name')['Numerical Column'].mathematical function
# df.groupby('Country')['sales'].sum()

# Line Plot : Age vs CGPA
# 
# top_ten = df['Age'].value_counts().head(10)

data = df.groupby('Age')['CGPA'].mean().head(10)  
x = data.index
y = data.values

plt.figure(figsize=(10,5))
plt.title('CGPA Distribution as Per Age')
plt.xlabel('Age')
plt.ylabel('CGPA')
plt.plot(x,y, color='red',linestyle='--',linewidth='1.5',marker='*')
plt.grid()

data = df.groupby('City')['Financial Stress'].mean().head(10)  
a = data.index
b = data.values

plt.figure(figsize=(10,5))
plt.title('City-Wise Financial Stress')
plt.xlabel('City')
plt.ylabel('FInancial Stress')
plt.plot(a,b, color='red',linestyle='--',linewidth='1.5',marker='*')
plt.grid()
plt.show()


### To convert a Date Column to datetime you can use pd.to_datetime()
### To extract the year from the DateTime Column ----> df['col_name'].dt.year
### To extract the Month Value (1-12) from the DateTime Column --> df['col_name].dt.month
### To extract the Month name from the DateTime column ---> df['col_name].dt.month_name() 

 ## if we want to convert datatype then we can use
 ## df['column_name'] = df['column_name'].astype('category')
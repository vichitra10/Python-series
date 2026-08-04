import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Student Depression Dataset.csv')  ## Data Gathering 

### Getting started with bar plot

## Line Chart: Line chart being used for representing Time Series Analysis

### Scatter Plot: Scatter Plot is used to represent the corelation in between Two Numerical Columns (Such that How on changes in the first numerical column it affects the variation in the second Numerical Column )

### Bar Plot: Bar Plot is being used for categorical Numerical Columns
### Data : Sales in Multiple Countries ---> group the rows on the basis of Country Name and will come up with the total sum of sales
### 1000 records ---> 80 records ----> India -----> group all 80 rows or records  ---> Sales values associcated with these 80 rows ---> Aggregation Operation (sum(), count(), mean())
## Categorical Column : Numerical Column Aggregation
## groupby: is something we will using EveryTime
## Univariate and Bivariate Both Analysis will be done in Bar Plot
## Univariate: Categorical Column Data Distribution (How the data in Multiple Categories is Distributed)
## USe Case: Aggregate Analysis of Groups 

# data = df.sample()
# print(data)

data  = df['Gender'].value_counts()
# print(data)

x =  data.index
y = data.values

## Plotting bar plot ---- bar()---->plt.bar()
plt.bar(x,y)
# plt.show()


## Dietary Habits vs Depression
# dietary_habits = df['Dietary Habits'].value_counts()
# print(dietary_habits)

## want to remove some records from the dietary habits for others category
data = df[(df['Dietary Habits'] == 'Healthy') | (df['Dietary Habits'] == 'Moderate') | (df['Dietary Habits'] == 'Unhealthy')]
data['Dietary Habits'].value_counts().plot(kind='bar')
plt.title('Dietary Habits Distribution')
plt.xlabel('Dietary Habits')
plt.ylabel('Count')
plt.grid(axis='y')
plt.show()

## remove_unused_categories() 
## concat(): concat() function joins two dataset or Multiple dataset by using concat()
## pd.concat([df_1, df_2,df_3])


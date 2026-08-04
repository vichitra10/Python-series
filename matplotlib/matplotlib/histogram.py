import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Student Depression Dataset.csv')  ## Data Gathering 

## Histogram Chart
## Educational Youtube Channel: Age Group ---> 15-45 ---> Maximum Students from the age group of 15 to 20 OR 20 to 25 OR 25 to 30 OR 30 to 35 OR 35 to 40 OR 40 to 45

## 20-25 Years Age Group: 10K Students
## 25-30 Years Age Group: 20K Students

## Histogram can help us with the Univariate Analysis of the Numerical Column , by coming up with the insights by coming up with the fixed Equal Interval in the Numerical Column values
## bins basically used for the interval
## Plotting an Histogram : plt.hist([df['numerical'] , bins = [20,30,40,50,60,70]])

min_age = df['Age'].min() ## getting minimum age of a student
max_age = df['Age'].max() ## getting maximum age of a student 

plt.hist(df['Age'],bins=[20,25,30,35,40,45,50,55,60], log=True)
plt.grid()
# plt.show()

## Logarithmic Scale : 0 to 10 , 10 to 10 square, 102 to 103(square)
## plt.hist()

## for CGPA Column
plt.figure(figsize=(10,4))
plt.title('Total Students Distribution as per CGPA')
plt.xlabel('CGPA')
plt.ylabel('Number of Students')
plt.hist(df['CGPA'],
         bins=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0],
         log=True)
plt.grid()
plt.show()
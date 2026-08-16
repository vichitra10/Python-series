## Distribution Plots

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('Student Performance Dataset.csv')

## Histogram
plt.figure(figsize=(8,5))
sns.histplot(data=df,x = 'G3')
plt.title('Distributions of final Grades')
plt.xlabel('Final Grade (G3)')
plt.ylabel('Number of Students')
plt.show(block=False)


## KDE Plot
plt.figure(figsize=(8,5))
sns.kdeplot(data=df, x= 'G3')
plt.title('KDE of final Grades')
plt.xlabel('Final Grade (G3)')
plt.ylabel('Number of Students')
plt.show(block= False)


## Rug Plot

plt.figure(figsize=(8,5))
sns.rugplot(data=df, x='G3')
plt.title('Rug Plot of Final Grades')
plt.xlabel('Final Grade (G3)')
plt.show(block=False)

## Combine Histogram and Kde in a single plot

plt.figure(figsize=(8,5))
sns.histplot(data=df,x='G3',kde=True)
plt.title('Distribution of Final Grade with KDE')
plt.xlabel('Final Grade (G3)')
plt.ylabel('Number of Students')
plt.show()
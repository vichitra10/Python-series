## Categorical PLots

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Student Performance Dataset.csv')

## Bar Plot

plt.figure(figsize=(8,5))
sns.barplot(data=df,x='sex',y='G3')
plt.title('Average final grade by sex')
plt.xlabel('Sex')
plt.ylabel('Average Final Grade')
plt.show(block=False)

## Box Plot

plt.figure(figsize=(8,5))
sns.boxplot(data=df,x='sex',y='G3')
plt.title('Average final grade by sex')
plt.xlabel('Sex')
plt.ylabel('Average Final Grade')
plt.show(block=False)

## Violin Plot

plt.figure(figsize=(8,5))
sns.violinplot(data=df,x='sex',y='G3')
plt.title('Average final grade by sex')
plt.xlabel('Sex')
plt.ylabel('Average Final Grade')
plt.show(block=False)


## Count Plot

plt.figure(figsize=(8,5))
sns.countplot(data=df,x='sex')
plt.title('Average final grade by sex')
plt.xlabel('Sex')
plt.ylabel('Average Final Grade')
plt.show()
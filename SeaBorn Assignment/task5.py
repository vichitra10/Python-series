## Matrix Plots

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Student Performance Dataset.csv')

## Pair Plot

sns.pairplot(
    data=df,
    vars=['age', 'absences', 'G1', 'G2', 'G3']
)

plt.show(block='False')

## Heatmap of Corelation Matrix

corr = df[['age', 'absences', 'G1', 'G2', 'G3']].corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr,annot=True,cmap='YlGnBu')
plt.title('Corelation Matrix')
plt.show()
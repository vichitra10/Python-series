## Multi PLots & Figure Level Plots

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv('Student Performance Dataset.csv')


## FacetGrid

g = sns.FacetGrid(
    df,
    col='sex'
)

g.map_dataframe(
    sns.scatterplot,
    x='G1',
    y='G3'
)

g.set_axis_labels(
    'First Period Grade (G1)',
    'Final Grade (G3)'
)
g.set_titles('Sex = {col_name}')
plt.show(block=False)

## Relplot

sns.relplot(data=df,x='G1',y='G3',hue='sex',kind='scatter')
plt.show(block=False)


## catplot
sns.catplot(data=df,x='sex',y='G3',kind='box')
plt.show(block=False)

## Displot
sns.displot(data=df,x='G3',hue='sex',kind='hist')
plt.show()
## Regression Plots

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Student Performance Dataset.csv')

## Regression Plot
plt.figure(figsize=(8, 5))

sns.regplot(
    data=df,
    x='G1',
    y='G3'
)

plt.title('Regression Plot: G1 vs G3')
plt.xlabel('First Period Grade (G1)')
plt.ylabel('Final Grade (G3)')

plt.show(block=False)


## Implot with hue

plt.figure(figsize=(8, 5))

sns.lmplot(
    data=df,
    x='G1',
    y='G3',
    hue='sex'
)

plt.title('Regression Plot: G1 vs G3')
plt.xlabel('First Period Grade (G1)')
plt.ylabel('Final Grade (G3)')

plt.show()
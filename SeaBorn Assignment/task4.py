## Bivariate Distribution Plots

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Student Performance Dataset.csv')

## Bivariate Histogram

plt.figure(figsize=(8,5))
sns.histplot(data=df,x='G1',y='G3')
plt.title('Bivariate Histogram : G1 vs G3')
plt.xlabel('First period Grade (G1)')
plt.ylabel('Final Grade (G3)')
plt.show()
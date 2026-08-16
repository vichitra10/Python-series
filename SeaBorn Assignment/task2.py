## Line Plot as Scatter & Facet
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv('Student Performance Dataset.csv')

plt.figure(figsize=(8, 5))
sns.lineplot(
    data=df,
    x='age',
    y='G3'
)
plt.title('Average Final Grade by Age')
plt.xlabel('Age')
plt.ylabel('Final Grade (G3)')
plt.show(block=False)


## Scatter Style Line Plot

plt.figure(figsize=(8, 5))

sns.lineplot(
    data=df,
    x='age',
    y='G3',
    marker='o'
)

plt.title('Average Final Grade by Age')
plt.xlabel('Age')
plt.ylabel('Final Grade (G3)')
plt.show(block=False)

## Faceting using school

sns.relplot(
    data=df,
    x='age',
    y='G3',
    col='school',
    kind='line',
    marker='o'
)

plt.show()
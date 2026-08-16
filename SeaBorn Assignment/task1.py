## Relational Plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



stu_df = pd.read_csv('Student Performance Dataset.csv')
# print(data.head())


## Relation Plot 

sns.relplot(data=stu_df,x='age',y='G3',hue='sex')
plt.title('Age vs Final Grade by Sex')
# plt.show()

## Scatter Plot
plt.figure(figsize=(8, 5))
sns.scatterplot(data=stu_df,x='age',y='G3',hue='sex')
plt.title('Age vs Final Grade by Sex')
plt.xlabel('Age')
plt.ylabel('Student Grade')
plt.show()


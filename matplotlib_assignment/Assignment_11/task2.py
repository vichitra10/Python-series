## Scatter Plot()

import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
sales = pd.read_csv('Chocolate Sales.csv')

# Clean Amount column
sales['Amount'] = (
    sales['Amount']
    .str.replace('$', '', regex=False)
    .str.replace(',', '', regex=False)
    .astype(float)
)

# Create Scatter Plot
plt.figure(figsize=(10, 5))
plt.title('Relationship Between Boxes Shipped and Sales Amount')
plt.xlabel('Boxes Shipped')
plt.ylabel('Sales Amount')
plt.scatter(
    sales['Boxes Shipped'],
    sales['Amount'],
    color='blue',
    marker='o',
    alpha=0.7
)
plt.grid(True)
plt.tight_layout()
plt.show()
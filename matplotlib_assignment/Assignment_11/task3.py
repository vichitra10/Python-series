## Bar Plot ()

import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
sales = pd.read_csv('Chocolate Sales.csv')

total_boxes = sales.groupby('Product')['Boxes Shipped'].sum()

print(total_boxes)

## Vertical Bar Plot

plt.figure(figsize=(15,6))
plt.title('Total boxes shipped by Product')
plt.xlabel('Product')
plt.ylabel('Total boxes Shipped')
plt.bar(total_boxes.index, total_boxes.values, color='skyblue')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

## Horizontal Bar Plot

plt.figure(figsize=(15,6))
plt.title('Total boxes shipped by Product')
plt.xlabel('Total boxes Shipped')
plt.ylabel('Product')
plt.barh(total_boxes.index, total_boxes.values, color='skyblue')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

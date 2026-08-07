## Histogram (Marks Distribution)
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
student = pd.read_csv('Student Depression Dataset.csv')

print(student['CGPA'].head(10))

# Create Histogram
plt.figure(figsize=(8,5))

plt.hist(
    student['CGPA'],
    bins=10,
    color='skyblue',
    edgecolor='black'
)

plt.title('Distribution of Student CGPA')
plt.xlabel('CGPA')
plt.ylabel('Number of Students')

plt.grid(axis='y')
plt.tight_layout()
# plt.show()
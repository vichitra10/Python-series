## Percentiles and Sorting
import numpy as np
marks = np.array([78,85,90,66,72,88,95,60])

sorted_marks = np.sort(marks)

percentile_25 = np.percentile(marks, 25)
percentile_50 = np.percentile(marks, 50)
percentile_75 = np.percentile(marks, 75)

average = np.mean(marks)
above_average = np.sum(marks > average)


print(f"Original Marks: {marks}")
print(f"Sorted Marks: {sorted_marks}")

print(f"\n25th Percentile: {percentile_25}")
print(f"50th Percentile (Median): {percentile_50}")
print(f"75th Percentile: {percentile_75}")

print(f"\nAverage Marks: {average}")
print(f"Students Scored Above Average: {above_average}")
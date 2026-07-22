## Statistical Operations (Core Focus)
import numpy as np
marks = np.array([78,85,90,66,72,88,95,60])

mean = np.mean(marks)
median = np.median(marks)
variance = np.var(marks)
standard_deviation = np.std(marks)
minimum = np.min(marks)
maximum = np.max(marks)
range_value = maximum - minimum


print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {standard_deviation}")
print(f"Minimum Value: {minimum}")
print(f"Maximum Value: {maximum}")
print(f"Range (Max - Min): {range_value}")

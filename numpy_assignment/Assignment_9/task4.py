## Aggregation Operation
import numpy as np
data = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

row_wise_sum = np.sum(data, axis=1)
column_wise_sum = np.sum(data,axis=0)
min_value = np.min(data)
max_value = np.max(data)
overall_mean = np.mean(data)


print(f"Row wise sum of Array {row_wise_sum}")
print(f"Column wise sum of Array: {column_wise_sum}")
print(f"Minimum Value: {min_value}")
print(f"Max Value: {max_value}")
print(f"OverAll Mean: {overall_mean}")
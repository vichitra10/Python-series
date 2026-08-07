## Python functionalities on Series
import pandas as pd
mark_series = pd.Series([78,85,90,66,72])

max_marks = max(mark_series)
print(f"Maximum marks value is:  {max_marks}")
min_marks = min(mark_series)
print(f"Minimu makrs value is : {min_marks}")
total_marks = sum(mark_series)
print(f" Total marks: {total_marks}")
mean = mark_series.mean()
print(f"The mean value is: {mean}")

check_pass_student = lambda: mark_series >= 70
print(check_pass_student())
print("Total Passed Students:", check_pass_student().sum())



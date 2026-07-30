## Pandas Series Basics
import numpy as np
import pandas as pd
marks = [78,85,90,66,72]
marks_series = pd.Series(marks)
# print(series_marks)
print(f" Series Value: {marks_series.values}")
print(f" Series Index: {marks_series.index}")
print(f" Series Data Type: {marks_series.dtype}")
print(f" Series First Element: {marks_series[0]}")
print(f" Series Last two Element: {marks_series[-1:]}")




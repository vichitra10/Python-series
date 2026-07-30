## Mathematical Operation in Series
import numpy as np
import pandas as pd
marks = [78,85,90,66,72]
marks_series = pd.Series(marks)
print(f"Series After Adding Grace Marks: {marks_series + 5}") ## Adding grace marks for every Students
print(f"Series After Subtract 2 Marks: {marks_series - 2}") ## Subtract 2 marks for every Students
print(f"Series After Multiply by 1.05 Marks: {marks_series * 1.05}") ## Multiply all marks by 1.05
print(f"Series After Divide all marks by 2: {marks_series/2}") ## Divide all marks by 2

### Filtering and Conditional Selection
import pandas as pd

student = {'Name': ['Amit','Neha','Rahul','Sneha','Pooja'],
           'Marks': [78,85,90,66,72],
           'Subject': ['Math','Math','Science','Science','Math']
           }
stu_df = pd.DataFrame(student)

data = stu_df[stu_df['Marks'] >75]  ## students who scored more than 75 marks
data1 = stu_df[stu_df['Subject'] == 'Math']  ## students who belonging to subject math

average_marks = stu_df["Marks"].mean()       ## average marks
data2 = stu_df[stu_df['Marks'] > average_marks]  ## Students who scored more than average marks
data3 = stu_df[stu_df['Marks'] < 75]   ## students who failed (marks < 70)


print(f"Students who scored more than 75 marks:\n{data}")
print(f"Students who belonging to subject math:\n{data1}")
print(f"Students who scored more than average marks:\n{data2}")
print(f"Students who failed (marks < 70):\n{data}")
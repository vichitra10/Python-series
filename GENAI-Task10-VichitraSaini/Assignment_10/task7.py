## Grouping and Basic Analysis 
import pandas as pd

student = {'Name': ['Amit','Neha','Rahul','Sneha','Pooja'],
           'Marks': [78,85,90,66,72],
           'Subject': ['Math','Math','Science','Science','Math']
           }
stu_df = pd.DataFrame(student)

subject_average_marks = stu_df.groupby("Subject")["Marks"].mean()
student_count = stu_df.groupby("Subject")["Name"].count()
max_marks = stu_df.groupby("Subject")["Marks"].max()

print(f"Average marks per subject:\n{subject_average_marks}")
print(f"Number of Student per Subject:\n{student_count}")
print(f"Maximum marks per subject:\n{max_marks}")


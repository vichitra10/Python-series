## Create a DataFrame
import pandas as pd
student = {'Name': ['Amit','Neha','Rahul','Sneha','Pooja'],
           'Marks': [78,85,90,66,72],
           'Subject': ['Math','Math','Science','Science','Math']
           }

print(student)

## convert into a dataframe
student_df = pd.DataFrame(student)
# print(student_df)


head_data = student_df.head(3)  ## get first 3 rows
print(head_data)
tail_data = student_df.tail(2)  ## get last 2 rows
print(tail_data)

shape_data = student_df.shape  ## shape data 
print(shape_data)

columns_data = student_df.columns
print(columns_data)


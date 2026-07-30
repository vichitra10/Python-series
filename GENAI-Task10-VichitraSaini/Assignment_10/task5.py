## Important Dataframe functions
import pandas as pd

student = {'Name': ['Amit','Neha','Rahul','Sneha','Pooja'],
           'Marks': [78,85,90,66,72],
           'Subject': ['Math','Math','Science','Science','Math']
           }
stu_df = pd.DataFrame(student)
stu_df.info() ## info function
print(stu_df.describe())  ## describe function
print(stu_df.head())      ## head function
print(stu_df.tail())      ## tail function
sorted_df = stu_df.sort_values(by="Marks", ascending=False)
print(sorted_df)

sorted_df = sorted_df.reset_index(drop=True)

print(sorted_df)

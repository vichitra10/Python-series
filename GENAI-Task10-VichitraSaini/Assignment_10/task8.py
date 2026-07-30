## Pandas Plotting (Simple Graphes)
import pandas as pd

students = {
    "Name": ["Amit", "Neha", "Rahul", "Sneha", "Pooja"],
    "Marks": [78, 85, 90, 66, 72],
    "Subject": ["Math", "Math", "Science", "Science", "Math"]
}

stu_df = pd.DataFrame(students)
print(stu_df.plot(x="Name", y="Marks", kind="bar"))
print(stu_df["Marks"].plot(kind="line"))
print(stu_df["Marks"].plot(kind="hist"))
## Read File Safely (Error Handling Inside File Handling Only)
import os

# print(os.getcwd())
filename = input("Enter the file name: ").strip()

if os.path.exists(filename):
    file = open(filename, "r")
    print(file.read())
    file.close()
else:
    print("File not found. Please check the filename.")
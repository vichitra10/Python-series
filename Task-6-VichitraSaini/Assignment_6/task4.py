# File Reader with Exception Handling
try:
    filename = input("Enter the filename: ")

    with open(filename, "r") as file:
        lines = file.readlines()

        print("First 3 lines:")
        for line in lines[:3]:
            print(line.strip())

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

finally:
    print("File operation attempted.")
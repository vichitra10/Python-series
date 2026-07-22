## Safe Division Utility
try:
    numerator = int(input("Enter Numerator: "))
    denominator = int(input("Enter Denominator: "))

    result = numerator/denominator
except ValueError:
    print("Error: Please Enter a valid number")
except ZeroDivisionError:
    print("Error: Denominator can not be zero")
else:
    print(f"Result: {result}")
finally:
    print("Operation Completed")            


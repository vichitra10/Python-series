import numpy as np

A = np.array([10,20,30,40])
B = np.array([1,2,3,4])


Addition = A + B
Subtraction = A - B
Multiplication = A * B
Division = A / B
Power = A ** 2

print("Addition:", Addition)
print("Subtraction:", Subtraction)
print("Multiplication:", Multiplication)
print("Division:", Division)
print("Power:", Power)


## use of np.add() 
Addition1 = np.add(A,B)
Subtraction1 = np.subtract(A,B)
Multiplication1 = np.multiply(A, B)
Division1 = np.divide(A, B)

print("Addition:", Addition1)
print("Subtraction:", Subtraction1)
print("Multiplication:", Multiplication1)
print("Division:", Division1)
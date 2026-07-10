## Recursive Function: Factorial Utility

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    if n == 0:
       return 1
    elif n == 1:
       return 1
    else:
        return n * factorial(n - 1)   
    
print(factorial(5)) # Output will be :   120
print(factorial(0)) # Output will be : 1
print(factorial(-1)) # Output will be : maximum recursion depth exceeded
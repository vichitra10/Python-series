 ## Creating NumPy Arrays
import numpy as np

OneDArray = np.arange(1,11)
twoDArray = np.arange(1,10).reshape(3,3)
listArray = np.array([10, 20, 30, 40, 50])

# Print shapes
print("OneDArray shape:", OneDArray.shape)
print("twoDArray shape:", twoDArray.shape)
print("listArray shape:", listArray.shape)

# Print data types
print("OneDArray dtype:", OneDArray.dtype)
print("twoDArray dtype:", twoDArray.dtype)
print("listArray dtype:", listArray.dtype)
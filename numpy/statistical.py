import numpy as np
## Statistical Function in Numpy
  ## mean() ---> syntax for mean()-->np.mean
array_data = np.arange(1,17).reshape(4,4)
print(array_data)
print(np.mean(array_data)) ## default mean for the matrix
print(np.mean(array_data, axis=0)) ## mean for all columns
print(np.mean(array_data,axis=1))  ## mean for all  rows

## Median: To calculate Median of all values in the array or Matrix
   ## syntax for median: np.median()
  
array_data = np.arange(1,17).reshape(4,4)
print(array_data)

print(np.median(array_data)) ## default median
print(np.median(array_data,axis = 0) ) ## for column wise median
print(np.median(array_data, axis = 1)) ## for row wise median

## var --> It helps with calculating the variance of all values inside the array or matrix
   ## syntax ---- np.var()

print(np.var(array_data)) ## variance of array data
print(np.var(array_data,axis = 0))  ## column wise variance
print(np.var(array_data,axis = 1))  ## row wise variance


                                    ###-------------Trigonometric Functions ---------------###

## sin() ---> sin value for the value we are going to pass inside it
## tan()
## cos()
print(f" The value of sin 0: {np.sin(0)}")
print(f" The value of tan 45: {np.tan(45)}")
print(f" The value of cos 90: {np.cos(90)}")

## Dot product of Matrices
    ##syntax : np.dot(matrix1,matrix2)

matrix_1 = np.round(np.random.random((3,4))*100).astype('int32')
matrix_2 = np.round(np.random.random((4,3))*100).astype('int32')

print(matrix_1)
print(matrix_2)

result = np.dot(matrix_1,matrix_2)
print(result)


## log() : To calculate the log of all values of our Matrix
   ## syntax : np.log

print(np.log(matrix_1))

## exp(): exponentional function to all values inside the matrix
    ## syntax: np.exp()

print(np.exp(matrix_1))

## round(): It helps us with rounding off the float values to its nearest possible interger value
   ##syntax: np.round(array)
   ## round of value for 1.7 --->2
   ## round of value for 1.3 --->1

   ## ceil() --> 1.6 will be 2 and 1.3 will be 3 also (Next corresponding value)
   ## floor() --> 1.6 will be 1 and 1.3 will be 1 also (Previous value)
    # np.round()
    # np.ceil()
    # np.floor()

random_array = np.random.random(3)*100
print(random_array)

print(f" Result with round function :{np.round(random_array)}")
print(f" Result with ceil function :{np.ceil(random_array)}")
print(f" Result with floor function :{np.floor(random_array)}")

## Transpose(): It calculates the transpose of the given matrix
   ##syntax : np.transpose(arr) or arr.T
   ## transpose --> (i,j) ----> (3,4) ----->T ---->(4,3)

transpose_array = np.arange(1,13).reshape(3,4)
print(transpose_array)

print(np.transpose(transpose_array)) 
print(transpose_array.T)

## Ravel(): Convert ND array into 1D Array
    ## syntax : np.ravel()

print(f"Use of Ravel function: {np.ravel(transpose_array)}")

## Indexing and Slicing in Numpy
   ## Indexing ---> lists[size-1] ---> To have the access over the values 
   ## Indexing in 2D Array  ----> [row, column]
   ## Indexing in 3D Array ------> [z-axis, y-axis, x-axis]

index_exp = np.round(np.random.random((5, 5)) * 100).astype('int32')
print(index_exp)
print(index_exp[2,3])

multiArray = np.arange(1,9).reshape(2,2,2)
print(multiArray)

## Iterating over an Array
new_array = np.arange(1,10)
for i in new_array:
    print(i)

## for multi dimensional array we can iterate the array with the help of nditer()  
   ##syntax ---> np.nditer(arr)  

print(multiArray)
for i in np.nditer(multiArray):
    print(i)  

## 1D Array ----> value by value iteration
## 2D Array ----> Row by Row Iteration
## 3D Array ----> 2d Array by 2d Array  


                                 ## Staking and Splitting Array ##
## Stacking: Joining the Array Together
## Horizontal Stacking: Row by Row Joining is done --hStack()
## Vertical Stacking: Column by Column Joining is done ---vStack()

array_one = np.arange(1,13).reshape(3,4)
array_two = np.arange(13,25).reshape(3,4) 


horizontal_stack = np.hstack((array_one, array_two))
print(array_one )
print("\n")
print(array_two)
print(horizontal_stack)

vertical_stack = np.vstack((array_one, array_two))
print(vertical_stack)


## Horizontal Split : np.hsplit(array, number of parts you want your array to be splitted at)
## vertical Split: np.ssplit(array,number of parts)

print(np.vsplit(vertical_stack,3))
print(np.hsplit(horizontal_stack,2))

    

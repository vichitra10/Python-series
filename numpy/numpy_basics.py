import numpy as np
numpy_array = np.array([1,2,3,4,5]) ## One Dimensional Array
# print(numpy_array)
# print(type(numpy_array)) ## Check type of Array


## Two Dimensional Array
two_dime_array = np.array([[1,2,3],[4,3,5],[2,6,7]])
# print(two_dime_array)
# print(type(two_dime_array))

## Three Dimensional Array
three_dime_array = np.array([[[1,2],[3,2],[5,6]], [[3,2],[3,8],[6,6]],[[3,9],[6,8],[9,6]]])
# print(three_dime_array)
# type(print(three_dime_array))


## range function : for range i to 20 (with using loop )
empty_list = []
for i in range(21):
    empty_list.append(i)
# print(empty_list) 

## but if we use np.arange function then we dont need a loop for specific list like above , we can simply use 
# array_list = np.arange(21)
# print(array_list)

## with the help of we can pass a certain range nd if we want to some gap in the list we can pass parameter as well as
# print(np.arange(1,21)) ## start list with 1 to 20 bcoz indexing start with the zero 
# print(np.arange(5,21)) ## give a list which with 5
# print(np.arange(0,100,5)) ## give a array list with 5 gap

arrange_data = np.arange(1,17)
arrage_shape_data = arrange_data.reshape(4,4) ## first number is row and the second one is used for column
print(arrange_data)
print(arrage_shape_data)


## np.reshape: this function is used to help us out with changing the shape of the array as per our needs

new_arrange_shape_data = arrange_data.reshape(2,8)
print(new_arrange_shape_data)

## np.zeros: 
zero_data = np.zeros((4,5),dtype=int)
print(zero_data)

## random(): It helps us out with generating any random values from 0 to 1 inside our matrix
random_data = np.random.random((3,4))
print(random_data)

## Identity: It helps us out creating the matrix as an Indentity Matrix or called square matrix(Rows=Colums)
identity_data = np.identity(3)
print(identity_data)

## linspace(): Its makes sure that every value with the given range is going to have similiar distance from each other
linspace_data = np.linspace(-10,10,10)
print(linspace_data)

## ndim: stands for N dimension

arr = np.array([1,2,3])
print(arr.ndim) ## Output will be 1 which means its one dimesional array

## shape : Its provide us with the idea about the rows, columns in our dataset or in array 
new_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(new_array.shape)

## size: Total number of elements present inside our Dataset or Array
array_element = np.arange(5,56)
print(array_element.size)


## itemsize
print(np.array([[1,2],[2,4],[4,1]], dtype=np.int32).itemsize)

## dtype: It provide us with the idea about the every type inside our array

## astype(): astype() will be helping us out with figuring out the data type of the column in the dataset in pandas and it will be used in numpy as well for getting the data type changed of our overall array


## Mathematical Operation in Numpy
## Scaler Operation: A scaler value will be multiplied with the array or a numeric value (e.g, 1.4)

## Important function in Numpy for Machine Learning and Data Science

# max(): It is going to be used to calculate the max value inside a matrix or an array 
   ## synatx for max() --> np.max()
array_data = np.arange(1,17).reshape(4,4)
print(array_data)
print(f"The max value is {np.max(array_data)}")


## axis(): It provides us with the idea about the any operation value inside a specific row or column or we can get a specific value row wise or column wise

    ## axis=0  ----> Column wise Operation
    ## axis=1  ----> Row wise Operation

print(np.max(array_data,axis = 0))  ## this is for column
print(np.max(array_data,axis=1))    ## this is for row rows


## and we also have min() function and the synatx for np.min()
## sum() : Calculates the sum of the all values of a given matrix or array
   ## synatx of sum() : np.sum()

print(f"The sum of array value for 0 axis: {np.sum(array_data, axis=0)}")
print(f"The sum of array value for 1 axis: {np.sum(array_data, axis=1)}")


## prod(): Its helps with calculating the product of all values inside the matrix
    ## syntax for prod(): np.prod() 
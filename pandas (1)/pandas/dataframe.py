import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
## DataFrame can be created in 3 ways
   #@ Lists -------> dataframe
   #@ Dictionary -------> dataframe
   #@ read_csv() -------> dataframe

## dataframe ---> combination of rows and column -----> 2D Data Structure
rows = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
list_data = pd.DataFrame(rows,columns=['A','B','C'])
# print(list_data)
# print(list_data.shape)

## Dictionary ----> Dataframe
## Dictionary -----> dataframe -----> rows and column combination

dict_data = {'Name': ['Amit','Yash','Vivek'], 'Money(In lacs)':[1,5,7], 'Financial_stress':[1,1,0]}
dict_data_list = pd.DataFrame(dict_data)
# print(dict_data_list)

## read_csv(): 

data_set = pd.read_csv('Student Depression Dataset.csv')
# print(data_set)

## Data Exploration ---> Attributes & Functions for the Dataframe
   #### Attributes
       
       ## shape ----> It provides the info about the (row and column) information about the dataset
           ## syntax: data_set.shape

       ## dtypes: It provides the idea about the datatype of all columns, so all columns with their name and their assoicated will be shown by using dtypes
           ## syntax: data_set.dtypes

       ## index: For a Dataframe with labelled index we can get the idea about the label just by using index attributes
       ## columns:  It provides the idea about all of the column names of the given dataframe
       ## values: It provides the idea about the values present row by row inside the dataframe. It always return numpy array representing the value of column row by row 
       ## ndim: It provides the idea about the dimension about the dataframe
       ## size: It provides the idea total number of elements presents inside the dataframe, that means all rows multiplied all columns


    ### Some Important Functions 

        ## head(): to get to have the idea about the data that your dataset is storing as the top five rows , that means starting from the top we can get the top 5 rows and along with that if i want that instead of top 5 rows i want to to see a fixed no of rows from the dataset that number I can pass inside the head() as a parameter.

        ## tail(): it will provides the insight about the dataframe from the bottom so tail() can show us the bottom 5 rows and again based on the value you will be passing as the parameter, those many values you can get using the tail fn = ()  

        ## sample(): provides the insight about the dataframe as the random values present inside the dataset and again based on how many values i want , I can put the parameter as per that . 

        ## info(): provides the idea about the datatype of all column , number of missing value of all columns, dataframe storage in memory
        ## describe(): It provides an idea as the mathematical summary of the data ---minimum, maximum,count,mean,std,25%,50% and more
        ## Missing value or not ----> isnull()
        ## duplicate value are present or not in dataset --->duplicated()
        ## Renaming the column as well (In order to make sure that the changes are going to be permanent we can go with inplace parameter)


          


## Attributes Example
# print(data_set.shape) 
# print(data_set.dtypes)    
# print(data_set.index)     
# print(data_set.columns)  
# print(data_set.values)
# print(data_set.size)


## Function Example we have
# print(data_set.head()) 
## or we can get the how many number of rows we can get
# print(data_set.head(19))

# print(data_set.tail())
# print(data_set.sample())
# print(data_set.info())
# print(data_set.describe())
# print(data_set.isnull())
# print(data_set.isnull().sum())
# print(data_set.duplicated())
# print(data_set.duplicated().sum())

data_set.rename(columns={'CGPA':'Cgpa'},inplace=True)


## Some mathematical Functions in Dataframe 
   ## sum() :  It calculate the sum of all values present in a column or in multiple column
   ## mean(): It calculates the average of all values or mean of all values in a column
   ## min(): It calculates the minimum value of a column
   ## max(): It calculates the maximum value of a column
   ## median(): It calculates the median value of a column
   ## var(): It calculates the variance of all values of a column 
   ## axis(): It helps us calculate the mathematical calculation row wise or column wise
   ## mathematical operation ---> row wise ---> axis=1
   ## mathematical operation ---> column wise ---> axis=0


## Flitering data stored in dataframe for coming up with the important insights
     ## filter 1: Students ---Gender -->male , Age < 24, City --->Pune
## value_counts(): This function is being used to calculate the count of the categoriacal values and that means that what is the count of the first category , count of second category ...
# For the given column  ----> 4 categories  ------> count of each category from the column itself     

print(data_set)
student_filter_data =   data_set[(data_set['Gender'] == 'Male') & (data_set['Age'] < 24) & (data_set['City'] == 'Pune')]
# print(student_filter_data)

age_count = data_set['Age'].value_counts()
gender_count = data_set['Gender'].value_counts().plot(kind='bar')
# print(age_count)
# plt.show()

gender_count.plot(kind='bar')
plt.title("Gender Count")
plt.xlabel("Gender")
plt.ylabel("Count")
# plt.show()

# print(plt.get_backend())

## strip(): It helps to remove any additional spaces or bracket or anything you want to remove from the
data_set['Sleep Duration'] = data_set['Sleep Duration'].str.strip(" ' ")


## Add New column in Dataframe :  data_set['column_name'] = 'Scaler Value'
## data_set['new_column] = data_set['col1'] + data_set['col2']
## data_set.drop(column = "[column name]") : remove a specific column from the dataset
## astype: change the datatype of a specific column and its helps us out with covering less memory storage

data_set['Name'] ='Vichitra' 
print(data_set)
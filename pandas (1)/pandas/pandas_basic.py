## Pandas: Pandas is a powerful library used for Data Manipulation and Analysis. It helps us to work with data in Tabular Format , just like how we deal with data and spreadsheet in excel or database.

## Pandas provide functionalities and attributes to clean, organize and large amounts of data
## Why should we learn: Works like Excel inside Python
## Fast: Handles Large Data Faster than Manual Methods
## Clean Data: Helps clean, filter, and transform messy Data
## Integrates well: Matplotlib, Seaborn
## Ideal For Ml and AI: It is ideal for data Science

import numpy as np
import pandas as pd

## Pandas Series is a column of data in a table like in Excel or Google sheets with lables called as indexes attached to each value.
## Series is a 1D Array that can hold any type of data like integers , float, strings(object), boolean


## Data Type --> Integers ---> Data in a series(Column)---> Quantity of items in the stock
## Data Type --> Float ---> Data in a Series(Column) ----> Price or product Ratings
## Data Type --> Strings ---> Columns -----> Product Name
## Data Type ---> Boolean ---> Column -----> Is Item in stock or not
## Data Type ----> Dates/Times ---> Column ----> Expiry Date or Sales Dates 
## Mixed Type ---> Milk, 40, True


## Creating the Series in Multiple Ways
   ## List
   ## Numpy Array
   ## Dictionary
   ## Custom Index
   ## Scaler Value


## Series with List
country = ['India','China','America','Nepal']
print(country)
print(pd.Series(country))

bats_man_run = [48,85,65,20,6,30,19]
print(pd.Series(bats_man_run))


## Series for student marks we can write like this
subject_name = ['Maths','Physics','Chemistry','Biology','English']
subject_marks = [58,92,64,50,70]
subject_marks_series = pd.Series(name = "Subject Marks Data",dtype='int32',data=subject_marks, index=subject_name)
print(subject_marks_series)


## creating series using numpy array
values = np.arange(10,21)
print(pd.Series(values))

## Dictonaries to series
  ## Dictionary is another Data Structure that store the data in a key value pair and 
  ## Just because it stores the data in a key value pair so we dont have to explictily mention the index

data_items = {'Maths':78,'English':70,'Physics':88,'Chemistry':70,'Biology':55}
print(pd.Series(data_items))

## Custom Index to series
value = [1,2,3,4,5]
index = ['A','B','C','D','E']
print(pd.Series(data=value,index=index))


## Scaler value inside an Series
print(pd.Series(4,index=('a','b','c','d')))


# df = pd.read_csv("youtube_tech_channels_20251120_133753.csv")

# subs = df[["channel_name", "subscribers", "total_views","total_videos"]]

# subs.to_csv("youtube_channels_small.csv", index=False)

# print("New CSV created successfully!")

   

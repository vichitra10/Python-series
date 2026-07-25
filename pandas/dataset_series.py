import pandas as pd
### Read World dataSets in the Series
  
## read_csv(): this function reads the content from the csv file in pandas so that we can perform the operation on the data or we can perform affective analysis.

## DataFrmae: Combination of Multiple Series
## squeeze: squeeze parameter makes sure that the data is in series format

## Attributes in the Series

    ## 1. .values ---> representing only the value of the given series
    ## 2. .index ----> returns only the index value from the given column
    ## 3. dtype ---> Dtype provides the idea about the data type of the values that you are storing
    ## 4. size ----> this attributes provides the idea about the total number of rows inside the dataset
    ## 5. shape ---> this attribute provides the idea about the row and column information
    ## 6. ndim ----> provides the idea about the dimension of the given data set
    ## 7. name -----> this attributes provide the idea about the name of series
    ## 8. is_unique ----> this proides us with the idea wheather its unique value or not inside the column


df = pd.read_csv("youtube_channels_small.csv")
dataframe = df[["channel_name", "subscribers", "total_views","total_videos"]]
# print(df.values)
# print(df.index)



## series methods
   ## head(): Provides the top preview of data as the top 5 rows of the dataframe or series. It is quite helpful with providing the the preview of the dataset and if we want to preview top 10 rows then we can pass 10 as an argument or for 7 rows we can pass 7 rows

   ## tail(): Provides the Bootom preview of Data as the Bottom 5 rows.
   ## sample(): Provides any custom row from the dataset for us to preview it
   ## value_counts(): It provides the idea about the count of the values (categorical value), if i am having a column where the categorical value count I want to calculate then i can go with value_count()

   ## sort_value() --> This function sort the values in asscending order for the numerical columns  and as well as we can get the value in descending order with the help of passing the argument as asscending=false

   ## sort_index() ==> this function sort the index of the dataset

top_five_rows = dataframe.head()
# print(top_five_rows)
    
bottom_five_rows = dataframe.tail()   
# print(bottom_five_rows)

random_row_data = dataframe.sample()
# print(random_row_data)

avg_data =  dataframe['total_videos']
# print(avg_data)
# print(avg_data.value_counts())


sort_data_ascending = dataframe['total_videos'].sort_values()
sort_data_decending = dataframe['total_videos'].sort_values(ascending=False)
# print(f"Data in Ascedning Order: {sort_data_ascending}")
# print(f"Data in Descending Order: {sort_data_decending}")


## Method Chaining:  We will use multiple methods together to get the required value in a way the first method output will be second method input then second method output will be third method input


# print(dataframe['total_videos'].sort_values(ascending=False).head(1))
# print(dataframe['total_videos'].sort_values(ascending=False).head(1).values)


## order to make a change in our data permanent : inplace
# sort_data_ascending.sort_values(inplace=True)
print(sort_data_ascending)
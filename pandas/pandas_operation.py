import numpy as np
import pandas as pd

df = pd.read_csv("youtube_tech_channels_20251120_133753.csv")
subs = df[["channel_name", "subscribers", "total_views","total_videos"]]



total_subs = subs['subscribers'] 
# print(total_subs)

## Mathematical Operation in Pandas

    ## sum()---> sum of all values presents inside the series
    ## product()---> product of all values in the series
    ##  mean() ----> mean provides us with the average value of the data column
    ### for eg: Company Data ---> salary ---> average value for that column salary = 7,8,9,10
    ### describe(): ----> describe function provides the idea about the summary of the important mathematical calculations for the data
    ## median:  Median also provide the idea about the average of data, for coming up with median , we need to sort the values in Ascedning manner and then middle value after sorting the data
    ## mode(): Mode Provides us with the idea that which value is getting repeated maximum 
    ## std(): If i need to get the idea that how the value are disctributed from the average or mean value then we can come up with the standard deviation

    ##  min(): ---> For minimum value
    ## max(): ----> For Maximum Value
    ## mean(): ----> average value
    ## std(): ------> standard deviation
    ## 25% -----> 25% of the value out of my all values are less than this specific value
    ## 50% -----> 50% of the value out of my all values are less than this value
    ## 75% -----> 75% of the value out of my all values are less than this specific value
    ## count: ----> Total number of rows in the column

     ## For example
    ## JEE Mains ---> 25% ---> my score in JEE Mains was greater than 25 % of the total applicants who applied in JEE


print(f"Total number of subscriber: {total_subs.sum()}")
print(f"Product Value: {total_subs.product()}")
print(f"Mean Value: {total_subs.mean()}")
print(f"Median Value: {total_subs.median()}")
print(f"Mode Value: {total_subs.mode()}")
print(f"Standard Deviation: {total_subs.std()}")


##### Indexing in series(To have the access over the certain value or values)
      ##1.  Positive Indexing (Just like list)
      ##2.  No Negative Indexing
      ##3. Slicing---> In series we can get  the certain values over a given specific range and we can do it using the [initial_val:final_value+1]
      ## if i want to skipped value as a certain value
      ### Reverse value in a series
      ### Fancy Indexing: If i want the specific value from the series then we go with fancy indexing
      ### Indexing with label--> A series which is constisting of Lables as the index or custom index, then for this data we can reterive the info using the custom index and custom label

### Editing the Series(Bring the changes into the values stored inside the series)
    ### 1. Using Indexing ----> df[0]=65 ---> Changing the original value at index at 0 to 65 
    ### If indexing does not exists


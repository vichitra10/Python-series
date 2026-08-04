### Matplotlib 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## Use of MatplotLib
## Data Visualization: We can extract information and Patterns by creating Visuals and Graphs and we can analysis some important insights. 
### Different Kinds of Visualization
   ## 1)  2D Plot
   ## 2) Scatter Plot 
   ## 3)  Bar Chart
   ## 4)  Histogram
   ## 5) Pie Chart

df = pd.read_csv('Student Depression Dataset.csv')  ## Data Gathering 
records = print(df.sample(5))


## Data Exploration while Plotting graph -----> Dataset ------> Which Categorical column and Numerical Column
## Categorical Columns :  Gender , City , Profession, Sleep Duration, Diectary Habits, Degree, Family History of Mental Illness
   ### 10 Students ---> 10 Mobile Phone of Different Brands ----> Different Brands -------> Category
        ## Example: (Apple, Nokia, Samsung)
## Numerical Columns : Id, Age, CGPA, Work Study Hours
   ### 10 Students --->  Age -----> 17,20, 49,30,38
        ## Example: (Age, CGPA, Work Study Hours)  



## Univariate Analysis  & Bivariate Analysis

## Univariate Analysis: Analyasis or will be creating visulization for a given unique column  ---> How values are spread in my Age Column
    ## Example 
       ## Age ---> 23 ---> 40 (People having 23years old)

## Bivariate Analysis: Analysis of 2 Columns ---> Column --> Date---> Month
## Column 2 :  ----> Sale in a month

### Plot a Chart:  Month on Month Sales of Products for a Company
## Bivarate Analysis : 1)  Numeric-NUmeric , 2)  Numeric -Categoriacl , 3) Categorical-Categorical


## Multivariate Analysis: Work With Multiple Columns ---> More that 2 columns 



## 2D Line PLOT: 
#### Specific Purpose ----> Specific Plot

#### 2D Line Plot:  It usually work with 2 columns  -----> categorical ---categorical, categorical-Numerical , Numerical-Numerical
#### X Axis: Categorical Column Data or Category
#### Y Axis: Value that is going to change or that varies for the category


### 2d Line Plot or in general Line Plot , It can be used for time series data 
### Time Series Data:  Stock Price on Month  on Month Basis 
### Time Series Data: It is the data that varies with Time or it can be the data where the value varies continousaly  (Phone Brand ----> Price)
### Tracking the Weight over the Months (Time Series Data)
     
     ## Dataset : Indian Actor fees for a Movie  ----> Actor Name: Categorial ---> x Axis
     ##                                          ----> Price: Numerical ------> Y Axis

# x = ['Sharukh Khan','Akshay Kumar', 'Vidhyut', 'Salman Khan', 'Sanjay Dutt']
# y = [800000, 300000,200000,600000,400000]     

## creating a Line Plot  ---> plt.plot(x,y)--->plot()----> create the graph for us

# plt.plot(x,y)
# plt.show()


## Example with our student dataframe which is already used for this
data = df['Gender'].value_counts() ## value_counts is used for total value for gender
x = data.index ## Index for categorical column i.e male or female
y = data.values ## value for numerical column i.e 34,45.20

plt.figure(figsize=(10,4))
plt.title('Count of Population as per Gender', color='red')
plt.ylabel('Count of Population')
plt.xlabel('Gender')
plt.plot(x,y , color='red',marker='o',linestyle= '--', label='Gender Population')
plt.grid()
plt.show()

## plt.figure(): ---> figure --->parameter ---->figsize ----->(len, breadth) ---->figure dimension of our graph
    ## plt.figure = (figsize=(10,6))
## plt.title(): -----> title ----> It takes the value as the title of your plot that what it is representing as what insight we are getting through this graph, It can take the parameter for the color    
    ## plt.title('Count of population as per the Gender)

## plt.ylabel()---> Helps to represent that what Y axis is representing to us
    ## plt.ylabel('Count of Population')
## plt.xlabel()---> Helps to represent that what X axis is representing to use
    ## plt.xlabel('Gender')
## plt.grid() ---> Helps to bring grid on our visulization

## plt.show() ---> helps in representing the chart   
## plt.xlim() ---> X Values ----> [10,1000] ----> [100,1000] ----> [700,800], It puts a limitation that how much the data must be represented on the X Axis 
## plt.ylim() ---> Y values -----> [500,900] ----> [600,700] ---> It puts the limitation that how much value will be shown on the Y-Axis

## Customization for Line
    ## Parameter
    ## 1)  Color:  What is going to be the color of the line ---e.g (red, green, blue or HTML Hash Code)
    ## 2)  marker: How point of intersection appears ---> 'o', '^', '*','#'
    ## 3) linestyle: It will be defining the style of the line ---> '--','-.','...'
    ## 4) linewidth:  It shows the width of the line ----> 1,1.5,2
    ## 5)  markersize: It shows the marker size or it can change the size of the marker, default is 6 , -->,7,8,9
    ## 6)  label: label that what this specific line is representing but is only helpful while plotting multiple lines in a single visulation





### Mini Use Case : Sales Data Analysis
import pandas as pd
sales = {
    'Day':['Mon', 'Tue','Wed','Thu','Fri'],
    'Revenue':[1200,1500,900,2000,1800]
}

sales_df = pd.DataFrame(sales)
# print(sales_df)


total_revenue = sales_df['Revenue'].sum() ## Total Revenue
print(total_revenue)

average_revenue = sales_df['Revenue'].mean() ## Average Revenue
print(average_revenue)

highest_revenue_day = sales_df[sales_df["Revenue"] == sales_df["Revenue"].max()] ## Day with highest revenue
print(highest_revenue_day)

above_average = sales_df[sales_df['Revenue'] > average_revenue] ## Day where Revenue > average
print(above_average)

sales_df.plot(x="Day", y="Revenue", kind="line")  ## Plot revenue vs day
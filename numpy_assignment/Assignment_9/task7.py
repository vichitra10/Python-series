## Mini Use Case: Sales Analysis
import numpy as np
sales = np.array([1200,1500,900,2000,1800,1700,1600])

total_sales = np.sum(sales)
average_sales = np.mean(sales)
highest_sales_day = np.max(sales)
lowest_sales_day = np.min(sales)
standard_deviation = np.std(sales)
above_average_days = np.where(sales > average_sales)[0]

# print(average_sales)
# # print(above_average_days[0])
# print(len(above_average_days))


print(f"Total Sales: {total_sales}")
print(f"Average Sales: {average_sales}")
print(f"Highest Sales Day: {highest_sales_day}")
print(f"Lowest Sales Day: {lowest_sales_day}")
print(f"Standard Deviation: {standard_deviation} ")
print(f"Above Average Days: {above_average_days}")


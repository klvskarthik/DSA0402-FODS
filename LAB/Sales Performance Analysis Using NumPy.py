import numpy as np

sales_data = np.array([10000, 12000, 15000, 20000])

total = np.sum(sales_data)
increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

print("Total Sales:", total)
print("Percentage Increase:", increase, "%")

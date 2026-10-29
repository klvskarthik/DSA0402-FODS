import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [100, 150, 120, 180, 200, 250]

# Line Plot
plt.figure()
plt.plot(months, sales, marker='o')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Monthly Sales Line Plot')
plt.show()

# Scatter Plot
plt.figure()
plt.scatter(months, sales)
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Monthly Sales Scatter Plot')
plt.show()

# Bar Plot
plt.figure()
plt.bar(months, sales)
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Monthly Sales Bar Plot')
plt.show()
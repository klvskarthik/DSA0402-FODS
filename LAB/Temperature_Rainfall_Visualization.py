import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

temperature = [25, 27, 30, 33, 35, 32, 29, 28, 28, 27, 25, 24]
rainfall = [10, 15, 20, 30, 50, 100, 180, 200, 150, 80, 30, 15]

# Line Plot - Monthly Temperature
plt.figure()
plt.plot(months, temperature, marker='o')
plt.xlabel('Months')
plt.ylabel('Temperature (°C)')
plt.title('Monthly Temperature Line Plot')
plt.show()

# Scatter Plot - Monthly Rainfall
plt.figure()
plt.scatter(months, rainfall)
plt.xlabel('Months')
plt.ylabel('Rainfall (mm)')
plt.title('Monthly Rainfall Scatter Plot')
plt.show()
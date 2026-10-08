import numpy as np

house_data = np.array([
    [3, 1500, 250000],
    [5, 2200, 400000],
    [4, 1800, 300000],
    [6, 2500, 500000]
])

houses = house_data[house_data[:, 0] > 4]
average = np.mean(houses[:, 2])

print("Average Sale Price:", average)

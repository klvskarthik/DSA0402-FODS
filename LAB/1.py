import numpy as np

student_scores = np.array([
    [85, 78, 92, 80],
    [90, 82, 88, 75],
    [78, 85, 95, 82],
    [92, 80, 90, 88]
])

subjects = ["Math", "Science", "English", "History"]

avg = np.mean(student_scores, axis=0)
i = np.argmax(avg)

print("Average Scores:", avg)
print("Highest Average:", subjects[i], avg[i])

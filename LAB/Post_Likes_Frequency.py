import pandas as pd

data = {'Likes': [10, 20, 10, 30, 20, 10, 40, 30, 20, 50]}

df = pd.DataFrame(data)

frequency = df['Likes'].value_counts().sort_index()

print("Frequency Distribution of Likes:")
print(frequency)
import pandas as pd

data = {
    'Age': [20, 25, 30, 25, 35, 20, 40, 30, 25, 35]
}

df = pd.DataFrame(data)

frequency = df['Age'].value_counts().sort_index()

print("Frequency Distribution of Customer Ages:")
print(frequency)
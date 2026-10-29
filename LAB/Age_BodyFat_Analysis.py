import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Create dataset
data = {
    'Age': [23, 23, 27, 27, 39, 41, 47, 49, 50,
            52, 54, 54, 56, 57, 58, 58, 60, 61],
    '%Fat': [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2,
             34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
}

df = pd.DataFrame(data)

# Calculate mean, median and standard deviation
print("Statistical Analysis:")
print(df.agg(['mean', 'median', 'std']))

# Boxplots
plt.figure(figsize=(8, 5))
sns.boxplot(data=df)
plt.title('Boxplots of Age and Body Fat')
plt.show()

# Scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(df['Age'], df['%Fat'])
plt.xlabel('Age')
plt.ylabel('Body Fat (%)')
plt.title('Age vs Body Fat Scatter Plot')
plt.show()

# Q-Q plots
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
stats.probplot(df['Age'], dist="norm", plot=plt)
plt.title('Q-Q Plot of Age')

plt.subplot(1, 2, 2)
stats.probplot(df['%Fat'], dist="norm", plot=plt)
plt.title('Q-Q Plot of Body Fat')

plt.tight_layout()
plt.show()
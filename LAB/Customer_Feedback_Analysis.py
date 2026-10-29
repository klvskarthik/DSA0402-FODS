import pandas as pd
import matplotlib.pyplot as plt
import re
from collections import Counter

# Load dataset
df = pd.read_csv("data.csv")

# Stop words
stop_words = {
    'the', 'and', 'is', 'in', 'it', 'to', 'of', 'a', 'for',
    'on', 'with', 'this', 'that', 'was', 'are', 'i', 'very'
}

# Preprocess text
words = []

for feedback in df['feedback'].dropna():
    feedback = feedback.lower()
    feedback = re.sub(r'[^\w\s]', '', feedback)
    for word in feedback.split():
        if word not in stop_words:
            words.append(word)

# Calculate word frequency
frequency = Counter(words)

# Get top N words
n = int(input("Enter the number of top words: "))
top_words = frequency.most_common(n)

# Display frequency
print("\nTop", n, "Most Frequent Words:")
for word, count in top_words:
    print(word, ":", count)

# Plot bar graph
if top_words:
    words_list, counts = zip(*top_words)
    plt.bar(words_list, counts)
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.title("Top N Most Frequent Words in Customer Feedback")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
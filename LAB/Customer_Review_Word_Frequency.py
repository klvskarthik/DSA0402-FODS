import pandas as pd
from collections import Counter
import re

data = {
    'Review': [
        'Good product',
        'Excellent product',
        'Good quality product',
        'Excellent quality'
    ]
}

df = pd.DataFrame(data)

text = ' '.join(df['Review']).lower()
words = re.findall(r'\b\w+\b', text)

frequency = Counter(words)

print("Word Frequency Distribution:")
for word, count in frequency.items():
    print(word, ":", count)
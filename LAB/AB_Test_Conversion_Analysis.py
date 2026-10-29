import numpy as np
from scipy import stats

# Sample conversion rate data
A = [2.5, 3.0, 2.8, 3.2, 2.7, 3.1, 2.9, 3.3, 2.6, 3.0]
B = [3.2, 3.5, 3.8, 3.4, 3.6, 3.7, 3.3, 3.9, 3.5, 3.6]

# Calculate mean conversion rates
mean_A = np.mean(A)
mean_B = np.mean(B)

# Perform independent two-sample t-test
t_stat, p_value = stats.ttest_ind(A, B)

print("Mean Conversion Rate A:", round(mean_A, 2), "%")
print("Mean Conversion Rate B:", round(mean_B, 2), "%")
print("T-statistic:", round(t_stat, 4))
print("P-value:", round(p_value, 4))

# Check statistical significance
if p_value < 0.05:
    print("There is a statistically significant difference.")
else:
    print("There is no statistically significant difference.")
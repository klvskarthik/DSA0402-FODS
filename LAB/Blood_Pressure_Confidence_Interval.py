import numpy as np
from scipy import stats

# Sample blood pressure reduction data
drug = [12, 15, 10, 14, 13, 16, 11, 12, 14, 15,
        13, 12, 16, 14, 11, 15, 13, 12, 14, 16,
        10, 13, 15, 14, 12]

placebo = [5, 7, 4, 6, 5, 8, 3, 6, 4, 7,
           5, 4, 6, 8, 3, 5, 7, 4, 6, 5,
           4, 7, 5, 6, 3]

# Calculate 95% confidence interval
drug_ci = stats.t.interval(
    0.95, df=len(drug)-1,
    loc=np.mean(drug),
    scale=stats.sem(drug)
)

placebo_ci = stats.t.interval(
    0.95, df=len(placebo)-1,
    loc=np.mean(placebo),
    scale=stats.sem(placebo)
)

print("Drug Group")
print("Mean Reduction:", round(np.mean(drug), 2))
print("95% Confidence Interval:", np.round(drug_ci, 2))

print("\nPlacebo Group")
print("Mean Reduction:", round(np.mean(placebo), 2))
print("95% Confidence Interval:", np.round(placebo_ci, 2))
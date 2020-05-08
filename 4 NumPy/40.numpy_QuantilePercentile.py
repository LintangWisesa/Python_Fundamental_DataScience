import numpy as np

c = np.array([1,2,3,4,5,6,7,8,9,10,11])

# Median = Quantile ke 2 (Q2) = Percentile ke-50
print(np.median(c))
print(np.quantile(c, 0.5))
print(np.percentile(c, 50))

# Quantile ke 1 / bawah (Q1)
print(np.quantile(c, 0.25))
print(np.percentile(c, 25))

# Quantile ke 3 / atas (Q3)
print(np.quantile(c, 0.75))
print(np.percentile(c, 75))
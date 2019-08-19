# median: nilai tengah

import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6]])
b = np.array([[1, 2, 3], [4, 5, 6]])
c = np.array([[31, 12, 43, 54, 15, 16]]) 
# median akan sortir dahulu, baru nyari nilai tengah

print(np.median(a))
print(np.median(b))
print(np.median(b, axis=0))
print(np.median(b, axis=1))
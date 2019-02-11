# mean = nilai rata2

import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6]])
b = np.array([[1, 2, 3], [4, 5, 6]])

print(np.mean(a))
print(np.mean(b))
print(np.mean(b, axis=0))
print(np.mean(b, axis=1))
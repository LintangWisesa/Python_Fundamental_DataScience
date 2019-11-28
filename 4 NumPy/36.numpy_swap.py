import numpy as np

arr = np.arange(9).reshape(3,3)
print(arr)

# swap two columns in a 2d numpy array?
print(arr[:, [1,0,2]])
print(arr[:, [2,1,0]])
print(arr[:, [0,0,0]])

# swap two rows in a 2d numpy array?
print(arr[[1,0,2], :])
print(arr[[2,1,0], :])
print(arr[[0,0,0], :])
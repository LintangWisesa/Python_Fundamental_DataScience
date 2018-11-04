
import numpy as np

a = np.array([(1,2,3,4), (5,6,7,8)])
print(a)
print(a.shape)  # output: (2, 4)

a = a.reshape(4,2)
print(a)
print(a.shape)  # output: (4, 2)
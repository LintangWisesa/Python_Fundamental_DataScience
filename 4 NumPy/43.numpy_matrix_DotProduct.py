
# dot product
# |1|   |4|
# |2| . |5| = (1x4)+(2x5)+(3x6) = 32 
# |3|   |6|

import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a.dot(b))
print(a@b)
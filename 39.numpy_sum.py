#     1       2       3     axis1
#     4       5       6     axis1
#   axis0   axis0   axis0

import numpy as np

a = np.array([(1,2,3),(4,5,6)])

print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))
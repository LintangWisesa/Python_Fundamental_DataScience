
import numpy as np

a = np.array([(1,2,3),(4,5,6)])

print(a.sum())
print(a.sum(axis=0))    # sum() col = element index sama di-sum()
print(a.sum(axis=1))    # sum() row = element di tiap array di-sum()

#     1       2       3     axis1
#     4       5       6     axis1
#   axis0   axis0   axis0

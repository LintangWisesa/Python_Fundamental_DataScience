
import numpy as np

a = np.array([(1,2,3,4), (5,6,7,8), (9,10,11,12)])

print(a[0,2])
print(a[0:,3])      # [0:,3] means all rows, index 3
print(a[0:2,3])     # [0:2,3] from row 0-2 (2 is not included), index 3
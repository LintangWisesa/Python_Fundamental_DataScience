# determinant
# |a| |c|  =  ad - bc
# |b| |d|     

import numpy as np

a = np.array([(1,2),(3,4)])

print(np.linalg.det(a))

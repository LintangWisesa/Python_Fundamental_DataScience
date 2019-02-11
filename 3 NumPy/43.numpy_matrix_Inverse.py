# inverse
# |a c|  =  ( 1 / ad - bc ) |d  -b|
# |b d|                     |-c  a|

import numpy as np

a = np.array([(1,2),(3,4)])

print(np.linalg.inv(a))

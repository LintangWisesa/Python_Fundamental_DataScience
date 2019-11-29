# transpose
# elemen row 1, col 2 => row 2, col 1

# |a b| = |a c e|  
# |c d|   |b d f|  
# |e f|

import numpy as np

a = np.array([(1,2),(3,4)])

print(a.transpose())

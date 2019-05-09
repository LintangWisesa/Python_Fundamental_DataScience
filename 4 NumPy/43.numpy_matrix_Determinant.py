# determinant
# | a c |  =  ad - bc
# | b d |     

import numpy as np

a = np.array([(1,2),(3,4)])

# ada problem di numpy determinant,
# maka harus di-round-kan
print(round(np.linalg.det(a)))


import numpy as np

# =============================
# det matrix 2x2
# | a c |  =  ad - bc
# | b d |     

a = np.array([(1,2),(3,4)])
print(round(np.linalg.det(a)))

# =============================
# det matrix 3x3
# | a b c |   | a b c a b |    
# | d e f | = | d e f d e | = aei + bfg + cdh - ceg - afh - bdi
# | g h i |   | g h i g h |

m = np.array([
    [1, 2, 1],
    [3, 3, 1],
    [2, 1, 2]
])
print(np.linalg.det(m))
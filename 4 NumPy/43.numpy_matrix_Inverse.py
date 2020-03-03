# inverse
# |a c|  =  ( 1 / ad - bc ) |d  -b|
# |b d|                     |-c  a|

import numpy as np

a = np.array([(3,2),(1,4)])
ai = np.linalg.inv(a)

print(ai)
# a . ai = I    matrix identitas perkalian
print(a@ai) 

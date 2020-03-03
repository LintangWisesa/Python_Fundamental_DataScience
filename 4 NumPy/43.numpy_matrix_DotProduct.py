
# perkalian vektor: dot product
# syarat: shape A = shape B

# |1|   
# |2| . | 4 5 6 | = (1x4)+(2x5)+(3x6) = 32 
# |3|   

import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a.dot(b))
print(a@b)

# =========================

X = np.array([[4,6], [9,4]])
I = np.array([[1,0], [0,1]]) # matrix identitas perkalian
print(X@I)
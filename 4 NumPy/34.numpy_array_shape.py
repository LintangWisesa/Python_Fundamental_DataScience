
import numpy as np

a = np.array(['a','b','c'])
b = np.array([(1,2,3), (4,5,6)])
c = np.array([(1,2), (2,3), (3,4)])

print(a.shape)  # output: (3,)      
print(b.shape)  # output: (2, 3)
print(c.shape)  # output: (3, 2)

# (3,)    = dimensi 1 ada 3 elemen
# (2,3)   = dim1 ada 2e, di dim2 ada 3e
# (3,2)   = dim1 ada 3e, di dim2 ada 2e
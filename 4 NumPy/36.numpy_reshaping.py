
import numpy as np

a = np.array([(1,2,3,4), (5,6,7,8)])
print(a)
print(a.size)   # output: 8
print(a.shape)  # output: (2, 4)
# karena size = 8 maka (2,4) bisa direshape jadi:

a = a.reshape(4,2)  # 4 x 2 = 8 = size
print(a)
print(a.shape)  # output: (4, 2)

a = a.reshape(8,)   # 8 = size
print(a)
print(a.shape)  # output: (8,)

a = a.reshape(1,8,1)    # 1 x 8 x 1 = 8 = size
print(a)
print(a.shape)  # output: (8,)
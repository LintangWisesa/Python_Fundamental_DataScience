
import numpy as np

x1 = np.random.rand(10)     # random 10 elements which value between 0-1
x2 = np.random.rand(2,4)    # 2 array with 4 random (0-1) val on each array

print(x1)
print(x2)

y1 = np.random.randint(10, size=10)
y2 = np.random.randint(10, size=(2,5))  # (2,5) = shape, dim1 2 random elements & dim2 5 random elements

print(y1)
print(y2)
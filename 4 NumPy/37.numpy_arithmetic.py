
import numpy as np

a = np.array([(1,2,3,4), (5,6,7,8), (9,10,11,12)])

a = a + 2   # atau a += 2
print(a)

a = a - 2   # atau a -= 2
print(a)

a = a * 2   # atau a *= 2
print(a)

a = a / 2   # atau a //= 2
print(a)

# a[:,1] += 2   # +2 hanya di element ke-1
# print(a)
# output = [(1,4,3,4), (5,8,7,8), (9,12,11,12)]


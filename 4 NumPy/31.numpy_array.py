
# install numpy: $ pip install numpy
import numpy as np

# =======================================
# Why we use NUMPY?

# show only genap [2,4,6,8,12,10] 
# no numpy
x = [2,4,1,6,8,3,12,10]
y = list(filter(lambda i: i%2==0, x))
print(y)
# using numpy
z = np.array(x)
print(z[z % 2 == 0])

# show [2,4,6]
# no numpy
x = [(1, 2), (3, 4), (5, 6)]
y = list(map(lambda i: i[1], x))
print(y)
# using numpy
z = np.array(x)
y = z[:,1]
print(list(y))

# =======================================

z = np.array([1,2,3,4,5,6,7,8,9,10])

print(z)
print(z[0])
print(z[-1])
print(z[3::2])
print(z[z % 2 != 0])

# y = list(filter(lambda i: i%2==0, x))
# print(y)

# z[z % 2 != 0] = -1
# print(z)
out = np.where(z % 2 != 0, -1, z)
print(out)

# =======================================

a = np.array(['a','b','c'])
b = np.array([(1,2,3), (4,5,6)])

print(a)
print(b)

print(a[0])
print(b[1][0])
print(b[1, 0])  # = b[1][0] 

# =================================

a = np.array([(1,2,3,4), (5,6,7,8), (9,10,11,12)])

print(a[0][2])
print(a[0,2])       # a[dim1, dim2]

print(a[0:, 0:])    # a[all dim1, all dim2]
print(a[0:, 3:])
print(a[:, 0:])
print(a[:, 3:]) 

print(a[0:,3])          # [0:,3] means all rows, index 3
print(a[0:2,3])         # [0:2,3] from row 0-2 (2 is not included), index 3
print(a[0:3, [0,2]])    # row 0-2, index 0 & 2
print(a[0:, [0, -1]])   
print(a[:, [3,2,1,0]])
print(a[:, [3,2,1,0,0,1,2,3]])

print(a[0:3:2])         # start : stop : step
print(a[1::2])
print(a[1::2, 1])

#  3 dimensi
a = [
    [[1, 2], [3, 4], [5, 6]],
    [[7, 8], [9, 10], [11, 12]],
    [[13, 14], [15, 16], [17, 18]]
]
a = np.array(a)

print(a[1][2][0])
print(a[1,2,0])
print(a[:, :, 1])
print(a[:, :, [1, 0]])
print(a[:, :, [1, 0, 0, 1]])
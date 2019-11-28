import numpy as np

# intersect
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
x = np.intersect1d(a,b)
print(x)

# From 'a' remove all of 'b'
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
x = np.setdiff1d(a,b)
print(x)

# Get the positions where elements of a and b match
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
x = np.where(a == b)
print(x)

# Get all items between 5 and 10 from a
a = np.arange(15)
# Method 1
index = np.where((a >= 5) & (a <= 10))
print(a[index])
# Method 2:
index = np.where(np.logical_and(a>=5, a<=10))
print(a[index])
# Method 3: (thanks loganzk!)
print(a[(a >= 5) & (a <= 10)])
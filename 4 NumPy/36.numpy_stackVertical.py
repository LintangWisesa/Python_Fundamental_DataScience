import numpy as np

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
print(a)
print(b)

#> array([[0, 1, 2, 3, 4],
#>        [5, 6, 7, 8, 9],
#>        [1, 1, 1, 1, 1],
#>        [1, 1, 1, 1, 1]])

# Method 1:
x = np.concatenate([a, b], axis=0)
print(x)

# Method 2:
y = np.vstack([a, b])
print(y)

# Method 3:
z = np.r_[a, b]
print(z)
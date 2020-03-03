import numpy as np

pi = np.pi
print(pi)   
# similar to math.pi from math package

# ============================

print(np.sin(np.pi / 2))   # sin(90deg)
sudut = np.array([0, 30, 45, 60, 90])
print(np.sin(sudut * (np.pi / 180)))

#       0     30    45    60     90
# sin   0    1/2   v2/2  v3/2    1
# cos   1    v3/2  v2/2   1/2    0
# tan   0    v3/3   1     v3     -

# ============================

x = np.arange(0, 3 * np.pi, 0.1)
# y = np.sin(x)
# y = np.cos(x)
y = np.tan(x)
z = np.cos(0)

print(y)
print(z)

x = 2 * np.pi
y = np.sin(x)
print(x)
print(y)
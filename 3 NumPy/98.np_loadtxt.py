
# np loadtxt hanya bisa get data berupa angka!

import numpy as np

x = np.loadtxt('98.csv', delimiter=',', skiprows=1)
y = np.loadtxt('98.csv', delimiter=',', unpack=True, skiprows=1)

print(x)
print(y)
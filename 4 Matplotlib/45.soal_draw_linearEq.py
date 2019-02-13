# https://idschool.net/smp/cara-menggambar-persamaan-linear/
# pers garis 3x + 2y = 12!

# cari titik potong x dg sumbu y 
# y = 0 maka x = ?
# 3x = 12

# cari titik potong y dg sumbu x 
# x = 0 maka y = ?
# 2y = 12

import numpy as np
import matplotlib.pyplot as plt

a = np.array([[3]])
b = np.array([[2]])
c = np.array([12])

x = np.linalg.solve(a,c) # x ketika y = 0
y = np.linalg.solve(b,c) # y ketika x = 0
print(x)
print(y)

titikA = np.array([x[0], 0])
titikB = np.array([0, y[0]])
print(titikA)
print(titikB)

plt.plot(titikA, titikB)
plt.show()
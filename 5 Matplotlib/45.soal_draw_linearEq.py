import numpy as np
import matplotlib.pyplot as plt
# 3x + 2y = 12

# titik potong 1 dg sumbu-x => y = 0  => 3x = 12
# | 3 | | x | = | 12 |
x1 = np.linalg.solve([[3]], [12])[0]
y1 = 0
print(x1, y1)

# titik potong 2 dg sumbu-y => x = 0  => 2y = 12
# | 2 | | y | = | 12 |
y2 = np.linalg.solve([[2]], [12])[0]
x2 = 0
print(x2, y2)

x = np.array([x1, x2])     # 4,0
y = np.array([y1, y2])     # 0,6

plt.plot(x, y)
plt.grid(True)
plt.show()
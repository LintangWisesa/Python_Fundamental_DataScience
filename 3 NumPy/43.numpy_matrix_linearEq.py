
import numpy as np

# Solve 3x = 9

a = np.array([[3]])
b = np.array([30])

x = np.linalg.solve(a, b)
print(x)

# ====================================

# Solve the system of equations:
# 3 * x0 + x1 = 9 
# x0 + 2 * x1 = 8

a = np.array([[3,1], [1,2]])
b = np.array([9,8])

x = np.linalg.solve(a, b)
print(x)
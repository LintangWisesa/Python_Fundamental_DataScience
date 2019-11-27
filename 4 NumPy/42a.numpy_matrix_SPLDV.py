
import numpy as np

# satu variabel : Solve 3x = 9
# | 3 | | x | = | 9 |

# a = np.array([3]).reshape(1,1)
a = np.array([[3]])
b = np.array([9])

x = np.linalg.solve(a, b)
print(x)

# ====================================

# dua variabel: Solve the system of equations:
# 3x + y = 9 
# x + 2y = 8
# | 3 1 | | x | = | 9 |
# | 1 2 | | y |   | 8 |

a = np.array([[3,1], [1,2]])
b = np.array([9,8])

x = np.linalg.solve(a, b)
print(x)
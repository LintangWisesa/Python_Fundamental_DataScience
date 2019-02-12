import numpy as np

# tiga variabel
# x + y – z = –3
# x + 2y + z = 7
# 2x + y + z = 4

# | 1 1 -1 | | x |   | -3 |
# | 1 2 1 |  | y | = | 7 |
# | 2 1 1 |  | z |   | 4 |

a = np.array([[1,1,-1], [1,2,1], [2,1,1]])
b = np.array([-3,7,4])

hasil = np.linalg.solve(a, b)
print('x = ', hasil[0])
print('y = ', hasil[1])
print('z = ', hasil[2])

import numpy as np

x = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# [
#     [3, 2, 1],
#     [6, 5, 4],
#     [9, 8, 7]
# ]

# cara 1 no numpy
x = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
y = []
for row in x:
    a = row[0]
    row[0] = row[-1]
    row[-1] = a
    y.append(row)
print(y)

# cara 2 no numpy
x = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
y = list(map(lambda i: [i[2], i[1], i[0]], x))
print(y)
        
# cara 3 numpy
x = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
x = np.array(x)
print(x[:,[2,1,0]])

# =================================
# Rubik no numpy & with numpy

#    7 4 1    3 6 9    9 8 7    1 4 7    9 6 3
#    8 5 2    2 5 8    6 5 4    2 5 8    8 5 2
#    9 6 3    1 4 7    3 2 1    3 6 9    7 4 1
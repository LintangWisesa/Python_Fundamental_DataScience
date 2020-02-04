
for i in range(5):
    for j in range(6, 10):
        print(i, '&', j)

###########################

matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in matriks:
    print(row)

for row in matriks:
    for col in row:
        print(col)

######################

x = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j])

######################

list = [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ] 
    
]

for x in list:
    for y in x:
        for z in y:
            print(z)
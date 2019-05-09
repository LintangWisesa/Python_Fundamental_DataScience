import numpy as np

print('Selamat datang di aplikasi SPLDV')
print('Silakan input dengan format ax + by = c')

pers1 = input('Ketik persamaan 1 : ')
# pers2 = input('Ketik persamaan 2 : ')

def ambilPers1():
    x = pers1.split('x')[0]
    if x == '':
        x = 1
    else:
        x = int(x)
    print(x)

    y = pers1.split('y')[0].split('x')
    if x == '':
        y = 1
    else:
        if y.split('+')
        y = int(y)
    print(y)
    
ambilPers1()

# a = np.array([[3, 1], [1, 2]])
# b = np.array([9, 8])
# c = np.linalg.solve(a, b)
# print(c)
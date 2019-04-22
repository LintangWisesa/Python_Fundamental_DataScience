
import numpy as np

a = np.array(['a','b','c'])
b = np.array([(1,2,3), (4,5,6)])

satu = np.array(['andi', 'budi', 'caca'])       # 1 dimensi
dua = np.array([['andi', 'budi', 'caca']])      # 2 dimensi
tiga = np.array([[['andi', 'budi', 'caca']]])   # 3 dimensi
empat = np.array([                              # 4 dimensi
    [
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9] 
        ]
    ]
])

print(satu.ndim)
print(dua.ndim)
print(tiga.ndim)

print(b.ndim)       # dimensi
print(b.size)       # jumlah elemen value
print(b.itemsize)   # size
print(b.dtype)      # data type
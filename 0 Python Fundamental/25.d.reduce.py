angka = [1, 2, 3, 4]
# 1 x 2 x 3 x 4 = 24
hasil = 1
for i in angka:
    hasil *= i
print(hasil)

from functools import reduce
z = reduce(lambda x, y: x * y, angka)
print(z)


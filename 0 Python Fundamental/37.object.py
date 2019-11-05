
class X:
    def __init__(self, nama, gelar):
        self.nama = nama
        self.gelar = gelar

class Y(X):
    def __init__(self, nama, gelar, univ):
        super().__init__(nama, gelar)
        self.kampus = univ

caca = Y('caca', 'S.T.', 'UI')
# print(objY.nama, objY.gelar, objY.kampus)
print(objY.nama)
print(getattr(objY, 'gelar'))

print(hasattr(objY, 'warna'))
print(hasattr(objY, 'usia'))

objZ.usia = 23
setattr(objZ, 'alamat', 'BSD')

print(vars(objZ))
delattr(objZ, 'alamat')
print(vars(objZ))

del Y.kampus
print(objZ.kampus)

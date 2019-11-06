
# create class Y that inherit to X (Y add property)
class X:
    def __init__(self, nama, gelar):
        self.nama = nama
        self.gelar = gelar

# Cara 1
# class Y(X):
#     def __init__(self, nama, gelar, univ):
#         X.__init__(self, nama, gelar)
#         self.kampus = univ

# cara 2
class Y(X):
    def __init__(self, nama, gelar, univ):
        super().__init__(nama, gelar)
        self.kampus = univ

objX = Y('Andi', 'Prof', 'UGM')
# print(vars(objX))

########################################

lass Manusia:
    def __init__(self, nama):
        self.nama = nama

class Pria(Manusia):
    def __init__(self, nama):
        Manusia.__init__(self, nama)
        self.gender = 'Laki-Laki'

objA = Manusia('Andi')
objB = Pria('Andi')
print(vars(objA))
print(vars(objB))
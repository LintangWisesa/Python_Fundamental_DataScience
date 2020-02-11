# multilevel inheritance

class X:
    def __init__(self, nama):
        self.nama = nama

class Y(X):
    def __init__(self, nama, gelar):
        X.__init__(self, nama)
        self.gelar = gelar

class Z(Y):
    def __init__(self, nama, gelar, univ):
        Y.__init__(self, nama, gelar)
        self.univ = univ

objA = Z('Andi', 'Prof', 'UGM')
print(vars(objA))

############################################

class Manusia:
    def __init__(self, nama):
        self.nama = nama

class Pria(Manusia):
    def __init__(self, nama):           # hanya prop nama yg ditentukan obj
        Manusia.__init__(self, nama)
        self.gender = 'Pria'
     
class Bencong(Pria):
    def __init__(self, nama):           # hanya prop nama yg ditentukan obj
        Pria.__init__(self, nama)
        self.feminim = True

Andi = Bencong('Andi')
print(Andi.nama, Andi.gender, Andi.feminim)
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
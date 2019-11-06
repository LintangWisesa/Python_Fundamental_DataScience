
# create class Y that inherit to X (Y punya semua properti X)
class X:
    def __init__(self, nama, gelar):
        self.nama = nama
        self.gelar = gelar

# Cara 1
class Y(X):
    pass

# Cara 2
class Y(X):
    def __init__(self, nama, gelar):
        X.__init__(self, nama, gelar)

# cara 3
class Y(X):
    def __init__(self, nama, gelar):
        super().__init__(self, nama, gelar)

objX = X('Andi', 'Prof')
objY = Y('Budi', 'Dr.')

print(vars(objX))
print(vars(objY))
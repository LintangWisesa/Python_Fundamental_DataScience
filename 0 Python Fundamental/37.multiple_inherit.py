# multiple inheritance

class X:
    def __init__(self, nama):
        self.nama = nama

class Y:
    def __init__(self, gelar):
        self.gelar = gelar

class Z(X, Y):
    def __init__(self, nama, gelar, univ):
        X.__init__(self, nama)
        Y.__init__(self, gelar)
        self.univ = univ

objA = Z('Andi', 'Prof', 'UGM')
print(vars(objA))

##################################

class Karnivora:
    def __init__(self):
        self.daging = True
        self.nama = 'Karnivora'

class Herbivora:
    def __init__(self):
        self.tumbuhan = True
        self.nama = 'Herbivora'

class Omnivora(Karnivora, Herbivora):
    def __init__(self):
        Herbivora.__init__(self)
        Karnivora.__init__(self)
        # Herbivora.__init__(self)  # try this one, check the name
        # Karnivora.__init__(self)
        self.mcD = True
        self.nama = 'Omnivora'      # try this one, check the name

objA = Omnivora()
print(vars(objA))
print(Omnivora.__mro__) # method resolution order
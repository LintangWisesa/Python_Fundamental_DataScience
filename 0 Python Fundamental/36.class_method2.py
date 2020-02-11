# class Siswa with method: hitungLuas() & keliling() with a parameter
class X:
    def luasPersegi(self, sisi):
        return sisi ** 2
    def kelilingPersegi(self, sisi):
        return sisi * 4

obj1 = X()
print(obj1.luasPersegi(2), obj1.kelilingPersegi(2))
print(obj1.luasPersegi(7), obj1.kelilingPersegi(7))
print(obj1.luasPersegi(12), obj1.kelilingPersegi(12))
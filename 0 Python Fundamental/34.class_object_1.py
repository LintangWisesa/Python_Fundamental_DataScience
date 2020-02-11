
# class Siswa with property: nama & usia
class Siswa:
    nama = 'Siswa'
    usia = 15

print(Siswa)
print(type(Siswa))
print(Siswa.nama)
print(Siswa.usia)

# object andi & budi from Siswa class
andi = Siswa()
print(andi.nama)
print(andi.usia)

budi = Siswa()
print(andi.nama)
print(andi.usia)

#############################################

# prop that values are not a primitive var
class X:
    a = [1,2,3,4,5]
    b = {'nama': 'Andi'}

obj = X()
print(obj.a)
print(obj.b)
print(obj.a[0])
print(obj.b['nama'])

# class is a code template for creating objects.
class Siswa:
    status = 'siswa'
    def __init__(self, nama, usia, jurusan):
        self.nama = nama
        self.usia = usia
        self.jurusan = jurusan

andi = Siswa('Andi', 19, 'Teknik Informatika')
budi = Siswa('Budi', 20, 'Elektronika Instrumentasi')

print(andi.status)
print(andi.nama)
print(andi.usia)
print(andi.jurusan)

print(budi.status)
print(budi.nama)
print(budi.usia)
print(budi.jurusan)
class Siswa:
    def __init__(self, nama, usia, jurusan):
        self.nama = nama
        self.usia = usia
        self.jurusan = jurusan

andi = Siswa('Andi', 19, 'Teknik Informatika')
budi = Siswa('Budi', 20, 'Elektronika Instrumentasi')

print(andi.nama)
print(andi.usia)
print(andi.jurusan)

print(budi.nama)
print(budi.usia)
print(budi.jurusan)
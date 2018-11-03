class Soal:
    def __init__(self, soal, jawab):
        self.soal = soal
        self.jawab = jawab

kumpulanSoal = [
    'Apa warna buah apel?\n(a) Merah\n(b) Biru\n(c) Hitam\n\n',
    'Apa warna buah pisang?\n(a) Biru\n(b) Kuning\n(c) Cokelat\n\n',
    'Apa warna buah jeruk?\n(a) Ungu\n(b) Emas\n(c) Orange\n\n'
]

allSoal = [
    Soal(kumpulanSoal[0], 'a'),
    Soal(kumpulanSoal[1], 'b'),
    Soal(kumpulanSoal[2], 'c')
]

def mulaiUjian(allSoal):
    nilai = 0
    for soal in allSoal:
        jawab = input(soal.soal)
        if jawab == soal.jawab:
            nilai += 1
    print('Benar: ' + str(nilai) + '/' + str(len(allSoal)))

mulaiUjian(allSoal)
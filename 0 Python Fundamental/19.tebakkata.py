kataRahasia = 'bakpao'
tebakan = ''
jumlahTebakan = 0
batasTebakan = 5
overTebakan = False

while tebakan != kataRahasia and not(overTebakan):
    if jumlahTebakan < batasTebakan:
        tebakan = input(f'Input ke {jumlahTebakan+1} Masukkan kata tebakan: ')
        jumlahTebakan += 1
    else:
        overTebakan = True

if overTebakan:
    print('Kesempatan menebak habis! Anda kalah!')
else:
    print('Tebakan benar! Anda menang!')
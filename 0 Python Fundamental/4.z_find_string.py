# Cari jumlah Huruf

kalimat = 'Hari ini Andi tidak sekolah.'
cari = 'a'
kalmina = kalimat.upper().replace(cari.upper(), '')
jumlah = len(kalimat) - len(kalmina)
print(jumlah)
print(f'Jumlah huruf \'{cari}\' ada = {jumlah}')

# Cari jumlah Huruf dg .count()
kalimat = 'Hari ini Andi tidak sekolah.'
cari = 'a'
print(cari.lower() in kalimat.lower())
print(kalimat.lower().count(cari.lower()))

################################

# Cari jumlah Kata

kalimat = 'sekolah Hari ini Andi tidak Sekolah.'
cari = 'sekolah'
kalcari = kalimat.upper().replace(cari.upper(), '')
jmlkata = int((len(kalimat) - len(kalcari)) / len(cari))
print(f'Jumlah kata \'{cari}\' ada = {jmlkata}')
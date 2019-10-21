# Cari jumlah Huruf

kalimat = 'Hari ini Andi tidak sekolah.'
cari = 'a'
kalmina = kalimat.upper().replace(cari.upper(), '')
jumlah = len(kalimat) - len(kalmina)
print(jumlah)

################################

# Cari jumlah Kata

kalimat = 'sekolah Hari ini Andi tidak Sekolah.'
cari = 'sekolah'
kalcari = kalimat.upper().replace(cari.upper(), '')
print(int((len(kalimat) - len(kalcari)) / len(cari)))

jomblo = True
bekerja = True

if bekerja and jomblo:
    print('Anda sudah kerja tapi masih jomblo!')
elif bekerja and not(jomblo):
    print('Anda sudah kerja dan sudah taken!')
elif not(bekerja) and jomblo:
    print('Anda belum kerja tapi sudah taken!')
else:
    print('Cari kerja biar ga jomblo!')
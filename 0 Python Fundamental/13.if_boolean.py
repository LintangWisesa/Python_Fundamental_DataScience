
if x and y:
    print('Anda x & y')
elif x and not y:
    print('Anda x')
elif not x and y:
    print('Anda y')
else:
    print('Anda siapa?')

# =============================================== 

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

# ===============================================

nilai = 79

if nilai >= 80:
    print('Nilai Anda =', nilai, '=> Anda lulus!')
# elif 80 > nilai >= 60:
elif nilai < 80 and nilai >= 60:
    print('Nilai Anda =', nilai, '=> Anda remidial')
else:
    print('Nilai Anda =', nilai, '=> Anda tidak lulus')
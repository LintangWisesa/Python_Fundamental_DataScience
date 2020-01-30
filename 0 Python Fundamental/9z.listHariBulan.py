hari = [
    'Senin', 'Selasa', 'Rabu', 'Kamis', 
    'Jumat', 'Sabtu', 'Minggu'
]

'''
Sekarang hari Rabu, hari apakah 100 hari lagi?
Sekarang hari Rabu, hari apakah 100 hari yang lalu?
'''

now = input("Hari ini hari apa? ").capitalize()
hariLagi = int(input("Mau berapa hari lagi? "))
sisaHari = int(hariLagi % len(hari))
hariYgDicari = hari[(hari.index(now) + sisaHari) % len(hari)]
print(f'{hariLagi} hari lagi = hari {hariYgDicari}')


'''
Sekarang bln Januari, bln apakah 100 bln lagi?
Sekarang bln Januari, bln apakah 100 bln yang lalu?
'''

bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei',
    'Juni', 'Juli', 'Agustus', 'September', 'Oktober',
    'November', 'Desember'
]

now = input("Bulan ini bulan apa? ").capitalize()
blnLagi = int(input("Mau berapa bulan lagi? "))
sisaBln = int(blnLagi % len(bulan))
blnYgDicari = bulan[(bulan.index(now) + sisaBln) % len(bulan)]
print(f'{blnLagi} bulan lagi = bulan {blnYgDicari}')

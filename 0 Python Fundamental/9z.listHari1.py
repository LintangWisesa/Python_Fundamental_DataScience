# list
hari = [
    'senin', 'selasa', 'rabu', 'kamis', 
    'jumat', 'sabtu', 'minggu'
]
'''
Sekarang hari 'Rabu', hari apakah 100 hari lagi?
Sekarang hari 'Rabu', hari apakah 100 hari yg lalu?
'''
now = 'selasa'; brpHari = -1;
iNow = hari.index(now)
sisaHari = brpHari % len(hari)
hariYgDicari = hari[(iNow + sisaHari) % 7]
print(hariYgDicari)

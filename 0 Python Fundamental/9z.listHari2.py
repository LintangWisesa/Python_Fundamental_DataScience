
hari = [
    'senin', 'selasa', 'rabu', 'kamis', 
    'jumat', 'sabtu', 'minggu'
]
'''
Sekarang hari 'Rabu', hari apakah 100 hari lagi?
Sekarang hari 'Rabu', hari apakah 100 hari yang lalu?
'''
now = 'senin'; 
brpHari = -2;    # positif untuk hari ke depan, negatif untuk hari yg lalu!

indexNow = hari.index(now);
sisaHari = abs(brpHari) % len(hari)
hariYangDicari = hari[(indexNow + int(sisaHari * (brpHari/abs(brpHari)))) % 7]
print(sisaHari)
print(hariYangDicari)

# dictionary = { key : value }

namaBulan = {
    '01': 'Januari',
    '02': 'Februari',
    '03': 'Maret',
    '04': 'April',
    '05': 'Mei',
    '06': 'Juni',
    '07': 'Juli',
    '08': 'Agustus',
    '09': 'September',
    '10': 'Oktober',
    '11': 'November',
    '12': 'Desember'
}

namaHari = {
    1: 'Senin',
    2: 'Selasa',
    3: 'Rabu',
    4: 'Kamis',
    5: 'Jum\'at',
    6: 'Sabtu',
    7: 'Minggu'
}

print(namaBulan['01'])
print(namaBulan.get('11'))
print(namaBulan.get('13'))
print(namaBulan.get('14', 'Maaf, data tidak ditemukan'))

print(namaHari.get(1))
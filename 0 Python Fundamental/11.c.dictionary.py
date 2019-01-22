
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

# change value
namaBulan[2] = 'February'
print(namaBulan[2])

# add item
namaBulan[13] = 'Xpander'
print(namaBulan)

# update
namaBulan.update({13: 'Xpanda'})
print(namaBulan)

# remove an item
namaBulan.pop(13)
print(namaBulan)

del namaBulan[2]
print(namaBulan)

# mencari key dari value-nya
print(list(namaHari.keys())[list(namaHari.values()).index('Senin')])
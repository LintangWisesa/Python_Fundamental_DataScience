
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

namaBulan[2] = 'February'   # change value
namaBulan[13] = 'Xpander'   # add item
print(namaBulan)

# update: change value / add item 
namaBulan.update({2: 'Xpander'})
namaBulan.update({13: 'Pajero', 14: 'Innova'})
print(namaBulan)

# remove an item
namaBulan.pop(13)
print(namaBulan)

del namaBulan[2]
print(namaBulan)

# melihat daftar key
print(namaHari.keys())
print(list(namaHari.keys()))
print(list(namaHari))       # simplest ways

# melihat daftar value
print(namaHari.values())
print(list(namaHari.values()))

# melihat key & value as tuple
print(namaHari.items())
print(list(namaHari.items()))

# mencari key dari value-nya
print(list(namaHari.keys())[list(namaHari.values()).index('Senin')])

# ====================================
# zip list to dict

# [(1, 'Andi'), (2, 'Budi'), (3, 'Caca')] => {1: 'Andi', 2: 'Budi', 3: 'Caca'}
a = [1,2,3]
b = ['Andi', 'Budi', 'Caca']

c = zip(a, b)
# c = list(zip(a, b))
print(c)

d = dict(c)
print(d)

# ===========================================
# change key name

x = {'Senin': 'Monday', 'Selasa': 'Tuesday'}
keys = list(x.keys())
vals = list(x.values())
# print(keys)
keys[keys.index('Senin')] = 1
print(keys)

d = dict(zip(keys, vals))
print(d)
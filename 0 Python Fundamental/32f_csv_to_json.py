# tanpa DictReader!

import csv
import json

with open('data1.csv') as dataku:
    output = csv.reader(dataku)
    hasil = []
    hasil2 = []
    for x in output:
        hasil2.append(x)
    for y in range(1, len(hasil2)-1):
        data = {
            'no': hasil2[y][0],
            'nama': hasil2[y][1],
            'kota': hasil2[y][2]
        }
        hasil.append(data)

print(hasil)

# # # # # # # # # # # # # # # # # #

hasilJson = json.dumps(hasil)
file = open('csv.json', 'w')

file.write(hasilJson)
file.close()
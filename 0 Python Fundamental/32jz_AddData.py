# add data on csv & json from user input!

# ================================
# read csv
import csv
dataCsv = []

with open('32l.csv', 'r') as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        # print(dict(row))
        dataCsv.append(dict(row))

# print(dataCsv)

# ================================
# read json
import json

with open('32l.json', 'r') as f:
    dataJson = json.load(f)

# print(dataJson)

# ================================
# user input

nama = input('Ketik nama : ')
usia = input('Ketik usia : ')
kota = input('Ketik kota : ')
newData = {
    'nama': nama,
    'usia': usia,
    'kota': kota
}
dataCsv.append(newData)
dataJson.append(newData)

# ================================
# import to csv

with open('32l.csv', 'w', newline = '') as fileku:
    # kolom = ['nama', 'usia', 'kota']
    kolom = list(dataCsv[0].keys())
    tulis = csv.DictWriter(fileku, fieldnames = kolom)
    tulis.writeheader()
    tulis.writerows(dataCsv)

# ================================
# import to json

with open('32l.json', 'w') as f:
    json.dump(dataJson, f)
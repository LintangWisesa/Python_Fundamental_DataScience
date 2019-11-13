import csv

data = []
with open('32z.csv', 'r') as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        data.append(dict(row))
# print(data)

kolom = list(data[0].keys())
out = []
for i in data:
    out.append(list(i.values()))
print(kolom)
print(out)

# ======================================

import xlsxwriter

workbook = xlsxwriter.Workbook('32z_fromXLSX.xlsx')     # file name
worksheet = workbook.add_worksheet('Data')              # sheet name

# write kolom
for i in kolom:
    worksheet.write(0, kolom.index(i), i)

# write data
row = 1
for no, nama, kota in out:
    worksheet.write(row, 0, no)     # row, col, data
    worksheet.write(row, 1, nama)
    worksheet.write(row, 2, kota)
    row += 1

workbook.close()

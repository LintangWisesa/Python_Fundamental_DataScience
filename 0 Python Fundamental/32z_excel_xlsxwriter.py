import xlsxwriter
# pip install xlsxwriter

workbook = xlsxwriter.Workbook('32z2.xlsx')     # file name
worksheet = workbook.add_worksheet('Data')      # sheet name

data = [
    [1, 'Andi', 'Jakarta'],
    [2, 'Budi', 'Bandung'],
    [3, 'Caca', 'Jakarta'],
]

# Iterate over the data and write it out row by row.
row = 0
for no, nama, kota in data:
    worksheet.write(row, 0, no)     # row, col, data
    worksheet.write(row, 1, nama)
    worksheet.write(row, 2, kota)
    row += 1

workbook.close()

import csv

listku = [
    {'no': 1, 'nama': 'Andi'},
    {'no': 2, 'nama': 'Budi'},
    {'no': 3, 'nama': 'Caca'},
    {'no': 4, 'nama': 'Deni'},
    {'no': 5, 'nama': 'Euis'},
]

with open('staff.csv', 'w', newline = '') as fileku:
    kolom = ['no', 'nama']
    tulis = csv.DictWriter(fileku, fieldnames = kolom)
    tulis.writeheader()
    tulis.writerows(listku)
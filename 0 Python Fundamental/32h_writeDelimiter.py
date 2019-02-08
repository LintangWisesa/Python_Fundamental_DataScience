
import csv

listku = [
    ['no', 'produk', 'harga'],
    [1, 'Batik', 250000],
    [2, 'Celana', 300000],
    [3, 'Drone', 10000000],
    [4, 'Kamera', 2000000],
    [5, 'Balon Udara', 25000000]
]

with open('gudang.csv', 'w', newline = '') as fileku:
    tulis = csv.writer(fileku, delimiter = ':')
    tulis.writerows(listku)
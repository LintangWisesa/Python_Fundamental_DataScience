# pivot table: aggregate dataframe, jika ada data kembar
# kalau pivot df, tdk boleh ada data kembar!

import pandas as pd 

data = [
    {'tgl':'2019-02-21', 'kota': 'Jakarta', 'suhu': 34, 'angin': 55},
    {'tgl':'2019-02-21', 'kota': 'Jakarta', 'suhu': 31, 'angin': 35},
    {'tgl':'2019-02-21', 'kota': 'Jakarta', 'suhu': 29, 'angin': 25},
    {'tgl':'2019-02-21', 'kota': 'Bandung', 'suhu': 18, 'angin': 85},
    {'tgl':'2019-02-21', 'kota': 'Bandung', 'suhu': 22, 'angin': 75},
    {'tgl':'2019-02-21', 'kota': 'Bandung', 'suhu': 20, 'angin': 85},
]

df = pd.DataFrame(data)

print(df.pivot_table(index = 'kota', columns = 'tgl'))
print(df.pivot_table(index = 'kota', columns = 'tgl', aggfunc='sum'))
print(df.pivot_table(index = 'kota', columns = 'tgl', aggfunc='sum', margins=True))

# aggregate function: mean, sum, count, diff, dst.
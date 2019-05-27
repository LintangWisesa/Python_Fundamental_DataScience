# pivot dataframe

import pandas as pd 

data = [
    {'tgl':'2019-02-21', 'kota': 'Jakarta', 'suhu': 34, 'angin': 55},
    {'tgl':'2019-02-22', 'kota': 'Jakarta', 'suhu': 31, 'angin': 35},
    {'tgl':'2019-02-23', 'kota': 'Jakarta', 'suhu': 29, 'angin': 25},
    {'tgl':'2019-02-21', 'kota': 'Bandung', 'suhu': 18, 'angin': 85},
    {'tgl':'2019-02-22', 'kota': 'Bandung', 'suhu': 22, 'angin': 75},
    {'tgl':'2019-02-23', 'kota': 'Bandung', 'suhu': 20, 'angin': 85},
]

df = pd.DataFrame(data)
print(df)

print(df.pivot(index = 'tgl', columns = 'kota'))
print(df.pivot(index = 'tgl', columns = 'kota')['suhu'])
print(df.pivot(index = 'tgl', columns = 'kota')['angin'])

# ===========================
# show hanya tanggal & angin
print(df.pivot(index = 'tgl', columns = 'kota').loc['03-02-2019', 'angin'])
# concat 2 dataframe yg sama dimensi & key propsnya!

import pandas as pd 
import matplotlib.pyplot as plt

jawa = [
    {'kota': 'Jakarta', 'suhu': 34, 'angin': 55},
    {'kota': 'Bandung', 'suhu': 18, 'angin': 85},
    {'kota': 'Surabaya', 'suhu': 34, 'angin': 65},
]
jawa = pd.DataFrame(jawa)

bali = [
    {'kota': 'Denpasar', 'suhu': 24, 'angin': 55},
    {'kota': 'Kuta', 'suhu': 20, 'angin': 75},
    {'kota': 'Ubud', 'suhu': 22, 'angin': 65},
]
bali = pd.DataFrame(bali)

# df = pd.concat([jawa, bali], sort=False)
# print(df)
# print(df)
# print(df.loc[1])  # index 1 nya ada 2!!!

# urutkan indexnya
# df = pd.concat([jawa, bali], ignore_index = True, sort=False)

# buat kategori key (ignore_index harus dihapus!)
df = pd.concat([jawa, bali], keys=['jawa','bali'], sort=False)
print(df)
# print(df.loc['jawa'])
# print(df.loc['bali'])
# print(df.loc['jawa', 0])
# print(df.loc['bali', 1])
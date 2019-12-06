# multi column index

import pandas as pd
import numpy as np

# ===================================
# multi index col

df = pd.DataFrame({
    'class' : ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'],
    'number' : [1,2,3,4,5,1,2,3,4,5],
    'math' : [90, 20, 50, 30, 57, 67, 89, 79, 45, 23],
    'english' : [40, 21, 68, 89, 90, 87, 89, 54, 21, 23]
})

# df1 = df.set_index(['number','class']).unstack().swaplevel(0,1,1).sort_index(1)
df1 = df.set_index(['number','class']).unstack().swaplevel(0,1,1).sort_index(1)
print(df1)
print(df1['A'])
print(df1['B'])
print(df1)

# ===================================
# multi index row

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

# buat kategori key (ignore_index harus dihapus!)
df = pd.concat([jawa, bali], keys=['jawa','bali'], sort=False)
print(df)
# print(df.loc['jawa'])
# print(df.loc['bali'])
# print(df.loc['jawa', 0])
# print(df.loc['bali', 1])
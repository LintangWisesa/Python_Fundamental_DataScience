import pandas as pd 
df = pd.read_csv('4_datarokok.csv')

# menjadikan elemen ke-3 (baris ke 2 di CSV) sbg judul kolom
# df = pd.read_csv('4_datarokok.csv', header=3)

# untuk CSV yg baris pertamanya jd header col & tdk ada nama kolom, bisa generate dg:
# df = pd.read_csv('4_datarokok.csv', header=None, names=['kolom1', 'kolom2', 'kolom3'])

# skip 2 baris pertama
# df = pd.read_csv('4_datarokok.csv', skiprows=2)

print(df)
# print(df.shape)
# print(df.describe())

# ======================

# print(df.head())
# print(df.head(2))
# print(df.tail())
# print(df.tail(3))
# print(df[2:5])

# print(df.columns)
# print(df.Provinsi)
# print(df['Provinsi'])
# print(df['2015'])
# print(df[['Provinsi', '2015']])
# print(type(df['2015']))


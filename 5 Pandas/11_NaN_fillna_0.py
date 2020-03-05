
import pandas as pd 

df = pd.read_csv('10_data_NaN.csv', na_values=['-', 'n.a', 'not available'])

# data NaN akan mjd 0
# df2 = df.fillna(0)
# print(df2)

# data NaN di tiap kolom/series dpt ditampilkan dlm bentuk beragam
# df3 = df.fillna({
#     '2015': 0,
#     '2016': 0,
#     'Provinsi': 'Lokasi X',
# })
# print(df3)

# data Nan di df diisi dg metod yg berbeda2
df['2015'] = df['2015'].fillna(method='bfill')
df['Provinsi'] = df['Provinsi'].fillna('Anonim')
df = df.fillna(method='ffill', axis=1)
print(df)
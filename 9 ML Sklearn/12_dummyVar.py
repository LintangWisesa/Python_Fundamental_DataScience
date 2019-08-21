# how should we handle text data in numeric model?

# categrical variable: nominal & ordinal
# nominal: tdk dpt diwakilkn dg angka => nama kota, warna, gender
# ordinal: dpt diwakilkn dg angka sbg urutan => kepuasan, degree, level

# one hot encoding: membuat 1 dummy var kolom dg val = 0 atau 1
# ========================================================

import pandas as pd
import numpy as np

data = [
    {'luas':2600, 'harga':550000, 'kota':'Bekasi'},
    {'luas':3000, 'harga':565000, 'kota':'Bekasi'},
    {'luas':3200, 'harga':610000, 'kota':'Bekasi'},
    {'luas':3600, 'harga':680000, 'kota':'Bekasi'},
    {'luas':4000, 'harga':725000, 'kota':'Bekasi'},
    {'luas':2600, 'harga':585000, 'kota':'Depok'},
    {'luas':2800, 'harga':615000, 'kota':'Depok'},
    {'luas':3300, 'harga':650000, 'kota':'Depok'},
    {'luas':3600, 'harga':710000, 'kota':'Depok'},
    {'luas':2600, 'harga':575000, 'kota':'Bogor'},
    {'luas':2900, 'harga':600000, 'kota':'Bogor'},
    {'luas':3100, 'harga':620000, 'kota':'Bogor'},
    {'luas':3600, 'harga':695000, 'kota':'Bogor'}
]

df = pd.DataFrame(data)
# print(df)

# ==========================================


# show dummy variables
dfDummies = pd.get_dummies(df['kota'])
# print(dfDummies)

# ==========================================

# join df & dfDummies lalu drop kolom kota:
dfFull = pd.concat([df, dfDummies], axis='columns')
dfFull = dfFull.drop(['kota'], axis='columns')
# print(dfFull)

# ==========================================

from sklearn.linear_model import LinearRegression
model = LinearRegression()

x = dfFull.drop(['harga'], axis='columns')
# print(x)
y = dfFull['harga']
# print(y)

# =================================================

# training model
model.fit(x,y)

# model.predict([[luas, bekasi, bogor, depok]])
# prediksi harga tanah utk luas 2800 di Bekasi
print(model.predict([[2800, 1, 0, 0]]))

# prediksi harga tanah utk luas 2800 di Bogor
print(model.predict([[2800, 0, 1, 0]]))

# prediksi harga tanah utk luas 2800 di Depok
print(model.predict([[2800, 0, 0, 1]]))

# menilai akurasi model:
print(model.score(x,y))
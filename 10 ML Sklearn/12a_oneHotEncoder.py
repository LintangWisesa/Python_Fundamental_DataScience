# one hot encoding = membuat 1 dummy var kolom dg val = 0 atau 1

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

# ============================================

# one hot encoding dg label encoder
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
dfle = df

dfle['kota'] = le.fit_transform(dfle['kota'])
print(dfle)
print(le.classes_)
print(le.transform(['Bekasi', 'Bogor', 'Depok', 'Bekasi', 'Bogor', 'Depok']))

x = dfle[['kota', 'luas']].values
print(x)
y = dfle['harga']
print(y)

# ==========================================

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories='auto'), [0])],
    remainder='passthrough'
)

x = np.array(ct.fit_transform(x), dtype=np.int64)

print(x)
# [[   1    0    0 2600]
#  [   1    0    0 3000]
#  [   1    0    0 3200]
#  [   1    0    0 3600]
#  [   1    0    0 4000]
#  [   0    0    1 2600]
#  [   0    0    1 2800]
#  [   0    0    1 3300]
#  [   0    0    1 3600]
#  [   0    1    0 2600]
#  [   0    1    0 2900]
#  [   0    1    0 3100]
#  [   0    1    0 3600]]
# bekasi, bogor, depok, harga

# ==========================================

from sklearn.linear_model import LinearRegression
model = LinearRegression()

model.fit(x,y)
print(model.predict([[1, 0, 0, 2800]])) # bekasi
print(model.predict([[0, 1, 0, 2800]])) # bogor
print(model.predict([[0, 0, 1, 2800]])) # depok

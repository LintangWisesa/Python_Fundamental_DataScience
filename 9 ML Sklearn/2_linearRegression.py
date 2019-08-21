# predict price, & create csv

from sklearn import linear_model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'luas': [2600, 3000, 3200, 3600, 4000],
    'harga': [550000, 565000, 610000, 680000, 725000]
}
df = pd.DataFrame(data)
# print(df)

reg = linear_model.LinearRegression()
reg.fit(df[['luas']], df['harga'])

# =============================
# prediksi harga dari data baru

yangAkanDiprediksi = {
    'luas': [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]
}
newData = pd.DataFrame(yangAkanDiprediksi)
prediksiHarga = reg.predict(newData)
print(prediksiHarga)

# ==============================
# output berupa csv:

newData['harga'] = prediksiHarga
print(newData)

newData.to_csv('z2_linearRegression.csv', index=False)

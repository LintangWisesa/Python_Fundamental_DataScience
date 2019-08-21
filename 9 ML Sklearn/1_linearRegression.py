# pip install sklearn

from sklearn import linear_model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# y = mx + b
# harga = m.luas + b

data = {
    'luas': [2600, 3000, 3200, 3600, 4000],
    'harga': [550000, 565000, 610000, 680000, 725000]
}
df = pd.DataFrame(data)
print(df)

# ==================================

# plot dataframe
plt.scatter(df['luas'], df['harga'], color='r', marker='*', s=100)
plt.xlabel('Luas Tanah (m2)')
plt.ylabel('Harga Tanah (Rp)')
# plt.show()

# ==================================

reg = linear_model.LinearRegression()
# train datasets: reg.fit(dataDependent, dataIndependent)
reg.fit(df[['luas']], df['harga'])

# prediksi harga utk luas 3300
print(reg.predict([[3300]]))

# y = mx + b
# menampilkan m/kemiringan/gradien garis = reg.coef_
print(reg.coef_)

# menampilkan b/konstanta = reg.intercept_
print(reg.intercept_)
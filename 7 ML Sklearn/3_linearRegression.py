# plot grafik 'garis terbaik'

from sklearn import linear_model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'luas': [2600, 3000, 3200, 3600, 4000],
    'harga': [550000, 565000, 610000, 680000, 725000]
}
df = pd.DataFrame(data)
print(df)

# ==================================

reg = linear_model.LinearRegression()
reg.fit(df[['luas']], df['harga'])

# prediksi harga utk luas 3300
print(reg.predict([[3300]]))

# y = mx + b
# menampilkan m/kemiringan/gradien garis:
print(reg.coef_)

# menampilkan b/konstanta
print(reg.intercept_)

# ====================================
# plot dataframe & garis terbaik 'best fit line'

plt.plot(df['luas'], reg.predict(df[['luas']]), color='g')
plt.scatter(df['luas'], df['harga'], color='r', marker='*', s=100)

plt.xlabel('Luas Tanah (m2)', fontsize=10)
plt.ylabel('Harga Tanah (Rp)', fontsize=10)
plt.show()
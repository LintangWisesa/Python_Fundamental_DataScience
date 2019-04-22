# pip install sklearn

# supervised learning
# memprediksi harga tanah berdasarkan data luas tanah & harganya

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

hargaRumah = [245, 312, 279, 308, 199, 219, 405, 324, 319, 255]
luasTanah = [140, 160, 170, 187, 110, 155, 235, 245, 145, 170]
print(luasTanah)

luas2 = np.array(luasTanah).reshape((-1,1))
print(luas2)

regr = linear_model.LinearRegression()
regr.fit(luas2, hargaRumah)
print('Koefisien:', regr.coef_)
print('Intercept:', regr.intercept_)

# didapatkan nilai koefisien & intercept
# jika ada data luas tanah baru, bisa dihitung:
# harga_new = (luas_new * koefisien) + intercept

luas_new = 170
harga_new = (luas_new * regr.coef_) + regr.intercept_
print(harga_new)
print(regr.predict([[luas_new]]))

# plotting garis prediksi

def graph(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x,y,'r--')

graph('regr.coef_*x + regr.intercept_', range(100, 300))
plt.scatter(luasTanah, hargaRumah, color='g', marker='o', s=50)
plt.ylabel('Harga rumah')
plt.xlabel('Luas tanah')
plt.show()
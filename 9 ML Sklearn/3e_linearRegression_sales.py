# case: https://www.displayr.com/what-is-linear-regression/
# plot grafik 'garis terbaik'

from sklearn import linear_model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'sales': [651, 762, 856, 1063, 1190, 1298, 1421, 1440, 1518],
    'advertising': [23, 26, 30, 34, 43, 48, 52, 57, 58]
}
df = pd.DataFrame(data)
print(df)

# ==================================

reg = linear_model.LinearRegression()
reg.fit(df[['advertising']], df['sales'])

# prediksi harga utk luas 3300
# print(reg.predict([[3300]]))

# y = mx + b
# menampilkan m/kemiringan/gradien garis:
print(reg.coef_)

# menampilkan b/konstanta
print(reg.intercept_)

# ====================================
# plot dataframe & garis terbaik 'best fit line'

plt.plot(df['advertising'], reg.predict(df[['advertising']]), color='g')
plt.scatter(df['advertising'], df['sales'], color='r', marker='*', s=100)

plt.xlabel('Advertising (M Euro)', fontsize=10)
plt.ylabel('Sales (M Euro)', fontsize=10)
plt.show()
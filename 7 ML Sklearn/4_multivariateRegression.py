# multivariate regression
# a.k.a linear regression with multiple variables 
# y = m1x1 + m2x2 + m3x3 + b
# harga = (m1.luas) + (m2.kamar) + (m3.usia) + b

from sklearn import linear_model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'luas': [2600, 3000, 3200, 3600, 4000],
    'kamar': [3, 4, 1, 3, 5],
    'usia': [20, 15, 18, 30, 8],
    'harga': [550000, 565000, 610000, 595000, 760000]
}
df = pd.DataFrame(data)
print(df)

# =====================================

reg = linear_model.LinearRegression()
reg.fit(df[['luas', 'kamar', 'usia']], df['harga'])

# nilai m1, m2, m3
print(reg.coef_)

# nilai b
print(reg.intercept_)

# =====================================

# prediksi utk luas:3000, kamar:2 & usia:20
x = reg.predict([[3000, 2, 20]])
print(x)
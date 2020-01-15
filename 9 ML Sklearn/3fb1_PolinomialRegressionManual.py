# https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-ridge-lasso-regression-python/

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# data dummy 1: sine curve (between 60° and 300°) and added some random noise
x = np.array([i*np.pi/180 for i in range(60,300,4)])
# print(x)
np.random.seed(10)
y = np.sin(x) + np.random.normal(0,0.15,len(x))
# print(y)

# data dummy 2: sinus curve
# rng = np.random.RandomState(1)
# x = 10 * rng.rand(50)
# x.sort()
# y = np.sin(x) + 0.1 * rng.randn(50)

df = pd.DataFrame({
    'x1': x, 'y': y
})
for i in range(2,16):
    df[f'x{i}'] = df['x1'] ** i
# print(df.head())

# ==============================================
# linear regression
from sklearn.linear_model import LinearRegression

for i in range(1,16):
    if i == 1:
        model = LinearRegression()
        model.fit(df[[f'x{i}']], df['y'])
        yp1 = model.predict(df[[f'x{i}']])
        df['yp1'] = yp1
    if i >= 2:
        model = LinearRegression()
        xVal = []
        xVal.extend(['x%d'%i for i in range(1, i+1)])
        # print(xVal)
        # print(df[xVal])
        model.fit(df[xVal], df['y'])
        y_pred = model.predict(df[xVal])
        df[f'yp{i}'] = y_pred
    
# print(df.head())
print(df.columns)

# ==============================================
# plotting regression

plt.figure(figsize=(15,10))
for i in range(1, 16):
    plt.subplot(3,5,i)
    plt.plot(df['x1'], df['y'], 'y.')
    plt.plot(df['x1'], df[f'yp{i}'], 'r-')
    plt.title(f'Pangkat $ x = {i} $')
plt.show()

# ==============================================
# RMSE terbaik (terkecil)

from sklearn.metrics import mean_squared_error

for i in range(1, 16):
    print(f'RMSE yp{i} =', np.sqrt(mean_squared_error(df['y'], df[f'yp{i}'])))
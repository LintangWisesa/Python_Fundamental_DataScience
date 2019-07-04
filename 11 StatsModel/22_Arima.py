# ARIMA: Autoregressive integrated moving average
# time series analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(
    '22_Arima.xlsx',
    index_col=False,
    parse_dates=['Month']
)
# date must to be an index
df = df.set_index('Month')
# print(df)

# ===============================================================
# plotting 1 data asli, hasilnya ternyata data tidak stationary
# ===============================================================

# plt.plot(df.index, df['Sales']) # atau:
# df.plot()
# plt.show()

# ===============================================================
# converting df to data stationary
# stationary: mean, variance & covariance is constant over periods
# ===============================================================

df_diff = df.diff(periods=1)    # integrated of order 1, denoted by d (for diff)
df_diff = df_diff[1:]           # drop data row 0 (NaN)

print(df.head())
print(df_diff.head())

# ===============================================================
# plotting 2 cek data stationary
# ===============================================================

# plt.plot(df_diff.index, df_diff['Sales']) # atau:
# # df_diff.plot()
# plt.show()

# ===============================================================
# autoregressive model (AR model)
# ===============================================================

# pip install statsmodels
from statsmodels.tsa.ar_model import AR
from sklearn.metrics import mean_squared_error

# split datasets: train & test
X = df.values
print(X.size)       # total data = 36
train = X[0:27]     # data untuk train = 0-26 (90%)
test = X[26:]       # data untuk test = 28-36 (10%)

# AR model
model_ar = AR(train)
model_ar_fit = model_ar.fit()
predictions = model_ar_fit.predict(start=27, end=36)
print(predictions)

# ===============================================================
# plotting 3 data real vs prediksi AR
# ===============================================================

# plt.plot(test)
# plt.plot(predictions)
# plt.show()

# ===============================================================
# autoregressive integrated moving average model (ARIMA model)
# ===============================================================

from statsmodels.tsa.arima_model import ARIMA

# ARIMA model needs 3 params: p, d, q
# p = periods taken for AR model
# d = integrated order, how many times differencing done
# q = periods in moving average model
model_arima = ARIMA(train, order=(4,1,1))
model_arima_fit = model_arima.fit()
predictions = model_arima_fit.forecast(steps=10)[0]

# ===============================================================
# plotting 4 data real vs prediksi ARIMA
# ===============================================================

plt.plot(test)
plt.plot(predictions)
plt.show()

# ===============================================================
# finding best p, d, q value
# ===============================================================

import itertools
p = d = q = range(0, 5)
pdq = list(itertools.product(p,d,q))
# print(pdq)

import warnings
warnings.filterwarnings('ignore')

for i in pdq:
    try:
        model_arima = ARIMA(train, order=i)
        model_arima_fit = model_arima.fit()
        print(model_arima_fit.aic)              # cari aic paling minimum!
    except:
        continue
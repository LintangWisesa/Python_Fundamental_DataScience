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
# plotting
# ===============================================================

# plt.plot(df.index, df['Sales'])
df.plot()
# plt.show()

# ===============================================================
# converting df to stationary
# stationary: mean, variance & covariance is constant over periods
# ===============================================================

df_diff = df.diff(periods=1)
df_diff = df_diff[1:]
print(df_diff)
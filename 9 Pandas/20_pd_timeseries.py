# 1. baca file as dataframe
# 2. ubah kolom tanggal jadi timestamp, bukan string!
# 3. jadikan kolom tanggal sbg index

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(
    '20_dataTelkom.csv', 
    index_col=False,
    parse_dates=['Tanggal']
)
df = df.set_index('Tanggal')

# sort data by index tanggal
df = df.sort_index()

# print(df.head())
# print(type(df['Tanggal'][0]))

# print(df['2019'])
# print(df['2019-03'])
# print(df['2019-02-27':'2019-02-28'])
# print(df['27-02-2019':'28-02-2019'])
# print(df.loc['27-02-2019'])

# print(df['2019-03']['Close'].mean())
# print(df['2019-03']['Close'].max())
# print(df['2019-03']['Close'].min())
# print(df[df['Close'] == df['2019-03']['Close'].max()])

# plotting
plt.plot(
    df.index, df['Close'], 'g-',
    df.index, df['Open'], 'r-'
)
plt.xlabel('Tanggal')
plt.ylabel('Rp')
plt.xticks(rotation=65)
plt.grid(True)
plt.show()
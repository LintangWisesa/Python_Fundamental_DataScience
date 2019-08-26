# historical price & data / data historis saham 
# https://www.nasdaq.com/symbol/aapl/historical
# https://finance.yahoo.com/quote/AALI.JK/history?ltr=1
# https://www.seputarforex.com/saham/data_historis/

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
# print(df['2016-03':'2017-03'])
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
    # df.index, df['Open'], 'r-'
    # df['2017'].index, df['2017']['Open'], 'r-'
)

# set axis
import matplotlib.dates as mdates

ax = plt.gca()  # get current axis
ax.xaxis.set_major_locator(mdates.DayLocator(   # WeekdayLocator, MonthLocator, YearLocator
    interval=5
))
ax.xaxis.set_major_formatter(mdates.DateFormatter(
    '%d-%m-%Y'  # '%d-%m-%y'  '%D'  '%b %y'
))

plt.xlabel('Tanggal')
plt.ylabel('Rp')
plt.xticks(rotation=65)
plt.grid(True)
plt.show()
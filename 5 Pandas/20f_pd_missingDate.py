
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(
    '20_dataTelkom.csv', 
    index_col=False,
    parse_dates=['Tanggal']
)
df = df.set_index('Tanggal')
df = df.sort_index()
# print(df)
# ada tanggal yg missing krn holiday/weekend

df = df.resample('D').sum()
df = df.replace(0, np.NaN)
df = df.fillna('Haha')
print(df)
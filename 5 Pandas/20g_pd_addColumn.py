
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
# df = df.replace(0, np.NaN)
# df = df.fillna('Haha')
# print(df)

# =====================================
# create kolom selisih

df = df[['Open', 'Close']]
df['Selisih'] = df.apply(
    # lambda row: row.Open - row.Close, axis = 1
    # atau
    lambda row: row['Open'] - row['Close'], axis = 1
) 
print(df)

# =====================================
# create column kesimpulan: Close lbh besar atau Open lebih besar

df['LebihBesar'] = df.apply(
    lambda row: 'OPEN' if row['Open'] > row['Close'] else (
        'SAME' if row['Open'] == row['Close'] else 'CLOSE'
        ),
    axis = 1
)
print(df)
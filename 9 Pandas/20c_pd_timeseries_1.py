# resampling

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    '20_Apple_StockPrice.csv', 
    parse_dates=['date'], 
    index_col='date'
)

# resample data dg freq='Month end' 
# menampilkan rata2 closing tiap akhir bulan 
df2 = df['close'].resample('M').mean()

# resample data dg freq='Weekend' 
# menampilkan rata2 closing tiap akhir pekan 
# df2 = df['close'].resample('W').mean()

# resample data dg freq='Quarter' 
# menampilkan rata2 closing tiap kuarter 
# df2 = df['close'].resample('Q').mean()

print(df2)
plt.plot(df2, 'r--')
plt.plot(df2, 'go')
plt.xticks(rotation=90)
plt.show()
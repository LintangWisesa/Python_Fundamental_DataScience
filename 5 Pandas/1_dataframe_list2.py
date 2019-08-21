# dataframe

import pandas as pd 
# DF dgn list akan membentuk df per DATA BARIS
import numpy as np

x = np.random.randint(10, size=10)
y = np.random.randint(10, size=10)
z = 'bhksujrmvl'

df = pd.DataFrame([x,y,z])
print(x)
print(y)
print(df)

df = pd.DataFrame()
df['x'] = x
df['y'] = y
df['z'] = z
print(df)
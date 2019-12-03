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

# =========================================

x = [2,4,6,8,10]
y = [1,3,5,7,9]
z = list(map(lambda a, b: [a, b], x, y))
df = pd.DataFrame(z)
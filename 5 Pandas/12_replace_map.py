
import pandas as pd 
import numpy as np

data = {
    'nama': ['Andi', 'Budi', 'Caca'],
    'nilai': ['A', 'B', 'C'],
}
df = pd.DataFrame(data)
print(df)

df2 = df.replace(['A', 'B', 'C'], [100, 80, 60])
print(df2)

df3 = df2.sort_values(by='nilai', ascending=True)
df3 = df3.set_index(np.arange(0, 3))
print(df3)

df3.index = np.arange(1, 4)
print(df3)

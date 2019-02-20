
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
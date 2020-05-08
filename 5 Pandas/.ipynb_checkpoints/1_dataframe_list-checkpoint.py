# DF dgn list akan membentuk df per DATA BARIS

import pandas as pd 
import numpy as np 

x = [1,3,5,7,9,11,13,15,17,19]

df = pd.DataFrame(x, columns=['Nilai'], index=list('abcdefghij'))
print(df)
print(df.shape)

baris, kolom = df.shape
print(baris)

# set nilai row & col
print(df.index)
print(df.columns)
df.index = list('abcde')
df.columns = ['Nama', 'Nilai', 'Value', 'Ranking']
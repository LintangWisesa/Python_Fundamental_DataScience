# DF dgn dict akan membentuk df per KOLOM
import pandas as pd 
import numpy as np 

data = {
    'matakuliah': ['Senin', 'Selasa', 'Rabu'],
    'dosen': ['Andi', 'Budi', 'Caca'],
    'nilai': [82, 88, 79]
}

df2 = pd.DataFrame(data)

print(df2)
print(df2.dtypes)
print(df2.shape)
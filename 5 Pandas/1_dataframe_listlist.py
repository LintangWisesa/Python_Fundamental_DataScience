# DF dgn list akan membentuk df per DATA BARIS
import pandas as pd 
import numpy as np 

x = [
    ['Januari', 'Lemon', 90],
    ['Februari', 'Duku', 88],
    ['Maret', 'Apel', 93],
    ['April', 'Jeruk', 79],
    ['Mei', 'Manggis', 82]
]

df = pd.DataFrame(x, columns = ['Bulan', 'Buah', 'Harga'])
print(df)
print(df.shape)

baris, kolom = df.shape
print(baris)

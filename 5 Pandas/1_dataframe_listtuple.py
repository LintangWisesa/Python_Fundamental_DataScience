# DF dgn list akan membentuk df per DATA BARIS
import pandas as pd 
import numpy as np

a = [
    ('Andi', 21, 'S1'),
    ('Budi', 28, 'S2'),
    ('Caca', 22, 'S1'),
    ('Deni', 24, 'D3')
]

df = pd.DataFrame(
    a, 
    index = ['a', 'b', 'c', 'd'],
    columns = ['nama', 'usia', 'pendidikan']
)
print(df)

print(df.shape)
baris, kolom = df.shape
print(baris)

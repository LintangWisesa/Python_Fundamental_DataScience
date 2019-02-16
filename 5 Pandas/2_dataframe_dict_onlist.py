
import pandas as pd 
import numpy as np 

data = [
    {'nama': 'Andi', 'usia': 23},
    {'nama': 'Budi', 'usia': 32},
    {'nama': 'Caca', 'usia': 29},
    {'nama': 'Deni', 'usia': 38},
    {'nama': 'Euis', 'usia': 24}
]

df2 = pd.DataFrame(data)

print(df2)
print(df2.dtypes)
print(df2.shape)
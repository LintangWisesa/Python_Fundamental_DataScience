# jika 2 dataframe urutannya berbeda, berikan INDEX!

import pandas as pd 
import matplotlib.pyplot as plt

usia = {
    'nama': ['Andi', 'Budi', 'Caca'],
    'usia': [21, 22, 23]
}
usia_df = pd.DataFrame(usia, index = [0,1,2])

berat = {
    'nama': ['Caca', 'Budi'],
    'berat': [67, 68]
}
berat_df = pd.DataFrame(berat, index = [2,1])

df = pd.concat([usia_df, berat_df], axis=1)
print(df)
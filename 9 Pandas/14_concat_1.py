
# concat dataframe yg punya props saling beririsan (ada yg sama, data beda)

import pandas as pd 
import matplotlib.pyplot as plt

usia = {
    'nama': ['Andi', 'Budi', 'Caca'],
    'usia': [21, 22, 23]
}
usia_df = pd.DataFrame(usia)

berat = {
    'nama': ['Lala', 'Po'],
    'berat': [67, 68]
}
berat_df = pd.DataFrame(berat)

df = pd.concat([usia_df, berat_df])
print(df)
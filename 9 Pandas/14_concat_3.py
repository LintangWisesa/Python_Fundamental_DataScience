# concat dataframe dg series

import pandas as pd 
import matplotlib.pyplot as plt

usia = {
    'nama': ['Andi', 'Budi', 'Caca'],
    'usia': [11, 14, 17]
}
usia_df = pd.DataFrame(usia)

s = pd.Series(['SD', 'SMP', 'SMA'], name='pendidikan')

df = pd.concat([usia_df, s], axis=1)
print(df)
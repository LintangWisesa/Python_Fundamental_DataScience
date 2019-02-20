
# merge 2 dataframe yg valuenya ada yg beda!

import pandas as pd 

usia = {
    'nama': ['Andi', 'Budi', 'Caca'],
    'usia': [21, 22, 23]
}
usia_df = pd.DataFrame(usia)

berat = {
    'nama': ['Caca', 'Budi', 'Deni'],
    'berat': [67, 68, 69]
}
berat_df = pd.DataFrame(berat)

df = pd.merge(usia_df, berat_df, on='nama', how='outer')
print(df)

# how = 'inner' ialah default value how, Andi & Deni tdk tampil.
# how = 'outer' maka Andi & Deni akan ikut tampil
# how = 'left'
# how = 'right'
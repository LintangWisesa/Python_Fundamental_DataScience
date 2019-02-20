# merge di pandas = join sql
# merge 2 dataframe yg beda urutan val!

import pandas as pd 

usia = {
    'nama': ['Andi', 'Budi', 'Caca'],
    'usia': [21, 22, 23]
}
usia_df = pd.DataFrame(usia)

berat = {
    'nama': ['Caca', 'Budi', 'Andi'],
    'berat': [67, 68, 69]
}
berat_df = pd.DataFrame(berat)

df = pd.merge(usia_df, berat_df, on='nama')
print(df)

# hasilnya akan merge 2 df, walaupun urutan val nama beda,
# tapi data tetap benar. beda dg concat yg hrs pakai index.
# merge hny mnggabungkan data yg ada di semua dataframe,
# jika data tdk ada di semua df yg dimerge, maka tdk ditampilkan
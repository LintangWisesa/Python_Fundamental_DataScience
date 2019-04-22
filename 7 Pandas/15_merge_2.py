
# merge 2 dataframe yg sama, hny beda val!

import pandas as pd 

berat1 = {
    'nama': ['Andi', 'Budi', 'Caca'],
    'berat': [55, 56, 57]
}
berat1_df = pd.DataFrame(berat1)

berat2 = {
    'nama': ['Andi', 'Budi', 'Caca'],
    'berat': [65, 66, 67]
}
berat2_df = pd.DataFrame(berat2)

# hasilny ada kolom:  nama  berat_x  berat_y
# df = pd.merge(berat1_df, berat2_df, on='nama')
# print(df)

# hasilny ada kolom:  nama  berat_sebelum  berat_sesudah
df = pd.merge(berat1_df, berat2_df, on='nama', suffixes=['_sebelum', '_sesudah'])
print(df)
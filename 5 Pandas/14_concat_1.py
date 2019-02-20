
# concat dataframe yg punya beda props

import pandas as pd 
import matplotlib.pyplot as plt

usia = {
    'nama': ['Andi', 'Budi', 'Caca'],
    'usia': [21, 22, 23]
}
usia_df = pd.DataFrame(usia)

berat = {
    'nama': ['Andi', 'Budi', 'Caca'],
    'berat': [67, 68, 69]
}
berat_df = pd.DataFrame(berat)

# jika di-concat biasa seperti:
#       df = pd.concat([usia_df, berat_df])
#       print(df)
# 
# hasilnya akan:
#       berat  nama  usia
#       0    NaN  Andi  21.0
#       1    NaN  Budi  22.0
#       2    NaN  Caca  23.0
#       0   67.0  Andi   NaN
#       1   68.0  Budi   NaN
#       2   69.0  Caca   NaN
# 
# cara yg BENAR adalah:

df = pd.concat([usia_df, berat_df], axis=1)
print(df)
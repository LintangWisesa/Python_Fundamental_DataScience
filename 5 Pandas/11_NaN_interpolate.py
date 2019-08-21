
import pandas as pd 

df = pd.read_csv('10_data_NaN.csv', na_values=['-', 'n.a', 'not available'])

df2 = df.interpolate()
# data NaN akan terisi dg nilai antara data sblmny & sesudahnya
# 12  => 12
# NaN => 13
# 14  => 14

# gabungan fillna & interpolate!
# df2 = df.interpolate().fillna({
#     'nama': 'Tanpa Nama'
# })
print(df2)


import pandas as pd 

df = pd.read_csv('10_data_NaN.csv', na_values=['-', 'n.a', 'not available'])

df2 = df.dropna()
print(df2)

# hapus data yg semua kolomnya NaN
# df2 = df.dropna(how='all') 

# tetap tampilkan data yg memiliki minimal 1 value
# df2 = df.dropna(thresh = 1) 

# tetap tampilkan data yg memiliki minimal 2 value
# df2 = df.dropna(thresh = 2) 

# hide jika di kolom nama datanya NaN
# df = df.dropna(subset = ['nama'])

# hide jika di kolom nama & usia datanya NaN
# df = df.dropna(subset = ['nama', 'usia'])
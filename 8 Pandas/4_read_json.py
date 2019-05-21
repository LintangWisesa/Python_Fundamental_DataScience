import pandas as pd 
df = pd.read_json('5_data.json')

# print df, kolom json akan urut otomatis
print(df)

# membalik urutan kolom
cols = df.columns.tolist()
print(cols)
cols = cols[-1:] + cols[:-1]
df = df[cols]
print(df)

# mengurutan kolom secara manual
df = df[['nama', 'usia']]
print(df)
import pandas as pd 
df = pd.read_csv('5_datarokok.csv')

print(df)
df.to_csv('9_new.csv')

# pandas index tidak ikut disertakan di CSV:
# df.to_csv('9_new.csv', index=False)

# nama kolom tidak ikut disertakan di CSV:
# df.to_csv('9_new.csv', header=False)

# hanya kolom tertentu di dataframe yg akan disertakan dlm CSV:
# df.to_csv('9_new.csv', index=False, columns = ['kolom1', 'kolom2'])
# cleaning messy data with na_values

import pandas as pd 

# data yg berisi '-', 'n.a' & 'not available' akan dibaca sbg NaN
df = pd.read_csv('5_datarokok.csv', na_values=['-', 'n.a', 'not available'])

# na_values berisi dict utk menembak data di kolom tertentu!
# df = pd.read_csv('4_datarokok.csv', na_values={
#     'kolom1': ['-', 'n.a', 'not available'],
#     'kolom2': ['-', 'n.a', 'not available', -1]
# })

print(df)

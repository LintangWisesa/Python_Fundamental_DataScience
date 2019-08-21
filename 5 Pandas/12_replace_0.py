
import pandas as pd 
import numpy as np

df = pd.read_csv('10_data_NaN.csv')

# replace all '-' & 'n.a' to 0
df2 = df.replace(['-', 'n.a'], 0)
print(df2)

# replace all '-' & 'n.a' to NaN
# df2 = df.replace(['-', 'n.a'], np.NaN)
# print(df2)

# replace a specific val to another specific val
# df2 = df.replace({
#     '-': 0,
#     'n.a': 'No Data'
# })
# print(df2)

# replace a specific val on a specific column to NaN
# df2 = df.replace({
#     'kolom1': '-',
#     'kolom2': 'n.a',
# }, np.NaN)
# print(df2)

# replace with ffill method!
# df2 = df.replace(
#     to_replace=['-', 'n.a'],
#     method = 'ffill'
# )

# replace val di kolom tertentu dg val tertentu
# kolom nama '-' menjadi 'Anonim'
# kolom usia '-' menjadi 0
# kolom massa '-' & 'n.a' menjadi 0
# =====================================
# df = df.replace({
#     'nama': '-',
#     'usia': '-',
#     'massa': ['-', 'n.a']
# }, {
#     'nama': 'Anonim',
#     'usia': 0,
#     'massa': [0, 'data tak ada']
# })
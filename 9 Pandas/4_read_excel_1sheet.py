# beberapa kasus ada PC yg require xlrd! 
# solusi: install aja => pip install xlrd

import pandas as pd
df = pd.read_excel('4_data.xlsx', 'Sheet1')
# df = pd.read_excel('4_data.xlsx', header=None, skiprows=2)

print(df)

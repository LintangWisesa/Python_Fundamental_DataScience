# pip install pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# pip install xlrd
df1 = pd.read_excel('4_Book.xlsx', 'Sheet1')
df1 = df1.set_index('id')
df1 = df1.sort_values(by='id')

df2 = pd.read_excel('4_Book.xlsx', 'Gaji Dev')
df2 = df2.set_index('id')
df2 = df2.sort_values(by='id')

df1['gaji'] = df2['gaji']
print(df1)
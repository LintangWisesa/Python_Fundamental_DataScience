import pandas as pd 
df = pd.read_csv('5_datarokok.csv')

# print(df)
# print(df.shape)

# ======================

# print(df[df['2015'] == df['2015'].max()])
# print(df[df['2015'] >= df['2015'].mean()])
# print(df['Provinsi'][df['2015'] >= df['2015'].mean()])
# print(df[['Provinsi', '2015']][df['2015'] >= df['2015'].mean()])

import pandas as pd 
df = pd.read_csv('5_datarokok.csv')

# print(df)
# print(df.shape)

# ======================

# menampilkan data yg kolom 2015-nya max
# print(df[df['2015'] == df['2015'].max()])
# print(df[df['2015'] == df['2015'].max()]['Provinsi])

# menampilkan data yg kolom 2015-nya >= rata2nya
# print(df[df['2015'] >= df['2015'].mean()])
# print(df[df['2015'] >= df['2015'].mean()]['Provinsi'])

# menampilkan provinsi yg kolom 2015-nya > rata2
# print(df['Provinsi'][df['2015'] >= df['2015'].mean()])

# menampilkan data provinsi & 2015, yg 2015-nya >= rata2
# print(df[['Provinsi', '2015']][df['2015'] >= df['2015'].mean()])

# menampilkan data player yg skill overall >= 90 & clubnya Real Madrid
# df[['Name', 'Position', 'Club', 'Overall']][df['Overall'] >= 90][df['Club'] == 'Real Madrid']

# atau:
# df = df[['Name', 'Position', 'Club', 'Overall']][df['Overall'] >= 90]
# df = df[[df['Club'] == 'Real Madrid']]
# print(df)

# min, max & mean by column tertentu
# print(df.min(level='suhu'))
# print(df.max(level='suhu'))
# print(df.mean(level='suhu'))
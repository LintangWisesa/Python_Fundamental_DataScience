import pandas as pd
df = pd.read_csv('9_new.csv')

# replace kolom nama & usia saja
df = df.replace({
    'nama': '-',
    'usia': '-',
    'massa': ['-', 'n.a']
}, {
    'nama': 'Anonim',
    'usia': 0
}, method = 'ffill')
print(df.head())

# replace kolom massa dg method ffill
df['massa'] = df['massa'].replace(
    to_replace=['-', 'n.a'],
    method = 'ffill'
)
print(df.head())
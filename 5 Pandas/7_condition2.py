import pandas as pd 
df = pd.read_csv('5_datarokok.csv')

# menampilkan data yg closing pricenya antara 99 & 101
df = df[(df['closing_price'] >= 99) & (df['closing_price'] <= 101)]
# atau:
df = df[df['closing_price'].between(99, 101)]

# menampilkan data yg usia > 25 ATAU kota = jakarta
df = df[(df['usia'] > 25) | (df['kota'] == 'Jakarta')]
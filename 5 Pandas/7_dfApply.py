import numpy as np
import pandas as pd

df = pd.read_html('http://digidb.io/digimon-list/')
df = df[0]
print(df)

# ===============================================
# basic apply
print(df['Atk'].apply(np.sum))
print(df[['Atk', 'Def']].apply(np.sum, axis=0))
print(df[['Atk', 'Def']].apply(np.sum, axis=1))

# ===============================================
# create new col = hp + sp

# without apply 
# df['hp+sp'] = df['HP'] + df['SP']

# using apply
df['hp+sp'] = df[['HP', 'SP']].apply(np.sum, axis=1)
print(df.head())

# ===============================================
# create new col based on its hp+sp. if hp+sp < 700 = LOW & hp+sp > 700 = HIGH

df['status'] = df['hp+sp'].apply(lambda x: 'HIGH' if x > 700 else 'LOW')
print(df.head())

# ===============================================
# create a column based on 2 other col

# Atk > rata Atk & Def > rata Def : col ['SUPER'] == 'SUPER'
# Atk > rata Atk & Def < rata Def : col ['SUPER'] == 'SUPER ATK'
# Atk < rata Atk & Def > rata Def : col ['SUPER'] == 'EXTRA DEF'
# Atk < rata Atk & Def < rata Def : col ['SUPER'] == 'NOT SUPER'

def super(i):
    if i['Atk'] >= df['Atk'].mean() and i['Def'] >= df['Def'].mean():
        return 'SUPER'
    elif i['Atk'] < df['Atk'].mean() and i['Def'] >= df['Def'].mean():
        return 'SUPER DEF'
    elif i['Atk'] >= df['Atk'].mean() and i['Def'] < df['Def'].mean():
        return 'SUPER ATK'
    else:
        return 'NOT SUPER'

df['SUPER'] = df.apply(lambda x: super(x), axis=1)
print(df.head())
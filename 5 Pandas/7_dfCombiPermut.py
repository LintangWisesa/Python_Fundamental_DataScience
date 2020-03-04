import numpy as np
import pandas as pd

df = pd.read_html('http://digidb.io/digimon-list/')
df = df[0]
print(df)

# =================================
# jumlah unique val di stage, type & attr

print(len(df['Stage'].unique()))
print(len(df['Type'].unique()))
print(len(df['Attribute'].unique()))

# =================================

# Kombinasi 1 himpunan: [a, b, c]
#             x,y
# Kombinasi C(3,2) = x! / y!(x-y)! = 3 = ab, ac, bc
# Permutasi P(3,2) = x! / (x-y)!   = 6 = ab. ac, ba, bc, ca, cb

# ================================

# Kombinasi 2 himpunan: [a, b, c], [d, e, f]
# 3 * 3 = 9 = ad, bd, cd, ae, be, ce, af, bf, cf

# ================================

df['kombi'] = df['Stage'] + df['Type'] + df['Attribute']
len(df['kombi'].unique())
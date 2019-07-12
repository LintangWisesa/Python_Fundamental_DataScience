import pandas as pd
import numpy as np
df = pd.read_csv("23a_collab.csv", index_col=0)

df.fillna(0, inplace=True)
print(df)

# ================================================

# Pandas dataframe.corr() is used to find the pairwise correlation of all columns in the dataframe. 
# Any na values are automatically excluded. For any non-numeric data type columns in the dataframe it is ignored.

corrMatrix = df.corr(method='pearson')
print(corrMatrix)
# pearson : standard correlation coefficient
# kendall : Kendall Tau correlation coefficient
# spearman : Spearman rank correlation

# ================================================

MrX = [("action1",5),("romantic2",1),("romantic3",1)]
skorSama = pd.DataFrame()

for genre, rating in MrX:
    skor = corrMatrix[genre] * (rating - 2.5)
    skor = skor.sort_values(ascending=False)
    # print(skor)
    skorSama = skorSama.append(skor, ignore_index=True)

print(skorSama)
# action1   action2   action3  romantic1  romantic2  romantic3
# 0  2.500000  1.766722  2.034204  -1.998527  -0.063480  -2.285265
# 1  0.038088  0.778499  0.569970  -0.222059  -1.500000  -0.590909
# 2  1.371159  1.265061  1.203271  -1.085620  -0.590909  -1.500000

print(skorSama.sum().sort_values(ascending=False))
# action1      3.909247     # jumlah total sum() tiap kolom
# action2      3.810282
# action3      3.807445
# romantic2   -2.154389
# romantic1   -3.306206
# romantic3   -4.376174
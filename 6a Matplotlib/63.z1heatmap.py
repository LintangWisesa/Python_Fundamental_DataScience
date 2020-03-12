import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as im
df = pd.read_csv('63z_dataSales.csv')
df = df.pivot(index='nama', columns='mobil')

fig, p = plt.subplots()
plt.imshow(df, cmap='BuPu_r')
plt.colorbar()

col = list(map(lambda x: x[1], df.columns.tolist()))
print(col)
i = list(map(lambda x: x, df.index.tolist()))
print(i)

for x in range(len(i)):
    for y in range(len(col)):
        p.text(y, x, df.iloc[x, y], color='y')

p.set_xticks(np.arange(len(col)))
p.set_xticklabels(col)
p.set_yticks(np.arange(len(i)))
p.set_yticklabels(i)

# plt.xlim(-.5, 4.5)
# plt.ylim(-.5, 4.5)

plt.show()

# ===================================
# Heatmap: frequency, correlation, image
df = pd.DataFrame([
    {'sales':'Andi', 'HP A':100, 'HP B':120, 'HP C':65},
    {'sales':'Budi', 'HP A':10, 'HP B':20, 'HP C':5},
    {'sales':'Caca', 'HP A':80, 'HP B':70, 'HP C':60},
])
df = df.set_index('sales')
# df

plt.imshow(df, cmap='BuPu')
plt.colorbar()
plt.xticks(np.arange(3), ['HP A', 'HP B', 'HP C'])
plt.yticks(np.arange(3), ['Andi', 'Budi', 'Caca'])

for x in range(3):
    for y in range(3):
        plt.text(y-.1, x+.1, df.iloc[x, y], color='w', fontsize=18)

plt.show()
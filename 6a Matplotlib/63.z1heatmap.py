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
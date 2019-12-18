import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as im

df = pd.read_csv('63z_atlit.csv')
dfCorr = df.corr()
# print(dfCorr)

plt.imshow(dfCorr, cmap='hot_r')
plt.colorbar()

col = list(map(lambda x: x, dfCorr.columns.tolist()))
plt.xticks(
    np.arange(len(dfCorr.index)), 
    dfCorr.index.tolist(),
    rotation=45
)
plt.yticks(
    np.arange(len(dfCorr.index)), 
    dfCorr.index.tolist()
)

for x in range(len(col)):
    for y in range(len(col)):
        plt.text(y, x, round(dfCorr.iloc[x, y], 3), 
            color='w', ha='center', va = 'center'
        )

plt.show()
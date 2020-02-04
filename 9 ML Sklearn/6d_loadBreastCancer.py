import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt

data = load_breast_cancer()
# print(dir(data))
# print(data['target_names'])
print(data['feature_names'])

df = pd.DataFrame(
    data['data'],
    columns = data['feature_names']
)
df['target'] = data['target']
print(df.head())

dfCorr = df.corr()

# ===============================

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


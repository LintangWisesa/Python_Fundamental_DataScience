import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

dataBoston = load_boston()
# dataBoston = load_boston(return_X_y=True)
# print(dir(dataBoston))

df = pd.DataFrame(
    dataBoston['data'],
    columns = dataBoston['feature_names']
)
df['price'] = dataBoston['target']
# print(df)

korelasi = df.corr()
plt.imshow(korelasi, cmap='BuPu')
plt.colorbar()
plt.xticks(np.arange(14), list(df.columns))
plt.yticks(np.arange(14), list(df.columns))
plt.show()
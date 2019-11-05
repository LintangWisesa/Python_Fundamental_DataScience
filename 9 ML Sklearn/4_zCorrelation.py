# mencari kolom yg menentukan target
# cari correlation antar kolom di dataframe

from sklearn import linear_model
import pandas as pd
import numpy as np

data = {
    'luas': [2600, 3000, 3200, 3600, 4000],
    'kamar': [3, 4, 1, 3, 5],
    'usia': [20, 15, 18, 30, 8],
    'harga': [550000, 565000, 610000, 595000, 760000]
}
df = pd.DataFrame(data)
print(df)

# ==================================
# find correlation & plot on a heatmap

corr = df.corr()
print(corr)

# plot with matplotlib heatmap
import matplotlib.pyplot as plt
plt.imshow(corr, cmap='hot_r')
plt.xticks(np.arange(4), df.columns)
plt.yticks(np.arange(4), df.columns)
plt.colorbar()
plt.show()

# plot with seaborn heatmap
import seaborn as sb
sb.heatmap(corr, annot=True)
plt.show()

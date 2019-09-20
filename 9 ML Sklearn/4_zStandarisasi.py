import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = [
    {'tb': 169.6, 'bb': 71.2},
    {'tb': 166.8, 'bb': 58.2},
    {'tb': 157.1, 'bb': 56},
    {'tb': 181.1, 'bb': 90},
    {'tb': 158.4, 'bb': 53},
    {'tb': 165.6, 'bb': 52.4},
    {'tb': 166.7, 'bb': 56.8},
    {'tb': 156.5, 'bb': 49.2},
    {'tb': 168.1, 'bb': 55.6},
    {'tb': 165.3, 'bb': 77.8}
]

df = pd.DataFrame(data)
print(df.head())

plt.subplot(121)
plt.boxplot(df['tb'])

# standardisasi
from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
scaled = scaler.fit_transform(df)
df_scaled = pd.DataFrame(scaled)
print(df_scaled.head())

plt.subplot(122)
plt.boxplot(df_scaled[0])
plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'x': [1,2,3,4,5],
    'y': [2,4,6,8,10],
    'z': [1,3,5,7,9],
})

# plt.plot(df['x'], df['y'])
# plt.plot(df['x'], df['y'], df.x, df.y)
plt.plot(df['x'], df[['y', 'z']])
plt.show()
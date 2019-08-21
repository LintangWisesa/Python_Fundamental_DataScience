import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# sns.set(style="white")

data = sns.load_dataset('flights')
# print(data)
data = data.pivot('month', 'year', 'passengers')

# sns.heatmap(data)
# sns.heatmap(data, cmap='BuPu')
# sns.heatmap(data, cmap='BuPu_r') # reverse color map
# sns.heatmap(data, linewidth=.05)
# sns.heatmap(data, cbar=False)
sns.heatmap(data, annot=True, fmt='d')

plt.show()
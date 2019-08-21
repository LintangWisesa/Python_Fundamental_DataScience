import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataku = sns.load_dataset('flights')
print(dataku)

sns.set(rc = {'figure.figsize':(12,12)})
sns.violinplot(x='year', y='passengers', data=dataku, inner=None)
sns.swarmplot(x='year', y='passengers', data=dataku, color='w')

plt.xticks(rotation=45)
plt.show()
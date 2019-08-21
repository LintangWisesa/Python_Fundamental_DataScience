import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# sns.set(style="white")

dataku = sns.load_dataset('flights')
print(dataku)

# sns.violinplot(x='year', y='passengers', data=dataku)
sns.violinplot(x='year', y='passengers', data=dataku, inner=None)

plt.xticks(rotation=45)
plt.show()
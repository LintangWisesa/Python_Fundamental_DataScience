import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# sns.set(style="white")

dataku = sns.load_dataset('flights')
print(dataku)

sns.swarmplot(x='month', y='passengers', data=dataku)
plt.xticks(rotation=45)
plt.show()
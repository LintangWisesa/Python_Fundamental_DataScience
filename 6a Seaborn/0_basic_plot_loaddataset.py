# pip install seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

dataku = sns.load_dataset('flights')
print(dataku)

sns.relplot(x='year', y='passengers', data=dataku)
# sns.relplot(x='year', y='passengers', data=dataku, kind='line')
# sns.relplot(
#     x='year', 
#     y='passengers', 
#     data=dataku, 
#     # kind='line',
#     hue='month',
#     size = 'month'
#     # style='month'
# )

plt.show()
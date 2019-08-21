import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

dataku = pd.DataFrame({
    'x': np.arange(10),
    'y': np.random.randint(10, size=10),
    'z': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No']
})

# sns.catplot(x='x', y='y', data=dataku)
# sns.catplot(x='x', y='y', data=dataku, kind='point')
sns.catplot(x='x', y='y', hue='z', data=dataku, kind='bar')
plt.show()

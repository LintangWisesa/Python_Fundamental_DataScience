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

# sns.relplot(x='x', y='y', hue='z', data=dataku)
# sns.relplot(x='x', y='y', hue='z', style='z', data=dataku)
# sns.relplot(x='x', y='y', hue='z', style='z', size='z', data=dataku)
sns.relplot(x='x', y='y', hue='z', style='z', size='z', data=dataku, kind='line')
plt.show()

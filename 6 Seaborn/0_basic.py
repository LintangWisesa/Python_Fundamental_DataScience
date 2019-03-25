import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

dataku = pd.DataFrame({
    'x': np.arange(10),
    'y': np.random.randint(10, size=10),
})

# scatter type
# sns.relplot(x='x', y='y', data=dataku)

# line type
sns.relplot(x='x', y='y', data=dataku, kind='line')

plt.xticks(rotation=90)
plt.show()

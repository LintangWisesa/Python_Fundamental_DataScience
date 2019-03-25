import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# sns.set(style="white")

random_state = np.random.RandomState(10)
mean = [2,2]
cov = [(1, .5), (.5, 1)]

x1, x2 = random_state.multivariate_normal(mean, cov, 500).T
x1 = pd.Series(x1, name='Example_X')
x2 = pd.Series(x2, name='Example_Y')

sns.jointplot(x1, x2, kind='kde', height=7, space=0, color='r')
plt.show()

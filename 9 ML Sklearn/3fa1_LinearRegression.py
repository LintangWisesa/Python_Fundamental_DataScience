# https://jakevdp.github.io/PythonDataScienceHandbook/05.06-linear-regression.html

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# =================================
# data
rng = np.random.RandomState(1)
print(rng)
x = 10 * rng.rand(50)
print(x)
y = 2 * x - 5 + rng.randn(50)
print(y)

plt.scatter(x, y);
# plt.show()

# =================================
# linear regression
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x.reshape(-1, 1), y)
xfit = np.linspace(0, 10, 1000)
yfit = model.predict(xfit.reshape(-1, 1))

plt.scatter(x, y)
plt.plot(xfit, yfit);
plt.show()

print("Model slope:    ", model.coef_[0])
print("Model intercept:", model.intercept_)

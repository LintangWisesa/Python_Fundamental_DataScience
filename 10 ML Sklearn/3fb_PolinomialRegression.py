# Linear Regression Polynomial basis functions

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

from sklearn.preprocessing import PolynomialFeatures
# x = np.array([2, 3, 4])
# poly = PolynomialFeatures(3, include_bias=False)
# print(poly.fit_transform(x.reshape(-1,1)))

from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
poly_model = make_pipeline(
    PolynomialFeatures(7),
    LinearRegression()
)

rng = np.random.RandomState(1)
x = 10 * rng.rand(50)
y = np.sin(x) + 0.1 * rng.randn(50)

poly_model.fit(x.reshape(-1,1), y)
xfit = np.linspace(0, 10, 1000)
print(xfit)
yfit = poly_model.predict(xfit.reshape(-1,1))

plt.scatter(x, y)
plt.plot(xfit, yfit)
plt.show()
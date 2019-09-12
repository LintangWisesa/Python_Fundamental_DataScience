import numpy as np
import pandas as pd

x = np.sort(np.random.randn(1000))
y = np.sin(-x)

import matplotlib.pyplot as plt
# plt.scatter(x, y)
# plt.show()

# Fit regression model
from sklearn.tree import DecisionTreeRegressor
regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_1.fit(x.reshape(-1,1), y)
regr_2.fit(x.reshape(-1,1), y)

# Predict
y_1 = regr_1.predict(x.reshape(-1,1))
y_2 = regr_2.predict(x.reshape(-1,1))

# Plot the results
plt.figure()
plt.scatter(x, y, s=20, edgecolor="black", c="darkorange", label="data")
plt.plot(x, y_1, color="cornflowerblue", label="max_depth=2", linewidth=2)
plt.plot(x, y_2, color="yellowgreen", label="max_depth=5", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()
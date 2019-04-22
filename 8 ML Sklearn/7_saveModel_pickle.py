# save model with pickle

from sklearn import linear_model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'luas': [2600, 3000, 3200, 3600, 4000],
    'harga': [550000, 565000, 610000, 680000, 725000]
}
df = pd.DataFrame(data)
print(df)

model = linear_model.LinearRegression()
model.fit(df[['luas']], df['harga'])

# print(model.predict([[3300]]))
# print(model.coef_)
# print(model.intercept_)

# ========================================
# save model with pickle

import pickle

# wb: write bytes
with open('7_savedModel', 'wb') as modelku:
    pickle.dump(model, modelku)
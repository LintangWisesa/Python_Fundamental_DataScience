# save model with joblib
# jika model mengandung banyak numpy array,
# joblib lbh efisien dibanding pickle

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
# save model with joblib

from sklearn.externals import joblib

joblib.dump(model, '9_saveModel_joblib')
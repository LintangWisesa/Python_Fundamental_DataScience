import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

data = {
    'mesin': [1000,2000,3000,4000,5000],
    'harga': [10,25,35,55,80]
}
df = pd.DataFrame(data)
# print(df)

model = linear_model.LinearRegression()
model.fit(df[['mesin']], df['harga'])
# print(model.coef_)
# print(model.intercept_)

yLR = model.predict(df[['mesin']])
df['harga_LR'] = yLR
# print(df)

plt.plot(df['mesin'], df['harga'])
# plt.show()

# ===========================================
# Evaluation Metrics

from sklearn.metrics import max_error, mean_absolute_error, mean_squared_error
from sklearn.metrics import median_absolute_error
from sklearn.metrics import mean_squared_log_error, r2_score

# loss function: makin kecil makin baik
print("Max Error:", max_error(df['harga'], df['harga_LR']))
print("MAE:", 
      round(mean_absolute_error(df['harga'], df['harga_LR']), 2))
print("MSE:", 
      round(mean_squared_error(df['harga'], df['harga_LR']), 2))
print("RMSE:", 
      np.sqrt(round(mean_squared_error(df['harga'], df['harga_LR']), 2)))
print("MedAE:", 
      round(median_absolute_error(df['harga'], df['harga_LR']), 2))
print("MSLE:", 
      mean_squared_log_error(df['harga'], df['harga_LR']))
print("RMSLE:", 
      np.sqrt(mean_squared_log_error(df['harga'], df['harga_LR'])))

# reward score: makin besar makin baik
print("R2 Score:", 
      r2_score(df['harga'], df['harga_LR']))
print(model.score(
      df['harga'], df['harga_LR']))
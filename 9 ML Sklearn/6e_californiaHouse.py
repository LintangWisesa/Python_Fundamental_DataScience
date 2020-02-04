import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing

# ==============================
# load datasets 
dataCH = fetch_california_housing()
# print(dir(dataCH))
# print(dataCH.data[0])
# print(dataCH['feature_names'])
print(dataCH.target[0])

# ==============================
# create dataframe
dfCH = pd.DataFrame(
    dataCH.data,
    columns = dataCH['feature_names']
)
dfCH['PRICE'] = dataCH.target
print(dfCH)

# ==============================
# see correlation
print(dfCH.corr())
import matplotlib.pyplot as plt
plt.imshow(dfCH.corr(), cmap='hot_r')
plt.yticks(np.arange(9), dfCH.columns)
plt.colorbar()

# ==============================
# splitting
x = dfCH[['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 
    'Population', 'AveOccup', 'Latitude', 'Longitude' ]]
y = dfCH['PRICE']
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .02)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)

# ==============================
# prediksi
print(model.predict([x_test.iloc[0]]))
# score accuracy
print(model.score(x_test, y_test) * 100)
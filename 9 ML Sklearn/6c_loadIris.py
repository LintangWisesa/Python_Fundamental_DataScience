import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

dataIris = load_iris()
# print(dir(dataIris))
# print(dataIris['target_names'])

dfIris = pd.DataFrame(
    dataIris['data'],
    columns = ['SL', 'SW', 'PL', 'PW']
)
dfIris['target'] = dataIris['target']
dfIris['spesies'] = dfIris['target'].apply(
    lambda x: dataIris['target_names'][x]
)

dfSetosa = dfIris[dfIris['target'] == 0]
dfVersicolor = dfIris[dfIris['target'] == 1]
dfVirginica = dfIris[dfIris['target'] == 2]

fig = plt.figure('Data Iris', figsize = (12,6))

# plot sepal length vs sepal width
plt.subplot(121)
plt.scatter(dfSetosa['SL'], dfSetosa['SW'], marker='o', color='r')
plt.scatter(dfVersicolor['SL'], dfVersicolor['SW'], marker='o', color='g')
plt.scatter(dfVirginica['SL'], dfVirginica['SW'], marker='o', color='b')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend(['Setosa', 'Versicolor', 'Virginica'])
plt.grid(True)

# plot petal length vs petal width
plt.subplot(122)
plt.scatter(dfSetosa['PL'], dfSetosa['PW'], marker='o', color='r')
plt.scatter(dfVersicolor['PL'], dfVersicolor['PW'], marker='o', color='g')
plt.scatter(dfVirginica['PL'], dfVirginica['PW'], marker='o', color='b')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.legend(['Setosa', 'Versicolor', 'Virginica'])
plt.grid(True)

plt.show()
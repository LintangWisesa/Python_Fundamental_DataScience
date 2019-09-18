# K-Means
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

data = load_iris()
# print(dir(data))
# print(data['target_names'])

df = pd.DataFrame(
    data.data,
    columns = ['SL', 'SW', 'PL', 'PW']
)
df['target'] = data.target
df['spesies'] = df.target.apply(
    lambda a: data.target_names[a]
)
print(df)
print(df.isnull().sum())

df0 = df[df['target'] == 0]
df1 = df[df['target'] == 1]
df2 = df[df['target'] == 2]

# k-means
from sklearn.cluster import KMeans
model1 = KMeans(
    n_clusters = len(data.target_names), 
    random_state=1
)
model2 = KMeans(
    n_clusters = len(data.target_names), 
    random_state=1
)

model1.fit(df[[ 'SL', 'SW' ]], df['target'])
model2.fit(df[[ 'PL', 'PW' ]], df['target'])

# predict
prediksiS = model1.predict(df[[ 'SL', 'SW' ]])
prediksiP = model1.predict(df[[ 'PL', 'PW' ]])

df['prediksiS'] = prediksiS
df['prediksiP'] = prediksiP
print(df)

centroidS = model1.cluster_centers_
centroidP = model2.cluster_centers_

# plotting: sepal L vs sepal W && petal L vs petal W
import matplotlib.pyplot as plt
fig = plt.figure('Data Iris', figsize=(10, 4))

plt.subplot(221)
plt.plot(df0['SL'], df0['SW'], 'r.')
plt.plot(df1['SL'], df1['SW'], 'g.')
plt.plot(df2['SL'], df2['SW'], 'b.')
plt.scatter(
    centroidS[:,0],
    centroidS[:,1],
    marker = '*',
    color = 'y',
    s = 200
)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend(['Setosa', 'Versicolor', 'Virginica', 'Centroid'])

plt.subplot(222)
plt.plot(df0['PL'], df0['PW'], 'r.')
plt.plot(df1['PL'], df1['PW'], 'g.')
plt.plot(df2['PL'], df2['PW'], 'b.')
plt.scatter(
    centroidP[:,0],
    centroidP[:,1],
    marker = '*',
    color = 'y',
    s = 200
)
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.legend(['Setosa', 'Versicolor', 'Virginica', 'Centroid'])

plt.subplot(223)
plt.plot(df0['PL'], df0['PW'], 'r.')
plt.plot(df1['PL'], df1['PW'], 'g.')
plt.plot(df2['PL'], df2['PW'], 'b.')
plt.scatter(
    centroidP[:,0],
    centroidP[:,1],
    marker = '*',
    color = 'y',
    s = 200
)
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.legend(['Setosa', 'Versicolor', 'Virginica', 'Centroid'])

plt.subplot(224)
plt.plot(df0['PL'], df0['PW'], 'r.')
plt.plot(df1['PL'], df1['PW'], 'g.')
plt.plot(df2['PL'], df2['PW'], 'b.')
plt.scatter(
    centroidP[:,0],
    centroidP[:,1],
    marker = '*',
    color = 'y',
    s = 200
)
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.legend(['Setosa', 'Versicolor', 'Virginica', 'Centroid'])

# plt.show()
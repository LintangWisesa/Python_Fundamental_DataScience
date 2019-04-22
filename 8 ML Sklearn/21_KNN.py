# K Nearest Neighbour
# it classifies a data point based on how its neighbours are classified!

# k in KNN is a parameter that refers to the number of nearest neighbors to include in the majority voting process
# how to choose k? => parameter tuning process: 
# sqrt(n): square root of total number of data point
# choose odd value to avoid confussion between 2 classes of data

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
digits = load_digits()

from sklearn.datasets import load_iris
iris = load_iris()

# ========================================
# create dataframe

df = pd.DataFrame(iris['data'], columns=iris['feature_names'])
df['target'] = iris['target']
df['spesies'] = df['target'].apply(lambda x: iris['target_names'][x])
# print(df)

# =============================================
# split dataset dg test = 0.2

from sklearn.model_selection import train_test_split
x = df.drop(['target', 'spesies'], axis='columns')  # data utama
y = df['target']                                    # data target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2)
# print(len(y_test))

# ===================================
# train model with KNN algorithm

from sklearn.neighbors import KNeighborsClassifier

# k = round((len(x_train)+len(x_test)) ** .5)
# print(k)

def nilai_k():
    k = round((len(x_train)+len(x_test)) ** .5)
    if (k % 2 == 0):
        return k + 1
    else:
        return k
print(nilai_k())

model = KNeighborsClassifier(
    n_neighbors = nilai_k(),    
    # p = 3, 
    # metric = 'euclidean'
)

model.fit(x_train, y_train)

print(model.predict([x_test.iloc[0]]))
print(y_test.iloc[0])

print(model.score(x_test, y_test) * 100, '%')
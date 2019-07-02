import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

data = sb.load_dataset('titanic')
# print(data.columns.values)

# 1 labelling
from sklearn.preprocessing import LabelEncoder
label = LabelEncoder()

data['sex'] = label.fit_transform(data['sex'])
# print(label.classes_)       # ['female' 'male']

data['who'] = label.fit_transform(data['who'])
# print(label.classes_)       # 'child' 'man' 'woman' 0  1  2

data['adult_male'] = label.fit_transform(data['adult_male'])
# print(label.classes_)      # [False  True]  

data['alone'] = label.fit_transform(data['alone'])
# print(label.classes_)       # [False  True]

data = data.drop(
    ['embarked', 'class', 'deck', 'embark_town', 'alive'],
    axis=1
)
data = data.dropna(subset = ['age'])
# print(data)

# Split: feature X & target Y
x = data.drop(['survived'], axis=1)
# print(x.iloc[0])
y = data['survived']
# print(y)

# ONE HOT ENCODER
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

coltrans = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories='auto'), [1, 6])],    # 1,6 = index col yang akan di-one hot encoding
    remainder='passthrough'
)
x = np.array(coltrans.fit_transform(x), dtype=np.float64)
# print(x[0])
# [ 0.    1.    0.    1.    0.    3.     22.    1.    0.    7.25     1.    0.  ]
# fm   male  child  man  woman  pclass  age  sibsp  par   fare   adultM   alone

# splitting
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(
    x,
    y,
    test_size = .1
)
# print(xtrain[0])
# print(ytrain.iloc[0])
# print(xtest[0])
# print(ytest.iloc[0])

# logistic regression
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(solver='liblinear')
model.fit(xtrain, ytrain)

# print(round(model.score(xtest, ytest) * 100, 2), '%')
# print(xtest[0])
# print(ytest.iloc[0])
# print(model.predict(xtest[0].reshape(1, -1)))

# [ 0.    1.    0.    1.    0.    3.     22.    1.    0.    7.25     1.    0.  ]
# fm   male  child  man  woman  pclass  age  sibsp  par   fare   adultM   alone
# print(model.predict([[0, 1, 1, 0, 0, 1, 5, 1, 2, 100, 0, 0]]))

import joblib
joblib.dump(model, 'modelTitanic')
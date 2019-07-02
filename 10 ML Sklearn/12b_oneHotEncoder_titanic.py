import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

data = sb.load_dataset('titanic')
# print(data)

# ==========================================
# label encoder
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
dfle = data
dfle['sex'] = le.fit_transform(dfle['sex'])
# print(list(le.classes_))        # ['female', 'male']
dfle['who'] = le.fit_transform(dfle['who'])
# print(list(le.classes_))      # ['child', 'man', 'woman']
dfle['adult_male'] = le.fit_transform(dfle['adult_male'])
# print(list(le.classes_))        # [False, True]
dfle['alone'] = le.fit_transform(dfle['alone'])
# print(list(le.classes_))        # [False, True]

# ==========================================
# clean missing data value
# print(dfle[['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'who', 'adult_male', 'alone']].isnull())
dfle = dfle.dropna(subset = ['age'])
# print(dfle)

# ==========================================
# define x feature & y target
x = dfle[['sex', 'who', 'adult_male', 'alone', 'pclass', 'age', 'sibsp', 'parch', 'fare']]
# print(x.iloc[0])
y = dfle['survived']
# print(y)

# ==========================================
# one hot encoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories='auto'), [0, 1, 2, 3])],
    remainder='passthrough'
)

x = np.array(ct.fit_transform(x), dtype=np.float64)
# print(x[0])
# [    0.    1.    0.    1.      0.         0.            1.             1.          0.         3.    22.    1.      0.    7.25]
# [ female male child   man   woman  adultman_false  adultman_true  alone_false  alone_true  pclass  age   sibsp  parch    fare]

# ==========================================
# split datasets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    x, 
    y, 
    test_size=.1
)
# print(x_train[0])
# print(y_train.iloc[0])
# print(x_test[0])
# print(y_test.iloc[0])

# ============================================
# logistic regression
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(solver='liblinear')
model.fit(x_train, y_train)
print(round(model.score(x_test, y_test) * 100, 2), '%')

# ============================================
# predict
# [female male] [child man woman] [adultman_false adultman_true] [alone_false alone_true] pclass age sibsp parch fare]
print(model.predict([[0., 1., 0., 1., 0., 0., 1., 0., 1., 3., 32., 0., 0., 7.8542]]))

# predict x_test
print(x_test[0])
print(model.predict(x_test[0].reshape(1, -1)))
print(y_test.iloc[0])

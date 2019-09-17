import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# ===================================
# create dataframe
data = load_iris()
df = pd.DataFrame(
    data['data'],
    columns = ['SL', 'SW', 'PL', 'PW']
)
df['target'] = data['target']
df['sp'] = df['target'].apply(
    lambda i: data['target_names'][i]
)
# print(df.shape)
# print(df.isnull().sum())

# ===================================
# splitting datasets: 5% testing data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    df[[ 'SL', 'SW', 'PL', 'PW' ]],
    df['sp'],
    test_size = .05
)

# ===================================
# fitting model RanFor
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(
    n_estimators = 100
)
model.fit(x_train, y_train)
# print(round(model.score(x_train, y_train) * 100, 2), '%')
# print(round(model.score(x_test, y_test) * 100, 2), '%')

# ===================================
# predict data testing
# print(x_test.iloc[0])
# print(y_test.iloc[0])
# print(model.predict([x_test.iloc[0]]))
# print(model.predict_proba([x_test.iloc[0]]))

# ===================================
# predict external data
# print(model.predict([[ 2, 3.2, 1.0, 1.9 ]])[0])
# print(model.predict_proba([[ 2, 3.2, 1.0, 1.9 ]]))

data = np.array([2, 3.2, 1.0, 1.9])
pred = model.predict([data])[0]
proba = model.predict_proba([data])
proPred = np.max(proba) * 100

print(proPred, '%', pred)
# 40% Setosa
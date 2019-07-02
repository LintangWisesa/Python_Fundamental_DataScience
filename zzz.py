import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('zzz.csv', sep=',')
# print(df)

# =========================================
# split datasets = data train & data test

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    df[['usia']], 
    df['beliAsuransi'], 
    test_size=.1
)

# =========================================
# logistic regression

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(solver='lbfgs')

# training model
model.fit(x_train, y_train)

# m coef & b intercept
# print(model.coef_)
# print(model.intercept_)

# accuracy
# print(model.score(x_train, y_train))

# =========================================

# prediction
# print(x_test)
# print(model.predict(x_test))
# print(model.predict([[40]]))

# probablility
# print(model.predict_proba(x_test))
# print(model.predict_proba([[40]]))

# =========================================

# plot dataframe
plt.scatter(df['usia'], df['beliAsuransi'])

dataplot = np.linspace(0,70,150)
def plotlogreg(line):
    return 1 / (1 + np.exp(-line))
bestfit = plotlogreg(
    (model.coef_ * dataplot) + model.intercept_).ravel()

print(bestfit)

# plot best fit line logistic regression: sigmoid func
plt.plot(
    dataplot,
    bestfit,
    'r-'
)

plt.xlabel('Usia')
plt.ylabel('Membeli Asuransi')
plt.title('Data pengguna asuransi')
# plt.show()
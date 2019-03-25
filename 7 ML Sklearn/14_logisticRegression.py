# logistic reg utk classification problem
# misal: apakah customer akan beli asuransi?
# dasar: sigmoid / logit func => convert input into range 0-1
# sigmoid(x) = 1/1+e^(-x)

# linear reg => y = mx + b
# logist reg => y = 1/1+e^(-mx+b)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

asuransi = {
    'usia': np.arange(70),
    'beli': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
}

# asuransi = {
#     'usia': [22,25,47,52,46,56,55,60,62,61,18,28,27,29,49,55,25,58,19,18,21,26,40,45,50,54,23],
#     'beli': [0,0,1,0,1,1,0,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0]
# }

df = pd.DataFrame(asuransi)
# print(df)

# plt.scatter(df['usia'], df['beli'], color='g')
# plt.show()

# ==================================

# split datasets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(df[['usia']], df['beli'], test_size=.1)

# import logistic reg
from sklearn.linear_model import LogisticRegression
# model = LogisticRegression()
model = LogisticRegression(solver='lbfgs') # avoid warning!

# training model
model.fit(x_train, y_train)

# coef & intercept
print(model.coef_)
print(model.intercept_)

# prediksi
print(x_test)                   # data usia
print(model.predict(x_test))    # beli asuransi atau tidak
print(model.predict([[43]]))    # usia 43 beli atau tidak

# akurasi
print(model.score(x_test, y_test))

# ====================================

# predict probabilities
print(model.predict_proba(x_test))  # kemungkinan beli/tdk utk data test!

# [
#   [0.676767, 0.321234],   => data ke-1: 67% tdk beli
#   [0.645432, 0.321234],   => data ke-2: 64% tdk beli
#   [0.323232, 0.676767]    => data ke-3: 32% tdk beli
# ]

# ====================================
# plot data

dataTes = np.linspace(0, 70, 150)
def plotLogReg(x):
    return 1 / (1 + np.exp(-x))

loss = plotLogReg((dataTes * model.coef_) + model.intercept_).ravel()

plt.plot(df['usia'], df['beli'], 'ro')
plt.plot(dataTes, loss, color='g', linewidth=2)

plt.grid(True)
plt.xlabel('Usia (th)')
plt.ylabel('Probabilitas membeli asuransi')
plt.yticks(np.arange(2))
plt.title('Logistic Regression')
plt.show()
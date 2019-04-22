
# cross validation:
# which model has the best performance?
# 1. train & test model with same datasets
# 2. split datasets into train & test, then fit to model
# 3. k-fold cross validation: membagi datasets mnjadi beberapa 'lipatan',
#                             tiap lipatan jadikan test data,
#                             nilainya dirata-rata

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

digits = load_digits()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(digits['data'], digits['target'], test_size=.3)


# ================================================
# MEMBANDINGKAN AKURASI ANTARA LOGISTIC REGRESSION, SVC & RANDOM FOREST
# ================================================


# ================================================
# logistic regression

from sklearn.linear_model import LogisticRegression
# modellr = LogisticRegression()
# modellr.fit(x_train, y_train)
# print(modellr.score(x_test, y_test))

# ================================================
# svm

from sklearn.svm import SVC
# modelsv = SVC()
# modelsv.fit(x_train, y_train)
# print(modelsv.score(x_test, y_test))

# ================================================
# random forest

from sklearn.ensemble import RandomForestClassifier
# modelrf = RandomForestClassifier()
# modelrf.fit(x_train, y_train)
# print(modelrf.score(x_test, y_test))


# ================================================
# MEMBANDINGKAN AKURASI ANTARA LOGISTIC REGRESSION, SVC & RANDOM FOREST
# DENGAN K-FOLD CROSS VALIDATION!
# ================================================


from sklearn.model_selection import KFold
kf = KFold(n_splits=3) # jumlah 'lipatan'

# for train_index, test_index in kf.split([1,2,3,4,5,6,7,8,9]):
#     print(train_index, test_index)

def get_score(model, x_train, x_test, y_train, y_test):
    model.fit(x_train, y_train)
    return model.score(x_test, y_test)

# print(get_score(LogisticRegression(), x_train, x_test, y_train, y_test))
# print(get_score(SVC(), x_train, x_test, y_train, y_test))
# print(get_score(RandomForestClassifier(), x_train, x_test, y_train, y_test))


# ================================================
# MEMBANDINGKAN AKURASI ANTARA LOGISTIC REGRESSION, SVC & RANDOM FOREST
# DENGAN MANUAL STRATIFIED K-FOLD! (tanpa stratified kfold, nilai akurasi berubah-ubah)
# ================================================


# from sklearn.model_selection import StratifiedKFold
# folds = StratifiedKFold(n_splits=3)

# score_lr = []
# score_sv = []
# score_rf = []

# for train_index, test_index in kf.split(digits['data']):
#     x_train = digits['data'][train_index]
#     x_test = digits['data'][test_index]
#     y_train = digits['target'][train_index]
#     y_test = digits['target'][test_index]
#     # print(get_score(LogisticRegression(), x_train, x_test, y_train, y_test))
#     # print(get_score(SVC(), x_train, x_test, y_train, y_test))
#     # print(get_score(RandomForestClassifier(), x_train, x_test, y_train, y_test))
#     score_lr.append(get_score(LogisticRegression(), x_train, x_test, y_train, y_test))
#     score_sv.append(get_score(SVC(), x_train, x_test, y_train, y_test))
#     score_rf.append(get_score(RandomForestClassifier(n_estimators=40), x_train, x_test, y_train, y_test))

# print(score_lr)
# print(score_sv)
# print(score_rf)
# cari nilai akurasi rata-ratanya utk mncari nilai terbaik!


# ================================================
# MEMBANDINGKAN AKURASI ANTARA LOGISTIC REGRESSION, SVC & RANDOM FOREST
# DENGAN K-FOLD CROSS VALIDATON SCORE! so easy
# ================================================


from sklearn.model_selection import cross_val_score
print(cross_val_score(LogisticRegression(), digits['data'], digits['target']))
print(cross_val_score(SVC(), digits['data'], digits['target']))
print(cross_val_score(RandomForestClassifier(n_estimators=40), digits['data'], digits['target']))
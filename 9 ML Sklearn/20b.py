import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

digits = load_digits()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    digits['data'], 
    digits['target'], 
    test_size=.1
)

from sklearn.linear_model import LogisticRegression
modellr = LogisticRegression(solver='lbfgs', multi_class='auto', max_iter=10000)
from sklearn.svm import SVC
modelsv = SVC(gamma='auto', probability=True)
from sklearn.ensemble import RandomForestClassifier
modelrf = RandomForestClassifier(n_estimators=10)

# K-Fold, hasil akurasi akan berubah-ubah
from sklearn.model_selection import KFold
kf = KFold(n_splits=3) # jumlah 'lipatan'

# for train_index, test_index in kf.split([1,2,3,4,5,6,7,8,9]):
#     print(train_index, test_index)

def get_score(model, x_train, x_test, y_train, y_test):
    model.fit(x_train, y_train)
    return model.score(x_test, y_test)

score_lr = []
score_sv = []
score_rf = []

for train_index, test_index in kf.split(digits['data']):
    x_train = digits['data'][train_index]
    x_test = digits['data'][test_index]
    y_train = digits['target'][train_index]
    y_test = digits['target'][test_index]

    score_lr.append(get_score(modellr, x_train, x_test, y_train, y_test))
    score_sv.append(get_score(modelsv, x_train, x_test, y_train, y_test))
    score_rf.append(get_score(modelrf, x_train, x_test, y_train, y_test))

# print(score_lr)
# print(score_sv)
# print(score_rf)
print('Score LR:', np.mean(score_lr))
print('Score SV:', np.mean(score_sv))
print('Score RF:', np.mean(score_rf))
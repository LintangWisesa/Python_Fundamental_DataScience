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

from sklearn.model_selection import cross_val_score
# print(cross_val_score(
#         modellr, digits['data'], digits['target'], cv=5)
# )
# print(cross_val_score(
#     modelsv, digits['data'], digits['target'], cv=5)
# )
# print(cross_val_score(
#     modelrf, digits['data'], digits['target'], cv=5)
# )

# rata2 score
print(
    np.mean(cross_val_score(
        modellr, digits['data'], digits['target'], cv=5))
)
print(
    np.mean(cross_val_score(
        modelsv, digits['data'], digits['target'], cv=5))
)
print(
    np.mean(cross_val_score(
        modelrf, digits['data'], digits['target'], cv=5))
)
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
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import cross_val_score
print(
    np.mean(cross_val_score(
        LogisticRegression(solver='lbfgs', multi_class='auto', max_iter=10000), 
        digits['data'], digits['target'], cv=5))
)
print(
    np.mean(cross_val_score(
        SVC(gamma='auto', probability=True), 
        digits['data'], digits['target'], cv=5))
)
print(
    np.mean(cross_val_score(
        RandomForestClassifier(n_estimators=40), 
        digits['data'], digits['target'], cv=5))
)
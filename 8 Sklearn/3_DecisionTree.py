import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

bacadata = pd.read_csv('3_Decision_Tree_Dataset.csv')
balance_data = pd.DataFrame({
    'result': bacadata['result'],
    'initial payment': bacadata['initial payment'],
    'last payment': bacadata['last payment'],
    'credit score': bacadata['credit score'],
    'house number': bacadata['house number']
})

print('Dataset Length:', len(balance_data))
print('Dataset Shape:', balance_data.shape)
print(balance_data.head())

# ========================================

# target vars
X = balance_data.values[:,1:5]
Y = balance_data.values[:,0]
print(X)
print(Y)

# split data into test & train
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=100)

# function to perform training w/ entropy
clf_entropy = DecisionTreeClassifier(
    criterion='entropy', 
    random_state=100,
    max_depth=3,
    min_samples_leaf=5
)
clf_entropy.fit(X_train, Y_train)

# =====================================

# func to create prediction
y_pred = clf_entropy.predict(X_test)
print(y_pred)

# check accuracy
print('Accuracy:', accuracy_score(Y_test, y_pred)*100)
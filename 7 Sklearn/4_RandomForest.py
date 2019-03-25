from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
np.random.seed(0)

iris = load_iris()
df = pd.DataFrame(iris['data'], columns=iris['feature_names'])
# print(df.head())

# ===================================

# tambah kolom baru: spesies
df['species'] = pd.Categorical.from_codes(
    iris['target'],
    iris['target_names']
)
df['is_train'] = np.random.uniform(0,1,len(df)) <= .75
# print(df)

# ===================================

train, test = df[df['is_train']==True], df[df['is_train']==False]
print('Jumlah observasi di training data:', len(train))
print('Jumlah observasi di test data:', len(test))

# ===================================

features = df.columns[:4]
print(features)

# convert nama spesies mjd digit angka
y = pd.factorize(train['species'])[0]
print(y)

# create random forest classifier
clf = RandomForestClassifier(n_jobs=2, random_state=0)
# training the classifier
clf.fit(train[features], y)

print(clf.predict(test[features]))

# ================================

# probability
print(clf.predict_proba(test[features])[0:10])
print(clf.predict_proba(test[features])[10:20])

# ================================

# show prediction
preds = iris['target_names'][clf.predict(test[features])]
print(preds[0:25])
# compare with original data
print(test['species'][0:25])

# ================================

# create confussion matrix

print(pd.crosstab(
    test['species'],
    preds,
    rownames=['Data asli'],
    colnames=['Prediksi']
))

# ================================

# tes prediksi
preds = iris['target_names'][clf.predict([[5,3,1,2]])]
print(preds)

preds = iris['target_names'][clf.predict([[5,3,1,2], [10,10,10,10]])]
print(preds)
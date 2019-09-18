import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
iris = load_iris()

# show data
# print(iris)

# show data columns
# print(iris['feature_names'])

# ========================================

# create dataframe
df = pd.DataFrame(iris['data'], columns=iris['feature_names'])
# print(df.head()) 

# tambahkan kolom 'target' => mencerminkan spesies
df['target'] = iris['target']
# print(df.head())

# target mencerminkan nama spesies di target_names
# print(iris['target_names'])

# tambahkan daftar spesies ke dataframe
df['spesies'] = df['target'].apply(lambda x: iris['target_names'][x])
# print(df)

# ========================================

# pisahkan df untuk setiap spesies
df0 = df[df['target'] == 0]     # setosa
df1 = df[df['target'] == 1]     # versicolor
df2 = df[df['target'] == 2]     # virginica

print(df0.head())
print(df1.head())
print(df2.head())

# =======================================
# plot data
fig = plt.figure('Iris Data', figsize=(14,7))

# plot data sepal length vs sepal width
plt.subplot(121)
plt.scatter(df0['sepal length (cm)'], df0['sepal width (cm)'], color='r', marker ='o')
plt.scatter(df1['sepal length (cm)'], df1['sepal width (cm)'], color='y', marker ='o')
plt.scatter(df2['sepal length (cm)'], df2['sepal width (cm)'], color='b', marker ='o')
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.title('Sepal width vs sepal length')
plt.legend(['0 Setosa', '1 Versicolor', '2 Virginica'])
plt.grid(True)

# plot data petal length vs petal width
plt.subplot(122)
plt.scatter(df0['petal length (cm)'], df0['petal width (cm)'], color='r', marker ='o')
plt.scatter(df1['petal length (cm)'], df1['petal width (cm)'], color='y', marker ='o')
plt.scatter(df2['petal length (cm)'], df2['petal width (cm)'], color='b', marker ='o')
plt.xlabel('petal length (cm)')
plt.ylabel('petal width (cm)')
plt.title('Petal width vs petal length')
plt.legend(['0 Setosa', '1 Versicolor', '2 Virginica'])
plt.grid(True)

# plt.show()

# ===========================================

# split dataset into test & train
from sklearn.model_selection import train_test_split
x = df.drop(['target', 'spesies'], axis='columns')  # data utama
y = df['target']                                    # data target

# train dataset dg test = 0.2
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2)

print(len(x_train))     # 120 = 80%
print(len(x_test))      #  30 = 20% (hasil dari test_size = .2)

# ============================================

# svm
from sklearn.svm import SVC
# model = SVC()
model = SVC(gamma='auto', probability=True)   # avoid warning

# train data
model.fit(x_train, y_train)

# akurasi
print(model.score(x_test, y_test))

# ===========================================

# prediksi
print(model.predict([[5.1, 3.5, 1.4, 0.2]]))    # output = [0] = spesies setosa
print(model.predict([[7.0, 3.2, 4.7, 1.4]]))    # output = [1] = spesies verticolor
print(model.predict([[5.9, 3.0, 5.1, 1.8]]))    # output = [2] = spesies virginica

# ===========================================
# plot svm

def make_meshgrid(x, y, h=.02):
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(
        np.arange(x_min, x_max, h),
        np.arange(y_min, y_max, h)
    )
    return xx, yy

def plot_contours(ax, clf, xx, yy, **params):
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out

iris = load_iris()
X = iris['data'][:, :2]
y = iris['target']

C = 1.0  # SVM regularization parameter
models = SVC(kernel='linear', C=C),SVC(gamma='auto'),SVC(kernel='rbf', gamma=0.7, C=C),SVC(kernel='poly', degree=3, C=C)

models = (clf.fit(X, y) for clf in models)

# title for the plots
titles = ('SVC with linear kernel',
          'LinearSVC (linear kernel)',
          'SVC with RBF kernel',
          'SVC with polynomial (degree 3) kernel')

# Set-up 2x2 grid for plotting.
fig, sub = plt.subplots(2, 2)
plt.subplots_adjust(wspace=0.4, hspace=0.4)

X0, X1 = X[:, 0], X[:, 1]
xx, yy = make_meshgrid(X0, X1)

for clf, title, ax in zip(models, titles, sub.flatten()):
    plot_contours(ax, clf, xx, yy,
                  cmap='coolwarm', alpha=0.8)
    ax.scatter(X0, X1, c=y, cmap='coolwarm', s=20, edgecolors='k')
    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    ax.set_xlabel('Sepal length')
    ax.set_ylabel('Sepal width')
    ax.set_xticks(())
    ax.set_yticks(())
    ax.set_title(title)

plt.show()
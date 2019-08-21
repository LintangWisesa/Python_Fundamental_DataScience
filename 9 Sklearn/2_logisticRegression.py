
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
from sklearn.linear_model import LogisticRegression

# ==============================================
# load digits datasets from sklearn
digits = load_digits()
print('Image Data Shape', digits['data'].shape)
print('Label Data Shape', digits['target'].shape)
print(digits['data'][0])

# ==============================================
# plot data
plt.figure(figsize=(20,4))
for index, (image, label) in enumerate(zip(digits['data'][0:5], digits['target'][0:5])):
    plt.subplot(1, 5, index+1)
    plt.imshow(np.reshape(image, (8,8)), cmap='gray')
    plt.title('Training: %i\n' % label, fontsize = 20)
plt.show()

# ==============================================
x_train, x_test, y_train, y_test = train_test_split(digits['data'], digits['target'], test_size=0.2, random_state=2)
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

# ==============================================
logReg = LogisticRegression()
logReg.fit(x_train, y_train)
print(logReg.predict(x_test[0].reshape(1, -1)))

logReg.predict(x_test[0:10])
predictions = logReg.predict(x_test)
score = logReg.score(x_test, y_test)
print(predictions)
print(score)

# ==============================================
cm = metrics.confusion_matrix(y_test, predictions)

plt.figure(figsize=(9,9))
sns.heatmap(cm, annot=True, fmt='.3f', linewidths=.5, square=True, cmap='Blues')
plt.ylabel('Actual Table')
plt.xlabel('Predicted Table')
all_sample_title = 'Accuracy Score: {0}'.format(score)
plt.title(all_sample_title, size=15)
plt.show()

# ===============================================
index = 0
classifiedIndex = []
for predict, actual in zip(predictions, y_test):
    if predict == actual:
        classifiedIndex.append(index)
    index += 1
plt.figure(figsize=(20,3))
for plotIndex, wrong in enumerate(classifiedIndex[0:4]):
    plt.subplot(1, 4, plotIndex+1)
    plt.imshow(np.reshape(x_test[wrong], (8,8)), cmap='gray')
    plt.title('Predicted: {}, Actual: {}'.format(predictions[wrong], y_test[wrong]), fontsize=20)
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
digits = load_digits()

# print(dir(digits))
# print(digits['data'])
# print(digits['images'])

# ====================================
# plot dataframe

# fig = plt.figure('Random Forest', figsize=(10,5))

# without loop:
# plt.subplot(2,5,1)
# plt.imshow(digits['images'][0])
# plt.subplot(2,5,2)
# plt.imshow(digits['images'][1])
# plt.subplot(2,5,3)
# plt.imshow(digits['images'][2])
# plt.subplot(2,5,4)
# plt.imshow(digits['images'][3])
# plt.subplot(2,5,5)
# plt.imshow(digits['images'][4])
# plt.subplot(2,5,6)
# plt.imshow(digits['images'][5])
# plt.subplot(2,5,7)
# plt.imshow(digits['images'][6])
# plt.subplot(2,5,8)
# plt.imshow(digits['images'][7])
# plt.subplot(2,5,9)
# plt.imshow(digits['images'][8])
# plt.subplot(2,5,10)
# plt.imshow(digits['images'][9])

# using loop:
# for i in range(10):
#     plt.subplot(2,5,i+1)
#     plt.imshow(digits['images'][i])
#     # plt.imshow(digits['images'][i], cmap='gray')
#     # plt.imshow(digits['images'][i], cmap='gray_r')

# plt.show()

# ======================================
# create dataframe

df = pd.DataFrame(digits['data'])
# create new column on df
df['target'] = digits['target']
# print(df)

# ======================================
# split dataset to train & test

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    df.drop(['target'], axis='columns'),
    digits['target'],
    test_size=.2
)

# print(len(x_train))
# print(len(y_train))
print(x_test)
# print(y_test)

# ===================================
# train model with random forest algorithm

from sklearn.ensemble import RandomForestClassifier
# model = RandomForestClassifier()
model = RandomForestClassifier(n_estimators=40)
model.fit(x_train, y_train)

# accuracy
print(model.score(x_train, y_train))

# new data to be predicted
newdata = [
     0.0,0.0,7.0,11.0,15.0,9.0,0.0,0.0,  
     0.0,0.0,15.0,15.0,4.0,11.0,4.0,0.0,  
     0.0,3.0,11.0,5.0,0.0,2.0,10.0,0.0,
     0.0,7.0,8.0,0.0,0.0,3.0,8.0,0.0, 
     0.0,6.0,8.0,0.0,0.0,4.0,8.0,0.0,  
     0.0,5.0,8.0,0.0,0.0,8.0,5.0,0.0, 
     0.0,1.0,12.0,2.0,1.0,13.0,0.0,0.0,  
     0.0,0.0,5.0,16.0,14.0,3.0,0.0,0.0,
]

# prediction
# y_prediction = model.predict(x_test)
y_prediction = model.predict([np.array(newdata)])
print(y_prediction)
# print(y_test)

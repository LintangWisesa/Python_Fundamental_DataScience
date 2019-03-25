# split datasets to training & test

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ferrari = [
    {'km':69000, 'umur':6, 'harga':18000},
    {'km':35000, 'umur':3, 'harga':34000},
    {'km':57000, 'umur':5, 'harga':26100},
    {'km':22500, 'umur':2, 'harga':40000},
    {'km':46000, 'umur':4, 'harga':31500},
    {'km':59000, 'umur':5, 'harga':26750},
    {'km':52000, 'umur':5, 'harga':32000},
    {'km':72000, 'umur':6, 'harga':19300},
    {'km':91000, 'umur':8, 'harga':12000},
    {'km':67000, 'umur':6, 'harga':22000},
    {'km':83000, 'umur':7, 'harga':18700},
    {'km':79000, 'umur':7, 'harga':19500},
    {'km':59000, 'umur':5, 'harga':26000},
    {'km':58780, 'umur':4, 'harga':27500},
    {'km':82450, 'umur':7, 'harga':19400},
    {'km':25400, 'umur':3, 'harga':35000},
    {'km':28000, 'umur':2, 'harga':35500},
    {'km':69000, 'umur':5, 'harga':19700},
    {'km':87600, 'umur':8, 'harga':12800},
    {'km':52000, 'umur':5, 'harga':28200}
]

df = pd.DataFrame(ferrari)

# plt.scatter(df['km'], df['harga'], color='r')
# plt.scatter(df['umur'], df['harga'], color='g')
# plt.show()

# ==================================

x = df[['km', 'umur']]
y = df['harga']

from sklearn.model_selection import train_test_split

# test = 20% & training = 80%
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=.2)
# x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=.8)
# x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=.2,random_state=10)

# print(len(x_train)) # 80%
# print(len(x_test))  # 20%
# print(x_train)

# ======================================

from sklearn.linear_model import LinearRegression
model = LinearRegression()

# data training
model.fit(x_train, y_train)
# prediksi data test
print(model.predict(x_test))
# cek akurasi
print(model.score(x_test, y_test))
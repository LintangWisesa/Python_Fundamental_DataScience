
import pandas as pd 
import numpy as np 

x = {'a':0, 'b':1, 'c':5, 'd':5, 'f':4, 'g':5}
xs = pd.Series(data=x, name='ID')

# data view
print(xs.shape)
print(xs.values.tolist())
print(xs.index.tolist())
print(xs.describe())
print(xs.describe()['std'])
print(xs.describe()['50%'])

# max min
print(xs.max())
print(xs.min())

# mean median mode
print(xs.mean())
print(xs.median())
print(xs.mode())
print(xs.mode()[0])
print(xs.std())

# mode & its freq
print(xs[xs == 5])
print(xs[xs == xs.mode()[0]])
print(xs[xs == xs.mode()[0]].count())

# series to list, find mode & its freq
xl = list(xs)
# xl = xs.tolist()
xl = list(filter(lambda i: i == xs.mode()[0], xl))
print(xl)
print(len(xl))

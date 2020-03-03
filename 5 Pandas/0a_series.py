
# Creating a Series by passing a list of values, 
# letting pandas create a default integer index:
# pip install pandas

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

x = pd.Series([1,3,5,np.nan,6,8])
print(x)
print(x[0])
print(x[0:6:2])

y = ['Andi', 'Budi', 'Caca', 'Deni', 'Euis']
z = pd.Series(y, index = ['a','b','c','d','e'])
print(z)
print(type(z))
print(z['a'])

# y = ['Andi', 'Budi', 'Caca', 'Deni', 'Euis']
# z = pd.Series(y, index = ['a','b','c','d','e'], name='Data')
# print(z)
# print(z['a'])

# =============================================

x = {'a':0, 'b':1, 'c':2, 'd':3, 'f':4, 'g':5}
xs = pd.Series(x)   # series from dict
print(xs)

a = [9,2,5,3,4]
b = pd.Series(
    data = {'a': 2, 'b': 3},    # from dict
    # data = 23                 # from scalar value
    name = 'Test'
)
print(b)
print(b.name)

plt.plot(x, x)
plt.show()
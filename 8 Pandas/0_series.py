
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
print(z['a'])

# y = ['Andi', 'Budi', 'Caca', 'Deni', 'Euis']
# z = pd.Series(y, index = ['a','b','c','d','e'], name='Data')
# print(z)
# print(z['a'])

plt.plot(x, x)
plt.show()
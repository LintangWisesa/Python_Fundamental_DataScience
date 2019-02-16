
# Creating a Series by passing a list of values, 
# letting pandas create a default integer index:

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])

print(s)
print(s[0])
print(s[0:6:2])
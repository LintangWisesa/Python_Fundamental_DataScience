
import pandas as pd 
import numpy as np 

x = [1,2,3,4,5]
x = pd.Series(x, name='Test')
df = pd.DataFrame(x)
print(df)

# =============================

x = [1,2,3,4,5]
x = pd.Series(x, name='Test')
y = [1,2,3,4,5]
y = pd.Series(y, name='Try')
df = pd.DataFrame({
    x.name : x,
    y.name : y
})
print(df)
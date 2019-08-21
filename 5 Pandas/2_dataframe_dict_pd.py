# DF dgn dict akan membentuk df per KOLOM
import pandas as pd 
import numpy as np 

# Creating a DataFrame by passing a dict of objects 
# that can be converted to series-like.

df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo' })

print(df2)
print(df2.dtypes)
print(df2.shape)
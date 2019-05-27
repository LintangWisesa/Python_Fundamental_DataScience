import pandas as pd 
import numpy as np

# =============================
# timestamp
# =============================

df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo' })

# print(df2)
# print(df2.dtypes)
# print(df2.shape)

# =============================
# date range
# =============================

dates = pd.date_range('20130101', periods=6)
print(dates)

df = pd.DataFrame(
    np.random.randn(6,4), 
    index = dates,
    columns = list('ABCD')
)
print(df)
print(df.shape)

baris, kolom = df.shape
print(baris)

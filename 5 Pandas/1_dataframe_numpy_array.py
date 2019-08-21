# DF dgn list akan membentuk df per DATA BARIS
import pandas as pd 
import numpy as np

# Creating a DataFrame by passing a NumPy array, 
# with a datetime index and labeled columns:

dates = pd.date_range('20130101', periods=6)
print(dates)
# print(dates[0])
# print(dates[1])
# print(dates[2])

df = pd.DataFrame(
    np.random.randn(6,4), 
    index = dates,
    columns = list('ABCD')
)
print(df)
print(df.shape)

baris, kolom = df.shape
print(baris)

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

# print(df)

# print(df.head(2))
# print(df.tail(2))
# print(df.index)

# print(df.columns)
# print(df.values)
# print(df.describe())

# print(df.T) # transposing data

# print(df.sort_index(axis=1, ascending=False))
# print(df.sort_values(by='B'))
# print(df.sort_values(by='B', ascending=False))



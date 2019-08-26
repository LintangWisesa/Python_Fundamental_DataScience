import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

# print(df)

# print(df.head(2))
# print(df.tail(2))
# print(list(df.index))
# print(list(df.columns))

# print(df.values)      # it will return a numpy array!
# print(df.describe())

# print(df.sort_index(axis=1, ascending=False))
# print(df.sort_values(by='B'))
# print(df.sort_values(by='B', ascending=False))
# print(df.sort_values(by=['B', 'A'], ascending=False))
# print(df.sort_values(by=['B', 'A'], ascending=[False, True]))

# df = df.set_index('kolom1')           
# atau bisa pakai inplace=True
# df.set_index('kolom1', inplace=True)
# print(df)

# print(df['A'])
# print(df[['A', 'B']])
# print(df[0:3])
# print(df[0:5:2])

# loc = memanggil baris/kol dg NAMA indexnya!
# ================================================= 

# print(df.loc[0])
# print(df.loc[0:3])
# print(df.loc[0:3, ['A', 'B']])

# print(df.loc[dates[0]])
# print(df.loc[:,['A','B']])
# print(df.loc['20130102':'20130104',['A','B']])

# iloc = memanggil baris/kol dg urutan index, harus INTEGER
# =================================================

# print(df.iloc[3])
# print(df.iloc[3:5,0:2])
# print(df.iloc[[1,2,4],[0,2]])
# print(df.iloc[1:3,:])
# print(df.iloc[:,1:3])
# print(df.iloc[1,1])

# manggil value dg nama index & nama kolom
# print(df.at[dates[0],'A'])

# manggil value dg urutan index & urutan kolom
# print(df.iat[1,1])

# print(df.T) # transposing data
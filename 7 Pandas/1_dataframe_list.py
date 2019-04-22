
import pandas as pd 
import numpy as np 

x = [1,3,5,7,9,11,13,15,17,19]

df = pd.DataFrame(x, columns = ['Nilai'])
print(df)
print(df.shape)

baris, kolom = df.shape
print(baris)

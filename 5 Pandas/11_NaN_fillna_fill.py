
import pandas as pd 

df = pd.read_csv('10_data_NaN.csv', na_values=['-', 'n.a', 'not available'])

# dg method forward filling, nilai data NaN akan mjd = data di sel sebelumnya
# df2 = df.fillna(method = 'ffill', axis = 'columns')
df2 = df.fillna(method = 'ffill', axis = 'index')
print(df2)

# method: 'bfill' => data NaN akan = nilai setelanya
# axis: 0 atau axis: 'index'
# axis: 1 atau axis: 'columns'
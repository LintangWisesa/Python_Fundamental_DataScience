
import pandas as pd 

df = pd.read_csv('10_data_NaN.csv', na_values=['-', 'n.a', 'not available'])

# check data which is null: true/false
df.isnull()
print(df)

# check how many null data on every col
df.isnull().sum()
print(df)
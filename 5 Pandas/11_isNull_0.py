
import pandas as pd 

df = pd.read_csv('10_data_NaN.csv', na_values=['-', 'n.a', 'not available'])

# check data which is null: true/false
print(df.isnull())

# check how many null data on every col
print(df.isnull().sum())

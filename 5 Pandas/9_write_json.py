
import pandas as pd 

df = pd.read_csv('5_datarokok.csv')

print(df)

df.to_json('9_new.json', orient='index')
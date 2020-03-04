
import pandas as pd 

df = pd.read_csv('5_datarokok.csv')

print(df)

df.to_json('9a.json', orient = 'records')
# df.to_json('9b.json', orient='index')     # default orient: index
# orient = records, values, index, table, columns
# require openpyxl: pip install openpyxl

import pandas as pd 

df = pd.read_csv('5_datarokok.csv')

print(df)

df.to_excel('9_new.xlsx', sheet_name = 'Data perokok', index = False)
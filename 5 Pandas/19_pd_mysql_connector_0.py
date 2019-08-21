# pip install mysql-connector-python
import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="lintang",
  passwd="12345",
  database="tes_flask"
)

# query = 'select * from dataku'
query = '''
select * from dataku
'''

df = pd.read_sql(query, con=mydb)
print(df)
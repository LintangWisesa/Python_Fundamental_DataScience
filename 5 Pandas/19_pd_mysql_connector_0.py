# pip install mysql-connector-python
import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="lintang",
  passwd="12345",
  database="pandas_tes"
)

# query = 'select * from dataku'
query = '''
select * from employees
'''

# df = pd.read_sql(query, mydb)
# df = pd.read_sql(query, con=mydb)
# print(df)

# =======================
# using mysqlclient & db url
# pip install mysqlclient
# conda install -c anaconda mysqlclient
df = pd.read_sql(query, "mysql://lintang:12345@localhost:3306/pandas_tes")
print(df)
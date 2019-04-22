# pip install pymysql
# pip install sqlalchemy

import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:pass@localhost:3306/database')

df = pd.read_sql_table('namatabel', engine)
# df = pd.read_sql_table('namatabel', engine, columns=['kolom1'])

print(df)
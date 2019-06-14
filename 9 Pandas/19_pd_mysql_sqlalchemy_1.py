# pd.read_sql_query

import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:pass@localhost:3306/database')

query = '''
select * from data
'''
df = pd.read_sql_query(query, engine)
print(df)
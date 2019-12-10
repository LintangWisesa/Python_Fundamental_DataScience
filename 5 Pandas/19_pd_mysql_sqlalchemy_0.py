# pd.read_sql

import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:pass@localhost:3306/database')

query = '''
select * from data
'''

df = pd.read_sql('namatabel', engine)
df = pd.read_sql(query, engine)
# on MAC
# df = pd.read_sql(query, engine.raw_connection())
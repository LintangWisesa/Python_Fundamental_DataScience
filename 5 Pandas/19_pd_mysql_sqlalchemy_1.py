# pd.read_sql_query()

# pip install sqlalchemy
# conda install -c anaconda sqlalchemy

import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:pass@localhost:3306/database')

query = '''
select * from data where id % 2 = 0
'''
df = pd.read_sql_query(sqlalchemy.text(query), engine)
print(df)

query = '''
select * from data where id %% 2 = 0
'''
df = pd.read_sql_query(query, engine)
print(df)

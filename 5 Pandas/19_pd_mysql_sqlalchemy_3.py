# write from csv to mysql

import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:pass@localhost:3306/database')

df = pd.read_csv('namafile.csv')
print(df)

df.rename(columns={
    'kolom1_csv': 'kolom1_mysql',
    'kolom2_csv': 'kolom2_mysql',
}, inplace=True)
print(df)

df.to_sql(
    name = 'nama_mysql_tabel',  # name must be lowercase
    con = engine,
    index = False,
    if_exists = 'append'    # fail, replace, append
)
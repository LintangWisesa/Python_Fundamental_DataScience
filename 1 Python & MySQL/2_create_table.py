import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="lintang",
  passwd="12345",
  database="py_mysql"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE users (nama VARCHAR(255), usia VARCHAR(255))")

# untuk memudahkan gunakan ''' string
# querydb = '''create table huhu(
#     id int,
#     nama text,
#     usia smallint
# )'''
# mycursor.execute(querydb)

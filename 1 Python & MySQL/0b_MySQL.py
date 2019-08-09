# pip install MySQL-connector-python

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port = 3306,  # not necessary
  user="lintang",
  passwd="12345",
  host = 'localhost',
  auth_plugin = 'mysql_native_password' # if authentication plugin 'caching_sha2_password' is not supported
)
print(mydb)

kursor = mydb.cursor()
kursor.execute('show databases')
print(kursor.fetchall())

alldb = []
for db in kursor.fetchall():
    alldb.append(db[0])
print(alldb)

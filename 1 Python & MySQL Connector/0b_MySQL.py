# pip install MySQL-connector-python

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port = 3306,  # not necessary
  user="lintang",
  passwd="12345",
  use_pure = True, # if SSL error. default False for v8++ MySQL & True for earlier MySQL
  auth_plugin = 'mysql_native_password' # if authentication plugin 'caching_sha2_password' is not supported
                                        # on mysql do this => alter user 'root'@'localhost' identified with mysql_native_password by 'password';
)
print(mydb)

kursor = mydb.cursor()
kursor.execute('show databases')

#1 get all db names
print(kursor.fetchall())
#2 get all db names
print(list(kursor))
#3 get all db names
alldb = []
for db in kursor.fetchall():
    alldb.append(db[0])
print(alldb)

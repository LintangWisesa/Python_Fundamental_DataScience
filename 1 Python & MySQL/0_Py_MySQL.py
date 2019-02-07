# pip install MySQL-connector-python

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="lintang",
  passwd="12345"
)
print(mydb)

kursor = mydb.cursor()
kursor.execute('show databases')
print(kursor.fetchall())

alldata = kursor.fetchall()
for i in range(0, len(alldata) - 1):
    print(alldata[i][0])

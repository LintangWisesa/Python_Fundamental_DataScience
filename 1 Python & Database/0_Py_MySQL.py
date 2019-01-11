# pip install MySQL-connector-python

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="lintang",
  passwd="12345"
)

print(mydb)

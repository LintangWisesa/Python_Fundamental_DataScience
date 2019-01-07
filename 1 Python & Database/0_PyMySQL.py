# pip install mysql-connector

import mysql.connector

db = mysql.connector.connect(
  host = "localhost",
  user = "lintang",
  passwd = "12345"
)

print(db)
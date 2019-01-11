import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="lintang",
  passwd="12345"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE py_mysql")


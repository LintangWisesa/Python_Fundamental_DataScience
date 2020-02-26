import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="lintang",
  passwd="12345"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE doraemon")
mycursor.execute("use doraemon")
mycursor.execute('create table karyawan(no int, nama varchar(100))')

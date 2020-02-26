import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="lintang",
  passwd="12345"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE doraemon")

# drop then show all db
# mycursor.execute('drop database doraemon')
# mycursor.execute('show databases')

# alldb = []
# for db in kursor.fetchall():
#     alldb.append(db[0])
# print(alldb)
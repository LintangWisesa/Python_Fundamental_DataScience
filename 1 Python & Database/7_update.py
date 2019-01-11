import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="lintang",
  passwd="12345",
  database="py_mysql"
)

mycursor = mydb.cursor()

sql = "UPDATE users SET nama = %s WHERE nama = %s"
nama = ('Bambang', 'Budi')
mycursor.execute(sql, nama)

mydb.commit()

print(mycursor.rowcount, "Data terupdate!")
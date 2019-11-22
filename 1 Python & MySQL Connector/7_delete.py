import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="lintang",
  passwd="12345",
  database="py_mysql"
)

mycursor = mydb.cursor()

sql = "DELETE FROM users WHERE nama = %s"
nama = ('Deni', )
mycursor.execute(sql, nama)

mydb.commit()

print(mycursor.rowcount, "Data terhapus!")
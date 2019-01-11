import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="lintang",
  passwd="12345",
  database="py_mysql"
)

mycursor = mydb.cursor()
sql = "INSERT INTO users (nama, usia) VALUES (%s, %s)"
val = ("Andi", "22")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "Data tersimpan!")

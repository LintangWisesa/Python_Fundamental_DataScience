import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="lintang",
  passwd="12345",
  database="py_mysql"
)

mycursor = mydb.cursor()
sql = "INSERT INTO users (nama, usia) VALUES (%s, %s)"
val = [
  ("Budi", "23"),
  ("Caca", "24"),
  ("Deni", "25"),
  ("Euis", "26"),
  ("Fafa", "27")
]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "Data tersimpan!")

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="lintang",
  passwd="12345",
  database="datascience"
)

mycursor = mydb.cursor(dictionary=True)

mycursor.execute("SELECT * FROM users")
myresult = mycursor.fetchall()

print(list(myresult))

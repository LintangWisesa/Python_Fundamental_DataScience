import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="lintang",
  passwd="12345",
  database="datascience"
)

mycursor = mydb.cursor()

mycursor.execute("describe users")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

print(kursor.fetchall())
print(kursor.fetchone())
print(kursor.fetchmany(2))
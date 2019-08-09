import pymysql

con = pymysql.connect(
    host='localhost',
    user='lintang',
    password='12345',
    db='doraemon',
)

kursor = con.cursor()
kursor.execute('select * from karakter')
# print(kursor.fetchall())

kolom = kursor.description
print(kolom)

for i in kursor.fetchall():
    print(i)
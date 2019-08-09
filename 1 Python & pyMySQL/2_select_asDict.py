import pymysql

con = pymysql.connect(
    host='localhost',
    user='lintang',
    password='12345',
    db='doraemon',
    cursorclass=pymysql.cursors.DictCursor
)

kursor = con.cursor()
kursor.execute('select * from karakter')
# print(kursor.fetchall())

for i in kursor.fetchall():
    print(i)
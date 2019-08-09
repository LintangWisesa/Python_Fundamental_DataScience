import pymysql

con = pymysql.connect(
    host='localhost',
    user='lintang',
    password='12345',
    db='doraemon',
    cursorclass=pymysql.cursors.DictCursor
)

kursor = con.cursor()
idCari = 2
queryDb = '''select * from karakter where id=%s'''
kursor.execute(queryDb, idCari)

print(kursor.fetchone())
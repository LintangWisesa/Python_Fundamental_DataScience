import pymysql

con = pymysql.connect(
    host='localhost',
    user='lintang',
    password='12345',
    db='doraemon',
    cursorclass=pymysql.cursors.DictCursor
)

kursor = con.cursor()
sql = '''delete from karakter
where nama = %s'''
val = ("Nobisuke")
kursor.execute(sql, val)

con.commit()
print(kursor.rowcount, "Data terhapus!")
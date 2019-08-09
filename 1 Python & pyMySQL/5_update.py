import pymysql

con = pymysql.connect(
    host='localhost',
    user='lintang',
    password='12345',
    db='doraemon',
    cursorclass=pymysql.cursors.DictCursor
)

kursor = con.cursor()
sql = '''update karakter set nama = 'Giant'
where nama = %s'''
val = ("Goda Takeshi")
kursor.execute(sql, val)

con.commit()
print(kursor.rowcount, "Data terupdate!")
import pymysql

con = pymysql.connect(
    host='localhost',
    user='lintang',
    password='12345',
    db='doraemon',
    cursorclass=pymysql.cursors.DictCursor
)

kursor = con.cursor()
sql = '''insert into karakter (nama, usia) 
values (%s, %s)'''
val = ("Nobisuke", "8")
kursor.execute(sql, val)

con.commit()
print(kursor.rowcount, "Data tersimpan!")
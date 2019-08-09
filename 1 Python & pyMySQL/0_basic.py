# pip install pymysql
# pip3 install pymysql
# py -m pip install pymysql

import pymysql

con = pymysql.connect(
    host='localhost',
    user='lintang',
    password='12345',
)
# print(con)

kursor = con.cursor()
kursor.execute('show databases')
# print(kursor.fetchall())

for i in kursor.fetchall():
    print(i)

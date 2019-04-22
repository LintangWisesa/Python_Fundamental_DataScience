# activate MySQL server
# create a database called 'lin_flask'
# create a table called 'users' with 2 col: name & age

# install flask-mysqldb: $ pip install flask-mysqldb

from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'lintang'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'lin_flask'

mysql = MySQL(app)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO users VALUES(%s, %s)', ('Budi', 23))
        mysql.connection.commit()
        cursor.close()
        return jsonify({'status': 'Data posted to MySQL!'})
    else:
        cursor = mysql.connection.cursor()
        data = cursor.execute('SELECT * FROM USERS')
        if data > 0:
            users = cursor.fetchall()
            print (users)
            return jsonify(users)

# try to POST to /data then see on mysql: select * from users

if __name__ == '__main__':
    app.run(debug = True)

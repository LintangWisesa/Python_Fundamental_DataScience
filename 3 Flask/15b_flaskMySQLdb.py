# install flask-mysqldb: $ pip install flask-mysqldb
# install pyyaml: $ pip install pyyaml

from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

db = yaml.load(open('15_mysql.yaml'))
app.config['MYSQL_HOST'] = db['host']
app.config['MYSQL_USER'] = db['user']
app.config['MYSQL_PASSWORD'] = db['pass']
app.config['MYSQL_DB'] = db['db']

mysql = MySQL(app)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO users VALUES(%s, %s)', ('Euis', 25))
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

if __name__ == '__main__':
    app.run(debug = True)

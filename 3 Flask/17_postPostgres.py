# activate PostgreSQL server
# create a database: create database lin_flask
# create a table called users:
# $ create table users (id serial primary key, email varchar(255));

# install psycopg2: $ pip install psycopg2
# install SQLAlchemy: $ pip install Flask-SQLAlchemy

# Ignore error by pylint, just run it!

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/lin_flask'
db = SQLAlchemy(app)

# Create our database model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    
    def __init__(self, email):
        self.email = email
    
    def __repr__(self):
        return '<E-mail %r>' % self.email

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/data', methods=['POST'])
def data():

    if request.method == 'POST':
        body = request.json
        print(body['email'])
        if not db.session.query(User).filter(User.email == body['email']).count():
            reg = User(body['email'])
            db.session.add(reg)
            db.session.commit()
            return 'sukses!'
    return render_template('home.html')

if __name__ == '__main__':
    app.debug = True
    app.run()

# Try to post to /data via postman 
# with body message: { "email": "haha@hihi.com" }
# then on postgres: select * from users;
# the data is posted successfully!
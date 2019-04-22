from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1><i>Welcome to my server!</i></h1>'

if __name__ == '__main__':
    app.run()

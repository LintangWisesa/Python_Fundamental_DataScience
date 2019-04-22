from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Lintang\'s server!'

if __name__ == '__main__':
    app.run(debug = True)
    # automatically restart when there is a change
    # app.run(host, port, debug, options)

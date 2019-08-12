# install flask first: pip install flask
# check flask version: flask --version
# running on MacOS: $ FLASK_APP=fileName.py flask run

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run()

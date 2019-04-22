# install flask-cors: $ pip install flask-cors

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('home.html')

# try to get/post/put/delete to /data from your front-end project!
@app.route('/data', methods=['GET', 'POST', 'PUT', 'DELETE'])
def data():
    if request.method == 'POST':
        return jsonify({'status': 'You\'re POST-ing'})
    elif request.method == 'GET':
        return jsonify({'status': 'You\'re GET-ing'})
    elif request.method == 'PUT':
        return jsonify({'status': 'You\'re PUT-ing'})
    else:
        return jsonify({'status': 'You\'re DELETE-ing'})

if __name__ == '__main__':
    app.run(debug = True)

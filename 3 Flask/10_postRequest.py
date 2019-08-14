from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        body = request.json

        print(body['name'])
        print(body['age'])
        # body json :
        # {"name":"lintang", "age":22}

        return jsonify({
            'name': body['name'],
            'age': body['age']
        })
    else:
        return jsonify({'status': 'You\'re GET-ing'})

if __name__ == '__main__':
    app.run(debug = True)

# try to POST to /data with body request:
# {
#   "name": "Andi",
#   "age": 21
# }
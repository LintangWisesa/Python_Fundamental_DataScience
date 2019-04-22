from flask import abort, Flask, jsonify, render_template

app = Flask(__name__)

Students = [
    {
        'id': 1,
        'name': 'Andi',
        'age': 21
    },
    {
        'id': 2,
        'name': 'Budi',
        'age': 22
    },
    {
        'id': 1,
        'name': 'Caca',
        'age': 23
    }
]

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/data', methods=['GET'])
def data():
    return jsonify({'students': Students})

# create a dynamic route /data/something int
@app.route('/data/<int:id>')
def datas(id):
    if id < 1 or id > len(Students):
        abort(404)
    else:
        return jsonify(Students[id-1])

if __name__ == '__main__':
    app.run(debug = True)

from flask import make_response, abort, Flask, jsonify, render_template

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

@app.route('/data/<int:id>')
def datas(id):
    if id-1 > len(Students)-1:
        abort(404)
    else:
        return jsonify(Students[id-1])

@app.errorhandler(404)
def not_found(error):
    # return '<h1>Maaf not found!</h1>'
    # return make_response('<h1>Maaf not found!</h1>')
    return make_response(jsonify({'status': 'Error Not Found'}), 404)
    # return make_response(
    #     render_template('error.html')
    # )

if __name__ == '__main__':
    app.run(debug = True)

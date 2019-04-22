from flask import abort, Flask, jsonify, request, render_template

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
    if 'id' in request.args:
        id = int(request.args['id'])
        print(request.args)
        return jsonify(Students[id])
    else:
        return jsonify({'error': 'No id field provided on URL'})
    
if __name__ == '__main__':
    app.run(debug = True)

# try to GET:
# localhost:5000/data?id=1
# localhost:5000/data?id=2

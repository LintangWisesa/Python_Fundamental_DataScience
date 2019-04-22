from flask import Flask, jsonify, render_template

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

@app.route('/data')
def data():
    return jsonify(Students)
    
# create a dynamic route /data/something string
@app.route('/data/<string:id>')
def datas(id):
    return jsonify(Students[int(id)])

if __name__ == '__main__':
    app.run(debug = True)

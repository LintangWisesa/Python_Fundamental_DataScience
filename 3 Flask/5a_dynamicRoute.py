from flask import Flask, jsonify, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')
    
# create a dynamic route /data/something string
@app.route('/data/<string:nama>')
def datas(nama):
    return 'Halo %s!' % nama

if __name__ == '__main__':
    app.run(debug = True)

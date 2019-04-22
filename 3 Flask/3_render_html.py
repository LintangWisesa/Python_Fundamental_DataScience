from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')
    # render html file from templates dir

@app.route('/about')
def about():
    return render_template('about.html')
    # render html file from templates dir

if __name__ == '__main__':
    app.run(debug = True)

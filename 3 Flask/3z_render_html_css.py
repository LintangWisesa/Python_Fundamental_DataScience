from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')
    # render html file from templates dir

@app.route('/about')
def about():
    return render_template('aboutVarCss.html')
    # render html file from templates dir
    # html with css file on 'static' dir! dir name must be 'static'!
    # will be able to access all files inside static dir, just go to
    # http://host:port/static/filename.extension 

if __name__ == '__main__':
    app.run(debug = True)

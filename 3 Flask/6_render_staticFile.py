from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return render_template('home.html')
    # render html file from templates dir

# go to => localhost:5000/file/lintang.png
@app.route('/file/<path:path>')
def staticfile(path):
    return send_from_directory('file', path)

if __name__ == '__main__':
    app.run(debug = True)

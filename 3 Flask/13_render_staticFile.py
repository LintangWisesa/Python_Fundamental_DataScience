from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return render_template('home.html')
    # render html file from templates dir

# go to => localhost:5000/fileku/1.png
# go to => localhost:5000/fileku/foto/lintang2.mp4
@app.route('/fileku/<path:x>')
def staticfile(x):
    return send_from_directory('file', x)

if __name__ == '__main__':
    app.run(debug = True)

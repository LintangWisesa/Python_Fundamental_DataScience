from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return redirect('/')
    # try to GET /home & it will redirect to /
    
@app.route('/about')
def about():
    return render_template('about.html')
    
if __name__ == '__main__':
    app.run(debug = True)

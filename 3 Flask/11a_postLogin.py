from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('login.html')

@app.route('/success/<name>')
def success(name):
   return 'You\'re logged in successfully,  %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['username']
      return redirect(url_for('success', name = user))
   else:
      user = request.args.get('username')
      return redirect(url_for('success', name = user))

if __name__ == '__main__':
   app.run(debug = True)
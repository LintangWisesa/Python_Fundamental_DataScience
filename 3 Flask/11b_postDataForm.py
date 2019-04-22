from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def formulir():
   return render_template('dataform.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print(result)  
      # ImmutableMultiDict([('Name', 'Andi'), ('Physics', '90'), ('chemistry', '100'), ('Mathematics', '90')])
      return render_template("dataresult.html", result = result)

if __name__ == '__main__':
   app.run(debug = True)
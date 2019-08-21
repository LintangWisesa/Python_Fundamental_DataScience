from sklearn.externals import joblib
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def score():
   return '<h1>Prediksi 3300 = ' + str(model.predict([[3300]])) + '</h1>'

if __name__ == '__main__':
   model = joblib.load('9_saveModel_joblib')
   app.run(debug = True)

# run & open localhost:5000/ via browser
# it will print the prediction! 
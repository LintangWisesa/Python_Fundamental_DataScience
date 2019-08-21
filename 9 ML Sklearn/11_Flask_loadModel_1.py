from sklearn.externals import joblib
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

def init():
    global model
    model = joblib.load('9_saveModel_joblib')

@app.route('/')
def score():
   return '<h1>Prediksi 1000 = ' + str(model.predict([[1000]])) + '</h1>'

if __name__ == '__main__':
   init()
   app.run(debug = True)

# run & open localhost:5000/ via browser
# it will print the prediction! 
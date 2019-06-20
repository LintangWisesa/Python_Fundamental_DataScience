# load model with joblib

# from sklearn.externals import joblib
import joplib   # $ pip install joblib

model = joblib.load('9_saveModel_joblib')

# ==================================
# prediksi harga dari luas tanah

print(model.predict([[3300]]))
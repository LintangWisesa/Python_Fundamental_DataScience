# load model

import pickle

with open('7_savedModel', 'rb') as modelku:
    model = pickle.load(modelku)

# show prediksi harga tanah berdasarkan luas, dg model yg diload:
print(model.predict([[3300]]))
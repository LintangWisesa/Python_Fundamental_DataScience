import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces

# ===============================
# load data
dataOF = fetch_olivetti_faces()
# print(dir(dataOF))
print(dataOF.data[0])  # 4096

# ===============================
# plot a face
# dataOF.images[0]   # 64 x 64
plt.imshow(dataOF.images[101], cmap='gray')
# plt.show()

# ===============================
# plot face of people number-x
fig = plt.figure('Wajah Orang')
for i in range(10):
    orangke = 14
    plt.subplot(2, 5, i+1)
    plt.imshow(dataOF.images[i + (10 * (orangke - 1))], cmap='gray')

plt.show()
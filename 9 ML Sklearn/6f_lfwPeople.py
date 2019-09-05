import numpy as np
import pandas as pd
from sklearn.datasets import fetch_lfw_people
import matplotlib.pyplot as plt

# =====================================
# load data
dataP = fetch_lfw_people(min_faces_per_person=70, resize=.5)
# print(dir(dataP))
# print(dataP.data[0].shape)
# print(dataP.images[1].shape)
# print(dataP.target[2])
# print(dataP.target_names)

# =====================================
# plot a face
plt.imshow(dataP.images[2], cmap='gray')

# =====================================
# plot 10 first face with its name
for i in range(10):
    plt.subplot(2, 5, i+1)
    plt.imshow(dataP.images[i], cmap='gray')
    plt.title(dataP.target_names[dataP.target[i]].split()[-1])

plt.show()
import numpy as np
import pandas as pd
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

dataDg = load_digits()
# print(dir(dataDg))
# print(dataDg['data'][0])

for i in range(10): 
    plt.subplot(2, 5, i+1)
    plt.imshow(dataDg['images'][i], cmap='gray')
    plt.title('Ini {}'.format(dataDg['target'][i]))
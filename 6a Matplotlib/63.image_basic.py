import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# recommended: png
img = mpimg.imread('63.png')
print(img)
print(img.ndim)
print(img.shape)
print(len(img))
print(len(img[0]))

imgplot = plt.imshow(img)

plt.show()
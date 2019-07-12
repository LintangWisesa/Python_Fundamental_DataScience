# 1 install cmake (dlib is built with c++): 
#       $ pip install cmake 
# 2 download dlib 
#       a. download dlib from: https://pypi.org/simple/dlib/
#       b. extract it & name its folder with just 'dlib'
#       c. cut & paste on C:/Python37/Lib/site-packages
# $ pip install imageio
import imageio
# from PIL import Image

import matplotlib.pyplot as plt
from mlxtend.image import extract_face_landmarks

img = imageio.imread('jokowi.jpg')
# img = Image.open('jokowi.jpg').convert('L')

landmarks = extract_face_landmarks(img)
print(landmarks.shape)
print('\n\nFirst 10 landmarks:\n', landmarks[:10])

fig = plt.figure(figsize=(15, 5))
ax = fig.add_subplot(1, 3, 1)
ax.imshow(img)
ax = fig.add_subplot(1, 3, 2)
ax.scatter(landmarks[:, 0], -landmarks[:, 1], alpha=0.8)
ax = fig.add_subplot(1, 3, 3)
img2 = img.copy()
for p in landmarks:
    img2[p[1]-3:p[1]+3,p[0]-3:p[0]+3,:] = (255, 255, 255)
ax.imshow(img2)
plt.show()
# pip install pillow

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import requests
from io import BytesIO

url_image = 'https://upload.wikimedia.org/wikipedia/en/thumb/d/d8/Captain_Tsubasa_%28キャプテン翼%29_first_edition_%28manga_1981%29.jpg/220px-Captain_Tsubasa_%28キャプテン翼%29_first_edition_%28manga_1981%29.jpg'
response = requests.get(url_image)
print(BytesIO(response.content))
gambar = Image.open(BytesIO(response.content)).convert('L')

# convert 0.png (388px x 388px) to array
arrayGambar = np.array(gambar)
print(arrayGambar)

### show result as image with matplotlib
plt.imshow(arrayGambar, cmap='gray')
plt.show()

### show result as image with pillow
# hasil = Image.fromarray(arrayGambar, 'L')
# hasil.show()

### save as image
# hasil.save('result.png')
# hasil.save('result.jpg')
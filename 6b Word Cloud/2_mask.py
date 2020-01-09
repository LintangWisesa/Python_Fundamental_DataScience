# pip install wordcloud

import numpy as np
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam vulputate turpis eros, quis tristique elit ultrices sed. Pellentesque commodo leo a molestie viverra. Nunc nisl libero, dictum vel dolor ut, rutrum ultricies nisi. Donec pretium sagittis mauris non suscipit. Quisque tincidunt sagittis dui non elementum. Sed nec erat quis massa dictum pulvinar. Aliquam at euismod mi, eget hendrerit tortor. Quisque a ultricies ante, non mattis sem. Pellentesque sollicitudin feugiat hendrerit. Duis scelerisque, leo at auctor laoreet, ipsum tortor iaculis libero, sit amet feugiat enim purus vel est. Morbi nec risus orci. Praesent malesuada vestibulum eleifend. Sed euismod, nulla id gravida rutrum, lectus massa pulvinar est, nec fermentum lorem est et nunc. Praesent feugiat semper sodales. Donec sit amet nisl commodo, vulputate ligula at, mollis ligula. Nam ullamcorper metus ac orci blandit faucibus."

# ===============================
# insert wordcloud in a mask image
from PIL import Image
mask = np.array(Image.open("2b.png"))
print(mask)

# ubah hitam jadi putih (0 jadi 255)
def transform_format(val):
    if val == 0:
        return 255
    else:
        return val
trans_mask = np.ndarray((mask.shape[0], mask.shape[1]), np.int32)

for i in range(len(mask)):
    trans_mask[i] = list(map(transform_format, mask[i]))

print(trans_mask)

# ==========================
# wordcloud

wordcloud = WordCloud(max_font_size=500, max_words=100, background_color="white", mask=trans_mask, contour_width=3, contour_color='firebrick')
wordcloud.generate(text)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
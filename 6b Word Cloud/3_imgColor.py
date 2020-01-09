# pip install wordcloud

import numpy as np
import pandas as pd
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam vulputate turpis eros, quis tristique elit ultrices sed. Pellentesque commodo leo a molestie viverra. Nunc nisl libero, dictum vel dolor ut, rutrum ultricies nisi. Donec pretium sagittis mauris non suscipit. Quisque tincidunt sagittis dui non elementum. Sed nec erat quis massa dictum pulvinar. Aliquam at euismod mi, eget hendrerit tortor. Quisque a ultricies ante, non mattis sem. Pellentesque sollicitudin feugiat hendrerit. Duis scelerisque, leo at auctor laoreet, ipsum tortor iaculis libero, sit amet feugiat enim purus vel est. Morbi nec risus orci. Praesent malesuada vestibulum eleifend. Sed euismod, nulla id gravida rutrum, lectus massa pulvinar est, nec fermentum lorem est et nunc. Praesent feugiat semper sodales. Donec sit amet nisl commodo, vulputate ligula at, mollis ligula. Nam ullamcorper metus ac orci blandit faucibus."

# create mask
mask = np.array(Image.open("3.png").convert('RGBA'))
wordcloud = WordCloud(background_color="white", mode="RGBA", max_words=1000, mask=mask).generate(text)

# create coloring from image
image_colors = ImageColorGenerator(mask)
plt.figure(figsize=(10,5))

plt.subplot(121)
plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")

plt.subplot(122)
plt.imshow(mask)
plt.axis("off")
plt.show()
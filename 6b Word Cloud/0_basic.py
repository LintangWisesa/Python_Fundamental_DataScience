# pip install wordcloud
# https://www.datacamp.com/community/tutorials/wordcloud-python

# or:
# 1. go here https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud
# 2. find wordcloud & download sesuai os & versi python, misal wordcloud-1.6.0-cp38-cp38-win32.whl
# 3. go to folder download, eksekusi: py -m pip install wordcloud-1.6.0-cp38-cp38-win32.whl

import numpy as np
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam vulputate turpis eros, quis tristique elit ultrices sed. Pellentesque commodo leo a molestie viverra. Nunc nisl libero, dictum vel dolor ut, rutrum ultricies nisi. Donec pretium sagittis mauris non suscipit. Quisque tincidunt sagittis dui non elementum. Sed nec erat quis massa dictum pulvinar. Aliquam at euismod mi, eget hendrerit tortor. Quisque a ultricies ante, non mattis sem. Pellentesque sollicitudin feugiat hendrerit. Duis scelerisque, leo at auctor laoreet, ipsum tortor iaculis libero, sit amet feugiat enim purus vel est. Morbi nec risus orci. Praesent malesuada vestibulum eleifend. Sed euismod, nulla id gravida rutrum, lectus massa pulvinar est, nec fermentum lorem est et nunc. Praesent feugiat semper sodales. Donec sit amet nisl commodo, vulputate ligula at, mollis ligula. Nam ullamcorper metus ac orci blandit faucibus."

# wordcloud = WordCloud().generate(text)
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)

plt.imshow(wordcloud)
# plt.imshow(wordcloud, interpolation="bilinear")  # better
plt.axis("off")
plt.show()

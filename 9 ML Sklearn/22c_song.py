# https://www.kaggle.com/iampedroalz/1000songs

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('song.csv')
df = df[['THEME', 'TITLE', 'ARTIST']]
def kombinasi(i):
    return str(i['THEME']) + '$' + str(i['ARTIST'])
df['x'] = df.apply(kombinasi, axis=1)
print(df.head())

model = CountVectorizer(
    tokenizer = lambda data: data.split('$')
)
kategori = model.fit_transform(df['x'])
print(model.get_feature_names())
print(count_matrix.toarray())
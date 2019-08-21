# Basic Recommendation using "cosinus similarity" / Content based filtering

import pandas as pd
import numpy as np

df = pd.read_csv('22a_movie.csv')
print(df.columns)             # cek daftar feature
print(df.iloc[0])
# print(df.isnull().sum())    # cek total data kosong di tiap feature
df = df.fillna('')          # data kosong akan mjd string kosong ('')
# print(df.isnull().sum())    # cek total data kosong di tiap feature

# =======================================================================
# 1. feature yg dipakai: hanya genre
df = df[['title', 'genres']]
print(df.iloc[0])

# =======================================================================
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()
count_matrix = cv.fit_transform(df['genres'])
print(cv.get_feature_names())   # list of genres
print(count_matrix.toarray())   # jumlah kejadian genre dalam 1 movie

# =======================================================================
from sklearn.metrics.pairwise import cosine_similarity

cosine_sim = cosine_similarity(count_matrix)
print(cosine_sim)

# =======================================================================
# recommendation for user who like 'Avatar'

sukaFilm = 'Avatar'
indexSukaFilm = df[df['title'] == sukaFilm].index.values[0]
print(indexSukaFilm)

# daftar seluruh movie beserta cos similaritynya
similar_movies = list(enumerate(cosine_sim[indexSukaFilm]))
print(similar_movies)   # (index, %kemiripan)

# daftar movie yg similar genre, lalu disortir menurut nilai cos similarity
sorted_similar_movies = sorted(similar_movies, key=lambda x:x[1], reverse=True)
print(sorted_similar_movies[:5])    
# show 5 movie yg mirip: (index, %kemiripan) 
# [(0, 0.9999999999999999), (10, 0.9999999999999999), (14, 0.9999999999999999), (46, 0.9999999999999999), (61, 0.9999999999999999)]  

# menampilkan 5 judul movie yg mirip
for i in sorted_similar_movies[:5]:
    print(df.iloc[i[0]])
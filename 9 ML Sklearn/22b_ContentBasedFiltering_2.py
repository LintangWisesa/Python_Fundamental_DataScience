# Basic Recommendation using "cosinus similarity" / Content based filtering

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('22_movie.csv')
print(df.columns)             # cek daftar feature
print(df.iloc[0])
# print(df.isnull().sum())    # cek total data kosong di tiap feature
df = df.fillna('')          # data kosong akan mjd string kosong ('')
# print(df.isnull().sum())    # cek total data kosong di tiap feature

# =======================================================================
# 2. feature yg akan dipakai: ‘keywords’, ’cast’, ’genres’, ’director’
df = df[['title', 'keywords', 'cast', 'genres', 'director']]
# print(df.head(5).columns)

# buat kolom baru yg berisi string: keyword + cast + genres + director
def combine_features(row):
    return str(row['keywords'])+' '+str(row['cast'])+' '+str(row['genres'])+' '+str(row['director'])

df['combined_features'] = df.apply(combine_features, axis=1)
print(df.iloc[0])

# =======================================================================
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()
# model = CountVectorizer(
#     # ngram_range = (2,2)                 # minimal 2 kata, maksimal 2 kata: hny yg 2 kata yg dihitung
#     tokenizer = lambda x: x.split(' ')    # split kata dg spasi spy "role-playing" terhitung 1 kata
# )
count_matrix = cv.fit_transform(df['combined_features'])
print(cv.get_feature_names())   # list of features
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

# menampilkan 5 judul movie yg mirip
for i in sorted_similar_movies[:5]:
    print(df.iloc[i[0]])
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('22c_song.csv')
df = df[['THEME', 'TITLE', 'ARTIST']]
def kombinasi(i):
    return str(i['THEME']) + '$' + str(i['ARTIST'])
df['x'] = df.apply(kombinasi, axis=1)
# print(df.head())

model = CountVectorizer(
    tokenizer = lambda data: data.split('$')
)
kategori = model.fit_transform(df['x'])
# print(model.get_feature_names())

sukaLagu = 'I Want to Hold Your Hand'
iSukaLagu = df[df['TITLE'] == sukaLagu].index.values[0]
# print(iSukaLagu)
# cos similarity
cosskor = cosine_similarity (kategori)
# print(cosskor)

listLagu = list(enumerate(cosskor[iSukaLagu]))
sortLagu = sorted(listLagu, key=lambda x: x[1], reverse=True)
# print(sortLagu[:5])

for i in sortLagu[:10]:
    if df.iloc[i[0]]['TITLE'] != sukaLagu:
        judul = df.iloc[i[0]]['TITLE']
        artis = df.iloc[i[0]]['ARTIST']
        print(f'{judul} ({artis}) {round(i[1]*100)}%')

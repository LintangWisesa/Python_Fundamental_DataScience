# Basic Recommendation using "cosinus similarity" / Content based filtering

from sklearn.feature_extraction.text import CountVectorizer

# text = [ A , B ]
text = ["London Paris London", "Paris Paris London"]
cv = CountVectorizer()

count_matrix = cv.fit_transform(text)
print(cv.get_feature_names())
print(count_matrix.toarray())

# ['london', 'Paris']
# [[2 1]
#  [1 2]]
# This indicates that the word ‘london’ occurs 2 times in A and 1 time in B. 
# Similarly, the word ‘paris’ occurs 1 time in A and 2 times in B. 

from sklearn.metrics.pairwise import cosine_similarity
similarity_scores = cosine_similarity(count_matrix)
print(similarity_scores)

#      A    B
#  A [[1.  0.8]         A & A 100% sama    A & B 80% sama
#  B [0.8 1. ]]         A & B 80% sama     B & B 80% sama
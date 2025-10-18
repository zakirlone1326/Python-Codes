from sklearn.feature_extraction.text import TfidfVectorizer #TfidfVectorizer convrts text into numeical vectors
from sklearn.metrics.pairwise import cosine_similarity

# Example documents
doc1 = "I am going to campus"
doc2 = "campus is intresting"

# Vectorize the documents using TF-IDF #tf TermFrequency idf inverseDocumentFrequency 
vectorizer = TfidfVectorizer() #now documents are numericals #vectorizer convberts text into nums
tfidf_matrix = vectorizer.fit_transform([doc1, doc2])

# Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

print(f"Cosine Similarity: {cosine_sim[0][0]}")



'''#channel c4A

import numpy as np #NumPy is for numeric operations
def cosinesim(vec1, vec2): #creating function named cosinesim takes two lists and calculates their cosine similarity
    vec1=np.array(vec1) #convert list to numpy aray
    vec2=np.array(vec2)
    numerator=np.dot(vec1, vec2) #dot product like a1*b1 a2*b2 ... an*bn
    v1norm=np.sqrt(sum(vec1**2)) #calculates magnitude(length) of each vector 
    v2norm=np.sqrt(sum(vec2**2))
    c=numerator/(v1norm*v2norm) #numerator is A.B and v1norm*v2nom is ||A||.||B||
    return c
data= [[2, 3, 5,9],
       [3, 5, 1, 7],
       [3,4,8,5]]

#result 1 means very similar 0 means completely different -1 opposite direction
cos=cosinesim(data[0], data[2])
print(cos)'''
       


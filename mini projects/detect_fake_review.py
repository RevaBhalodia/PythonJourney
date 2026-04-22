from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def detect_fake_reviews(reviews):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(reviews)

    similarity_matrix = cosine_similarity(tfidf_matrix)

    suspicious = []
    n = len(reviews)

    for i in range(n):
        for j in range(i+1, n):
            if similarity_matrix[i][j] > 0.8:
                suspicious.append((i, j))

    return suspicious

reviews = [
    "This product is amazing and works perfectly",
    "Amazing product works perfectly",
    "Worst product ever",
    "Totally useless item"
]

print(detect_fake_reviews(reviews))
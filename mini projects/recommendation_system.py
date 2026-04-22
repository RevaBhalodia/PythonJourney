import numpy as np

def recommend(user_ratings, similarity_matrix):
    scores = similarity_matrix.dot(user_ratings)
    return np.argsort(scores)[::-1]

user = np.array([5, 0, 0, 1])
similarity = np.array([
    [1, 0.9, 0.2, 0.4],
    [0.9, 1, 0.3, 0.5],
    [0.2, 0.3, 1, 0.8],
    [0.4, 0.5, 0.8, 1]
])

print(recommend(user, similarity))
# Emotion Detection using Machine Learning

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Step 1: Create a small dataset
data = {
    "text": [
        "I am very happy today",
        "This is so sad",
        "I am angry with you",
        "I feel scared",
        "I love this",
        "I hate this",
        "I am worried",
        "This is amazing",
        "I feel terrible",
        "I am excited"
    ],
    "emotion": [
        "happy", "sad", "angry", "fear",
        "happy", "angry", "fear", "happy",
        "sad", "happy"
    ]
}

df = pd.DataFrame(data)

# Step 2: Convert text into numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["text"])

# Step 3: Labels
y = df["emotion"]

# Step 4: Train model
model = MultinomialNB()
model.fit(X, y)

# Step 5: Take user input
user_input = input("Enter a sentence: ")

# Step 6: Transform input
input_vector = vectorizer.transform([user_input])

# Step 7: Predict emotion
prediction = model.predict(input_vector)

print("Predicted Emotion:", prediction[0])
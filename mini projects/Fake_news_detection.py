# Fake News Detection using Machine Learning

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Step 1: Small dataset
data = {
    "text": [
        "Government passes new education policy",
        "Scientists discover cure for cancer",
        "Aliens landed in India yesterday",
        "Prime Minister addresses nation",
        "You can earn 1 lakh per day from home",
        "New technology improves battery life",
        "Man becomes invisible after experiment",
        "Stock market reaches new high",
        "Click here to win free iPhone",
        "NASA launches new satellite"
    ],
    "label": [
        "real", "real", "fake", "real",
        "fake", "real", "fake", "real",
        "fake", "real"
    ]
}

df = pd.DataFrame(data)

# Step 2: Convert text to numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])

# Step 3: Labels
y = df["label"]

# Step 4: Train model
model = LogisticRegression()
model.fit(X, y)

# Step 5: User input
user_input = input("Enter news headline: ")

# Step 6: Transform input
input_vector = vectorizer.transform([user_input])

# Step 7: Predict
prediction = model.predict(input_vector)

print("Prediction:", prediction[0])
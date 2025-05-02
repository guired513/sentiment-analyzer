import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import os

# Load dataset
df = pd.read_csv("data/reviews.csv")

# Shuffle
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Check balance
print(df['label'].value_counts())

# Split
X_train, X_test, y_train, y_test = train_test_split(
    df["text"], df["label"], test_size=0.2, random_state=42, stratify=df["label"]
)

# Model pipeline
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(lowercase=True, stop_words="english", max_df=0.9)),
    ("clf", LogisticRegression(max_iter=1000))
])

# Train
pipeline.fit(X_train, y_train)

# Accuracy
acc = pipeline.score(X_test, y_test)
print(f"✅ Test Accuracy: {acc:.2f}")

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(pipeline, "models/sentiment_model.pkl")
print("✅ Model saved successfully.")
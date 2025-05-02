import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib



# Load data
df = pd.read_csv("data/reviews.csv")

# Split
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# Create pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])

# Train
pipeline.fit(X_train, y_train)

# Save model
joblib.dump(pipeline, 'models/sentiment_model.pkl')

print("✅ Model trained and saved!")
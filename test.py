import joblib

pipeline = joblib.load("models/sentiment_model.pkl")

while True:
    text = input("Enter a review: ")
    if text.lower() == "exit":
        break
    pred = pipeline.predict([text])[0]
    print(f"Prediction: {pred}")
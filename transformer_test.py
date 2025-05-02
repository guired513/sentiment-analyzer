from transformers import pipeline

# Load pre-trained sentiment-analysis pipeline
classifier = pipeline("sentiment-analysis")

while True:
    text = input("Enter a sentence (or 'exit' to quit): ")
    if text.lower() == "exit":
        break
    result = classifier(text)[0]
    print(f"Label: {result['label']} (Confidence: {result['score']:.2f})")
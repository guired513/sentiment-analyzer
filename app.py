from flask import Flask, request, render_template, jsonify
from transformers import pipeline

app = Flask(__name__)
classifier = pipeline("sentiment-analysis")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None
    if request.method == "POST":
        text = request.form["text"]
        result = classifier(text)[0]
        prediction = result["label"]
        confidence = round(result["score"] * 100, 2)
    return render_template("index.html", prediction=prediction, confidence=confidence)

@app.route("/api/predict", methods=["POST"])
def api_predict():
    try:
        data = request.get_json()
        result = classifier(data["text"])[0]
        return jsonify({
            "prediction": result["label"],
            "confidence": result["score"]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, render_template, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("models/sentiment_model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        text = request.form["text"]
        prediction = model.predict([text])[0]
    return render_template("index.html", prediction=prediction)

@app.route("/api/predict", methods=["POST"])
def api_predict():
    try:
        data = request.get_json()
        text = data["text"]
        prediction = model.predict([text])[0]
        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
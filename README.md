# 🤖 Sentiment Analyzer (Transformers-Powered Web App)

This project is a web-based sentiment analysis application built with **Flask** and powered by a **pre-trained Hugging Face Transformer model**. It classifies user-submitted text as `POSITIVE` or `NEGATIVE` and shows a confidence score. The app is publicly deployed on Render and can handle modern language, slang, and expressive sentences.

---

## 🔗 Live Demo

👉 [Click here to try the app](https://sentiment-analyzer-tfs2.onrender.com)  
(*Replace with your actual Render URL after deployment*)

---

## 🎯 Features

- Uses `distilbert-base-uncased-finetuned-sst-2-english` from Hugging Face 🤗
- Handles modern sentiment expressions and emojis
- Shows confidence level for each prediction
- JSON API endpoint (`/api/predict`) for integrations
- Clean Bootstrap-styled frontend
- Deployed on Render.com

---

## 🚀 Tech Stack

| Layer         | Tool / Library                          |
|---------------|------------------------------------------|
| Backend       | Python, Flask, Gunicorn                 |
| AI Model      | Hugging Face Transformers, DistilBERT   |
| Frontend      | HTML + Bootstrap (Jinja2 template)       |
| Deployment    | Render (Free tier)                      |

---

## 💻 Local Setup Instructions

### ✅ Prerequisites

- Python 3.8+
- pip
- Git
- Virtual environment (optional but recommended)

### 📦 Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/sentiment-analyzer.git
cd sentiment-analyzer

# Setup virtual environment (optional)
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app locally
python app.py
```

Visit: `http://127.0.0.1:5000`

---

## 🔁 JSON API Usage

### 📮 Endpoint: `/api/predict`  
**Method:** `POST`  
**Content-Type:** `application/json`

### 🧪 Example Request
```json
{
  "text": "This movie was absolutely amazing!"
}
```

### ✅ Example Response
```json
{
  "prediction": "POSITIVE",
  "confidence": 0.998
}
```

---

## 📁 Folder Structure

```
sentiment-analyzer/
├── app.py                 # Flask app with transformer model
├── templates/
│   └── index.html         # Frontend UI
├── static/                # Optional CSS or JS files
├── requirements.txt       # Python dependencies
├── Procfile               # For deployment on Render
├── .gitignore
└── README.md
```

---

## 📜 License

This project is licensed under the **MIT License**.  
Free to use, modify, and deploy with attribution.

---

## 🙏 Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [DistilBERT SST-2 Model](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english)
- [Render](https://render.com/) for free cloud hosting
- All open-source contributors and pre-trained model creators

---

## 👨‍💻 Author

**Gui Red**  
Researcher· AI Enthusiast · Bicol University  
🔗 [github.com/guired513](https://github.com/guired513)

# Sentiment Analyzer

The **Sentiment Analyzer** is a web-based application that predicts the sentiment of a given text input. It uses machine learning models to classify the sentiment as positive, negative, or neutral. This project is built with Python, Flask, and Bootstrap for the frontend.

## Features

- Input text or reviews to analyze sentiment.
- Displays the sentiment prediction in a user-friendly interface.
- Lightweight and easy to deploy.

## Project Structure
. ├── app.py # Main Flask application ├── requirements.txt # Python dependencies ├── train.py # Script to train the sentiment analysis model ├── test.py # Script to test the model ├── data/ │ └── reviews.csv # Dataset for training and testing ├── models/ │ └── sentiment_model.pkl # Pre-trained sentiment analysis model ├── templates/ │ └── index.html # HTML template for the web interface


## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/guired513/sentiment-analyzer.git
   cd sentiment-analyzer

2. Install dependencies:

    pip install -r requirements.txt

3. Ensure the dataset (data/reviews.csv) and pre-trained model (models/sentiment_model.pkl) are in their respective directories.

## Usage
1. Start the Flask application:
    python app.py

2. Open your browser and navigate to http://127.0.0.1:5000.
3. Enter text in the input box and click "Predict" to see the sentiment analysis result.

## Training the Model

To train the sentiment analysis model, use the train.py script:
    python [train.py](http://_vscodecontentref_/6)

Ensure the dataset (data/reviews.csv) is available before running the script.

## Testing the Model

To test the model's accuracy, use the test.py script:
    python [test.py](http://_vscodecontentref_/7)

## Technologies Used

- Backend: Flask
- Frontend: HTML, CSS (Bootstrap)
- Machine Learning: Scikit-learn, NLTK
- Data: Pandas, NumPy

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the project.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Bootstrap for the frontend framework.
- Scikit-learn for machine learning tools.
- NLTK for natural language processing.

👤 Author

Gui Red
Researcher, and AI Enthusiast
📍 Bicol University, Philippines
🔗 GitHub
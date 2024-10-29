import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response
import download_nltk_data

app = Flask(__name__)
CORS(app)

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))  # Default to 8000 for local testing
    app.run(debug=True, host='0.0.0.0', port=port)  # Use 0.0.0.0 for public access

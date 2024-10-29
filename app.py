import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response
import download_nltk_data

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the AI Chatbot! Please use the /predict endpoint."

@app.post("/predict")
def predict():
    # Get the message from the request
    data = request.get_json()
    
    # Validate the incoming data
    if not data or 'message' not in data:
        return jsonify({"error": "No message provided."}), 400  # Bad request if no message
    
    text = data['message']
    response = get_response(text)
    
    # Create the response message
    message = {"answer": response}
    return jsonify(message)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))  # Use PORT from environment variable, default to 8000
    app.run(debug=True, host='0.0.0.0', port=port)  # Use 0.0.0.0 for public access

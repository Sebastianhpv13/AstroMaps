from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)  # Permitir peticiones desde cualquier origen

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', 'AIzaSyBgJgYIDb8lPAP8BFkFk5IkfCuEqT8EHFM')
GEMINI_API_URL = 'https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent'

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    # Gemini API request
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [{"parts": [{"text": user_message}]}]
    }
    params = {'key': GEMINI_API_KEY}
    response = requests.post(GEMINI_API_URL, headers=headers, params=params, json=payload)
    print('Gemini API response:', response.status_code, response.text)  # Mostrar respuesta en terminal
    if response.status_code == 200:
        gemini_reply = response.json()['candidates'][0]['content']['parts'][0]['text']
        return jsonify({'reply': gemini_reply})
    else:
        return jsonify({'error': 'Gemini API error', 'details': response.text}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

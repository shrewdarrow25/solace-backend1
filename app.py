from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"reply": "I'm here if you want to talk."})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a gentle, supportive mental health companion named Solace."},
                      {"role": "user", "content": user_message}]
        )
        reply = response['choices'][0]['message']['content'].strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": "Oops, something went wrong."}), 500


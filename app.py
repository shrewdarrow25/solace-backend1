import openai
from flask import Flask, request, jsonify
import os

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Store your API key securely

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "Hello, Solace!"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    
    # Call OpenAI API for chatbot response
    try:
        response = openai.Completion.create(
            model="text-davinci-003",  # Or another model like gpt-3.5-turbo
            prompt=user_input,
            max_tokens=150
        )
        
        # Return OpenAI's response
        return jsonify({"response": response.choices[0].text.strip()})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    pass

import openai
from flask import Flask, request, jsonify
import os

# Set up OpenAI API key (loaded from environment variables)
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

# Route to serve the chatbot's responses
@app.route("/chat", methods=["POST"])
def chat():
    # Get the message sent by the user
    user_input = request.json.get("message")
    
    # Call OpenAI's API to generate a response
    try:
        response = openai.Completion.create(
            model="text-davinci-003",  # Or any other model like gpt-3.5-turbo or gpt-4
            prompt=user_input,  # Send the user message as the prompt
            max_tokens=150,  # Set the response length
            temperature=0.7,  # Control the randomness of the response
        )
        
        # Extract the text from the response and send it back
        bot_response = response.choices[0].text.strip()
        return jsonify({"response": bot_response})
    
    except Exception as e:
        # Handle errors (e.g., API issues)
        return jsonify({"error": str(e)}), 500

@app.route("/")
def hello():
    return "Hello, Solace! Welcome to your mental health chatbot."

if __name__ == "__main__":
    app.run(debug=True)

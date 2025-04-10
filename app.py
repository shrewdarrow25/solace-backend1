from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Solace!"

if __name__ == "__main__":
    # Get the PORT environment variable, default to 5000 if not set
    port = int(os.environ.get("PORT", 5000))
    # Make sure the app listens on all available network interfaces
    app.run(host="0.0.0.0", port=port)

from flask import Flask, request, jsonify
from chatbot.engine import get_response

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    reply = get_response(message)
    return jsonify({"reply": reply})

@app.route("/")
def root():
    return "Chatbot backend running"

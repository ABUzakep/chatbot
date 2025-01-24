from flask import Flask, render_template, request, jsonify
import difflib  # For matching user input with the knowledge base
import json

app = Flask(__name__)

# Load knowledge base from a JSON file
with open("knowledge_base.json", "r") as file:
    knowledge_base = json.load(file)

# Function to find the best response
def find_best_match(user_input):
    matches = difflib.get_close_matches(user_input, knowledge_base.keys(), n=1, cutoff=0.5)
    return knowledge_base[matches[0]] if matches else "Sorry, I didn't understand that."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()
    response = find_best_match(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

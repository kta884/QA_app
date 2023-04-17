import os
from dotenv import load_dotenv

load_dotenv()
print("OpenAI API Key:", os.environ["OPENAI_API_KEY"])

import os
import openai
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/answer", methods=["POST"])
def answer():
    question = request.form.get("question")
    if not question:
        return jsonify({"error": "No question provided"}), 400

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"この質問に日本語で答えてください: {question}",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )
    answer = response.choices[0].text.strip()
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)

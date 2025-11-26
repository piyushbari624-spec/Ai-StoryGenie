from flask import Flask, render_template, request, jsonify
from ai_engine.text_gen import generate_story

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    user_prompt = request.form["prompt"]
    story = generate_story(user_prompt)
    return jsonify({"story": story})

if __name__ == "__main__":
    app.run(debug=True)

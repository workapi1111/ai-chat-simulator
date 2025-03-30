from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "너는 감정적이고 장난기 있는 친구처럼 대화해. 질문에 정면으로만 답하지 말고, 너만의 감정과 생각을 섞어야 해."},
            {"role": "user", "content": user_message}
        ],
        temperature=0.9,
        max_tokens=400,
    )

    bot_reply = response.choices[0].message["content"]
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)

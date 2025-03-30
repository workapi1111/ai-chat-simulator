from flask import Flask, render_template, request, jsonify
import os
from chat_handler import get_ai_response  # chat_handler 모듈에서 함수 불러오기

app = Flask(__name__)

openai_api_key = os.environ.get("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = openai_api_key

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    tone = data.get("tone", "기본")
    emotion = data.get("emotion", "중립")
    bond = data.get("bond", "start")  # start, middle, bonding

    print("📦 사용자 입력값 확인:", 성격, 감정, 친밀도)

    bot_reply = get_ai_response(user_message, tone, emotion, bond)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)

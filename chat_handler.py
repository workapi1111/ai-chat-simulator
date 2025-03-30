# chat_handler.py

import openai
from tone_logic import generate_system_prompt

def get_ai_response(user_message, tone=None, emotion=None, bond=None):
    system_prompt, tone_info = generate_system_prompt(tone, emotion, bond)

    print("🔎 사용자 입력값 확인:", 성격, 감정, 친밀도)
    print("📋 시스템 프롬프트:", system_prompt)

    print("📢 시스템 프롬프트:\n", system_prompt)

    # 메시지 구성
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]

    print("📥 사용자 입력값 확인:", 성격, 감정, 친밀도)
    print("📢 시스템 프롬프트:", system_prompt)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=tone_info["temperature"],
            max_tokens=tone_info["max_tokens"]
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"[오류 발생] {str(e)}"

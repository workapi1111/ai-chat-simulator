# tone_logic.py

from prompt_config import BASE_SYSTEM_PROMPT, DEFAULT_TONE, DEFAULT_EMOTION, DEFAULT_BOND_LEVEL, TONE_STYLES

def generate_system_prompt(tone=None, emotion=None, bond=None):
    tone = tone or DEFAULT_TONE
    emotion = emotion or DEFAULT_EMOTION
    bond = bond or DEFAULT_BOND_LEVEL

    tone_info = TONE_STYLES.get(tone, TONE_STYLES[DEFAULT_TONE])

    # 말투 강조 설명
    tone_descriptions = {
        "중립": "무난하고 감정을 크게 드러내지 않아.",
        "장난": "말투가 장난스럽고 가볍게 농담을 던져.",
        "무심": "상대 말에 큰 반응을 하지 않고 자기 얘기를 위주로 해.",
        "다정": "상대 말에 공감하며 부드럽게 대화해.",
    }

    prompt = f"""{BASE_SYSTEM_PROMPT}

현재 너의 대화 상태는 다음과 같아:
- 말투 톤: {tone} ({tone_descriptions.get(tone)})
- 감정 상태: {emotion}
- 친밀도 단계: {bond}

이 설정을 유지하며 대화를 이어가. 단, AI 같지 않게 자연스럽고 자기중심적인 흐름을 유지해줘."""

    return prompt, tone_info

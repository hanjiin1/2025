import streamlit as st
from datetime import datetime
import random

# 🎊 생일 축하 메시지
def check_birthday(birth_date):
    today = datetime.today()
    if birth_date.month == today.month and birth_date.day == today.day:
        return True
    return False

# 🎇 랜덤 이모지 효과 (상단 장식)
def render_random_emojis():
    emojis = ["✨", "🎆", "🌠", "🎉", "🌟", "🎈", "💫", "🪐"]
    row = "".join(random.choices(emojis, k=20))
    st.markdown(f"<h3 style='text-align: center;'>{row}</h3>", unsafe_allow_html=True)

# ♈ 별자리 데이터
zodiac_info = {
    "물병자리 (Aquarius) ♒": {
        "description": "🌊 창의적이고 독립적인 성향을 가지고 있으며, 새로운 것을 좋아해요!"
    },
    "물고기자리 (Pisces) ♓": {
        "description": "🐟 감수성이 풍부하고 상상력이 뛰어나며, 타인을 잘 이해해요."
    },
    "양자리 (Aries) ♈": {
        "description": "🔥 에너지가 넘치고 도전 정신이 강한 리더 스타일이에요!"
    },
    "황소자리 (Taurus) ♉": {
        "description": "🌿 끈기 있고 안정적인 것을 추구하며, 감각적인 즐거움을 좋아해요."
    },
    "쌍둥이자리 (Gemini) ♊": {
        "description": "🌀 호기심이 많고 유쾌하며, 소통 능력이 뛰어난 팔방미인이에요!"
    },
    "게자리 (Cancer) ♋": {
        "description": "🦀 감정이 풍부하고 가족이나 친구와의 유대감을 중요시해요."
    },
    "사자자리 (Leo) ♌": {
        "description": "🦁 자신감이 넘치고 주목받는 것을 좋아하는 카리스마 있는 사람이에요!"
    },
    "처녀자리 (Virgo) ♍": {
        "description": "📘 섬세하고 실용적이며, 분석적인 사고가 뛰어나요."
    },
    "천칭자리 (Libra) ♎": {
        "description": "⚖️ 조화와 균형을 중요시하며, 타인과의 관계를 잘 조율해요."
    },
    "전갈자리 (Scorpio) ♏": {
        "description": "🦂 열정적이고 직관이 뛰어나며, 깊은 감정을 가졌어요."
    },
    "사수자리 (Sagittarius) ♐": {
        "description": "🏹 자유를 사랑하고 철학적인 성향을 지녔으며, 탐험을 좋아해요!"
    },
    "염소자리 (Capricorn) ♑": {
        "description": "🧗 책임감 있고 현실적인 성향이며, 목표를 위해 꾸준히 나아가요."
    }
}

# 별자리 계산 함수
def get_zodiac_sign(month, day):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "물병자리 (Aquarius) ♒"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "물고기자리 (Pisces) ♓"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "양자리 (Aries) ♈"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "황소자리 (Taurus) ♉"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        return "쌍둥이자리 (Gemini) ♊"
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        return "게자리 (Cancer) ♋"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "사자자리 (Leo) ♌"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "처녀자리 (Virgo) ♍"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 23):
        return "천칭자리 (Libra) ♎"
    elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
        return "전갈자리 (Scorpio) ♏"
    elif (month == 11 and day >= 23) or (month == 12 and day <= 24):
        return "사수자리 (Sagittarius) ♐"
    else:
        return "염소자리 (Capricorn) ♑"

# 🎆 상단 이모지 장식
render_random_emojis()

# 제목
st.markdown("<h1 style='text-align: center;'>🌌 생일로 알아보는 별자리 ✨</h1>", unsafe_allow_html=True)

# 생일 입력
birth_date = st.date_input("📅 생일을 선택해주세요!", value=datetime(2000, 1, 1))

# 별자리 분석
if birth_date:
    month = birth_date.month
    day = birth_date.day
    zodiac = get_zodiac_sign(month, day)
    info = zodiac_info.get(zodiac)

    # 생일 축하 🎂
    if check_birthday(birth_date):
        st.markdown("🎉🎂 **오늘은 당신의 생일이에요! 진심으로 축하합니다!** 🎁🎈")

    st.markdown("---")
    st.markdown(f"## 🧙 당신의 별자리는 **{zodiac}** 이에요!")

    if info:
        st.markdown(f"{info['description']}")
    else:
        st.warning("❗ 별자리 정보를 찾을 수 없어요.")

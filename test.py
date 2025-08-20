import streamlit as st
from datetime import datetime

# 별자리 데이터 (이미지 URL은 예시이며 교체 가능)
zodiac_info = {
    "물병자리 (Aquarius)": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/32/Aquarius.svg",
        "description": "창의적이고 독립적인 성향을 가지고 있으며, 새로운 것을 좋아합니다."
    },
    "물고기자리 (Pisces)": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/65/Pisces.svg",
        "description": "감수성이 풍부하고 상상력이 뛰어나며, 타인을 잘 이해하는 편입니다."
    },
    "양자리 (Aries)": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/5a/Aries.svg",
        "description": "에너지가 넘치고 도전 정신이 강하며, 리더십이 뛰어납니다."
    },
    "황소자리 (Taurus)": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Taurus.svg",
        "description": "끈기 있고 안정적인 것을 추구하며, 감각적인 즐거움을 좋아합니다."
    },
    "쌍둥이자리 (Gemini)": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/8/8a/Gemini.svg",
        "description": "호기심이 많고 유쾌하며, 소통 능력이 뛰어납니다."
    },
    "게자리 (Cancer)": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Cancer.svg",
        "description": "감정이 풍부하고 가족이나 친구와의 유대감을 중요시합니다."
    },
    "사자자리 (Leo)": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/8/8e/Leo.svg",
        "description": "자신감이 넘치고 활발하며, 주목받는 것을 좋아합니다."
    },
    "처녀자리 (Virgo)": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/6b/Virgo.svg",
        "description": "섬세하고 실용적이며, 분석적인 사고를 잘합니다."
    },
    "천칭자리 (Libra)": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/f/f7/Libra.svg",
        "description": "조화와 균형을 중요시하며, 타인과의 관계를 중시합니다."
    },
    "전갈자리 (Scorpio)": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/29/Scorpius.svg",
        "description": "열정적이고 직관이 뛰어나며, 깊은 감정을 가집니다."
    },
    "사수자리 (Sagittarius)": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/8/80/Sagittarius.svg",
        "description": "자유를 사랑하고 철학적인 성향을 지녔으며, 탐험을 좋아합니다."
    },
    "염소자리 (Capricorn)": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/7/76/Capricorn.svg",
        "description": "책임감 있고 현실적인 성향이며, 목표를 위해 노력하는 타입입니다."
    }
}

# 별자리 판별 함수
def get_zodiac_sign(month, day):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "물병자리 (Aquarius)"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "물고기자리 (Pisces)"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "양자리 (Aries)"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "황소자리 (Taurus)"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        return "쌍둥이자리 (Gemini)"
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        return "게자리 (Cancer)"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "사자자리 (Leo)"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "처녀자리 (Virgo)"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 23):
        return "천칭자리 (Libra)"
    elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
        return "전갈자리 (Scorpio)"
    elif (month == 11 and day >= 23) or (month == 12 and day <= 24):
        return "사수자리 (Sagittarius)"
    else:
        return "염소자리 (Capricorn)"

# Streamlit 앱 UI
st.title("🌌 생일로 알아보는 별자리")
birth_date = st.date_input("생일을 선택하세요", value=datetime(2000, 1, 1))

if birth_date:
    month = birth_date.month
    day = birth_date.day
    zodiac = get_zodiac_sign(month, day)
    info = zodiac_info.get(zodiac)

    st.subheader(f"🎉 당신의 별자리는 **{zodiac}**입니다!")

    if info:
        st.image(info["image"], width=200)
        st.markdown(f"**특징:** {info['description']}")
    else:
        st.warning("별자리 정보를 찾을 수 없습니다.")


import streamlit as st
from datetime import datetime

# 별자리 판단 함수
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

# Streamlit 앱
st.title("⭐ 생일로 알아보는 별자리")

birth_date = st.date_input("생일을 선택하세요", value=datetime(2000, 1, 1))

if birth_date:
    month = birth_date.month
    day = birth_date.day
    zodiac = get_zodiac_sign(month, day)
    st.success(f"당신의 별자리는 **{zodiac}**입니다!")


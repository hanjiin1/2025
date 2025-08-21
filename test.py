import streamlit as st
from transformers import pipeline

# 🎯 설정
st.set_page_config(page_title="거짓말 탐지기 🤥", page_icon="🧠")

# 🧠 모델 로드 (감정 분석)
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

analyzer = load_model()

# 📝 앱 타이틀
st.title("🧠 텍스트 기반 거짓말 탐지기")
st.write("🤔 당신이 한 말, 진짜일까요? 거짓일까요? AI가 추측해드립니다!")

# ✍️ 사용자 입력
user_input = st.text_area("💬 분석할 문장을 입력해주세요:", placeholder="예: 나는 매일 아침 5시에 일어나 운동해요.")

# ▶️ 버튼 클릭 시 실행
if st.button("🔍 분석하기"):
    if not user_input.strip():
        st.warning("⚠️ 문장을 입력해주세요!")
    else:
        with st.spinner("AI가 당신의 말을 분석 중입니다... 🧠"):
            result = analyzer(user_input)[0]
            label = result['label']
            score = result['score']

            # 🔎 간단한 로직으로 "거짓일 확률" 추정
            # 부정적이면 거짓일 확률 ↑, 긍정적이면 ↓ (재미용)
            if label == "NEGATIVE":
                lie_prob = round(score * 100)
            else:
                lie_prob = round((1 - score) * 100)

            truth_prob = 100 - lie_prob

            # 🎯 결과 출력
            st.markdown("### 🔍 분석 결과")
            st.write(f"📈 **진실일 확률**: `{truth_prob}%`")
            st.write(f"📉 **거짓일 확률**: `{lie_prob}%`")

            if lie_prob > 70:
                st.error("🤥 이건 왠지 거짓말 같아요!")
            elif lie_prob > 40:
                st.warning("🧐 음... 애매하네요. 믿을지 말지는 당신에게 달렸어요.")
            else:
                st.success("😇 믿을 수 있는 말 같아요!")

            # 📊 디버그용 출력
            st.caption(f"🧪 감정 분석 결과: {label} ({round(score * 100, 2)}%)")


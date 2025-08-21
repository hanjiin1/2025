import streamlit as st
import random

st.set_page_config(page_title="이상형 월드컵", layout="centered")

st.title("🏆 나만의 이상형 월드컵")
st.markdown("비교해서 **가장 마음에 드는 항목**을 골라주세요!")

# 사용자 입력
topic = st.text_input("💬 월드컵 주제를 입력해주세요 (예: 고양이 종류, 라면 브랜드 등)")
user_items = st.text_area("📋 항목을 줄바꿈으로 입력해주세요 (최소 8개 추천)").splitlines()

if len(user_items) < 2:
    st.warning("⚠️ 최소 2개 이상의 항목을 입력해야 해요.")
else:
    if st.button("🚀 월드컵 시작하기"):
        items = random.sample(user_items, len(user_items))  # 항목 랜덤 섞기
        
        def run_round(items):
            winners = []
            st.markdown(f"### 🔄 {len(items)}강!")
            for i in range(0, len(items), 2):
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(items[i], key=f"{items[i]}_left"):
                        winners.append(items[i])
                with col2:
                    if st.button(items[i+1], key=f"{items[i+1]}_right"):
                        winners.append(items[i+1])
            return winners

        round_items = items
        while len(round_items) > 1:
            round_items = run_round(round_items)
            st.divider()

        if len(round_items) == 1:
            st.success(f"🏆 최종 우승: **{round_items[0]}** 🎉")

import streamlit as st
import random

st.set_page_config(page_title="📚 단어 암기 퀴즈", layout="centered")

st.title("📘 단어 암기 퀴즈 앱")
st.markdown("🧠 **외워야 할 단어를 입력하면 자동으로 퀴즈를 만들어줄게요!**")

# 입력받기
st.subheader("✍️ 단어 리스트 입력")
st.markdown("👉 아래 형식으로 입력해 주세요: `단어 : 뜻` (한 줄에 하나씩)")
user_input = st.text_area("예시:\nphotosynthesis : 광합성\nmitochondria : 미토콘드리아", height=200)

if user_input:
    raw_list = user_input.strip().split("\n")
    word_dict = {}
    for line in raw_list:
        if ":" in line:
            word, meaning = line.split(":", 1)
            word_dict[word.strip()] = meaning.strip()
    
    if len(word_dict) < 1:
        st.error("❌ 단어를 제대로 입력해 주세요! (예: apple : 사과)")
    else:
        st.success(f"✅ {len(word_dict)}개의 단어가 등록되었어요. 퀴즈를 시작해볼까요?")
        
        # 퀴즈 시작
        if st.button("🚀 퀴즈 시작하기"):
            score = 0
            total = len(word_dict)
            quiz_words = list(word_dict.items())
            random.shuffle(quiz_words)
            
            st.subheader("📋 퀴즈 문제")

            for i, (word, meaning) in enumerate(quiz_words):
                user_answer = st.text_input(f"{i+1}. ❓ `{word}` 의 뜻은?", key=f"q_{i}")
                if user_answer:
                    if user_answer.strip() == meaning:
                        st.success("✅ 정답!")
                        score += 1
                    else:
                        st.error(f"❌ 오답! 정답은 👉 `{meaning}`")
            
            st.markdown("---")
            st.markdown(f"🎉 **최종 점수: {score} / {total}**")
else:
    st.info("📝 먼저 단어 리스트를 입력해 주세요!")

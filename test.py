import streamlit as st
import random

st.set_page_config(page_title="📚 단어 암기 퀴즈", layout="centered")

st.title("📘✨ 단어 암기 퀴즈 앱 ✨📘")

# 세션 상태 초기화
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "score" not in st.session_state:
    st.session_state.score = 0
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "quiz_words" not in st.session_state:
    st.session_state.quiz_words = []
if "message" not in st.session_state:
    st.session_state.message = ""
if "show_feedback" not in st.session_state:
    st.session_state.show_feedback = False

st.subheader("✍️ 단어 리스트 입력 ✍️")
user_input = st.text_area(
    "예시:\nphotosynthesis : 광합성 🌿\nmitochondria : 미토콘드리아 🔋",
    height=200,
)

def start_quiz():
    raw_list = user_input.strip().split("\n")
    word_dict = {}
    for line in raw_list:
        if ":" in line:
            word, meaning = line.split(":", 1)
            word_dict[word.strip()] = meaning.strip()
    if len(word_dict) < 1:
        st.error("❌ 단어를 제대로 입력해 주세요! (예: apple : 사과 🍎)")
        return False
    else:
        st.session_state.quiz_words = list(word_dict.items())
        random.shuffle(st.session_state.quiz_words)
        st.session_state.score = 0
        st.session_state.current_index = 0
        st.session_state.quiz_started = True
        st.session_state.message = ""
        st.session_state.show_feedback = False
        return True

if not st.session_state.quiz_started:
    if user_input:
        if st.button("🚀 퀴즈 시작하기!"):
            started = start_quiz()
            if not started:
                st.stop()
    else:
        st.info("📝 먼저 단어 리스트를 입력해 주세요! ✏️")

else:
    total = len(st.session_state.quiz_words)

    if st.session_state.current_index >= total:
        st.balloons()
        st.markdown("---")
        st.success(f"🎉 축하합니다! 퀴즈 완료! 🏆 최종 점수: **{st.session_state.score} / {total}** 🎯")
        if st.button("🔄 다시 도전하기!"):
            st.session_state.quiz_started = False
            st.session_state.score = 0
            st.session_state.current_index = 0
            st.session_state.quiz_words = []
            st.session_state.message = ""
            st.session_state.show_feedback = False

    else:
        current_word, current_meaning = st.session_state.quiz_words[st.session_state.current_index]
        st.subheader(f"📋 문제 {st.session_state.current_index + 1} / {total} 📝")
        st.write(f"❓ `{current_word}` 의 뜻은 무엇일까요? 🤔")

        if not st.session_state.show_feedback:
            with st.form(key="answer_form"):
                user_answer = st.text_input(
                    "여기에 답을 입력하세요 ✍️", key="answer_input"
                )
                submit = st.form_submit_button("✅ 제출하기")

            if submit:
                if user_answer.strip() == "":
                    st.warning("⚠️ 답을 입력해주세요!")
                else:
                    if user_answer.strip() == current_meaning:
                        st.session_state.message = "🎉 정답이에요! 👏👏👏"
                        st.session_state.score += 1
                    else:
                        st.session_state.message = f"❌ 아쉽네요! 정답은 👉 `{current_meaning}` 입니다! 💡"
                    st.session_state.show_feedback = True
                    st.session_state.user_answer = user_answer.strip()
                    st.experimental_rerun()

        else:
            st.info(st.session_state.message)
            if st.button("➡️ 다음 문제"):
                st.session_state.current_index += 1
                st.session_state.show_feedback = False
                st.session_state.message = ""
                st.experimental_rerun()

        st.markdown(f"📊 현재 점수: **{st.session_state.score}** / {total} 🎯")

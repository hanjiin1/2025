import streamlit as st

# 🌟 MBTI별 직업 추천 데이터
mbti_jobs = {
    "ISTJ": {
        "desc": "🛡️ 신중하고 책임감 있는 현실주의자!",
        "jobs": ["📊 회계사", "⚖️ 변호사", "🪖 군인", "📋 관리자"]
    },
    "ISFJ": {
        "desc": "💖 헌신적이고 세심한 수호자!",
        "jobs": ["💉 간호사", "👩‍🏫 교사", "🤝 사회복지사", "🖋️ 비서"]
    },
    "INFJ": {
        "desc": "🌌 통찰력과 이상을 추구하는 조언자!",
        "jobs": ["🧠 심리상담사", "✍️ 작가", "📚 교사", "🔬 연구원"]
    },
    "INTJ": {
        "desc": "♟️ 전략적이고 창의적인 마스터마인드!",
        "jobs": ["📈 전략가", "🔭 과학자", "⚙️ 엔지니어", "📊 데이터 분석가"]
    },
    "ISTP": {
        "desc": "🛠️ 분석적이고 도전적인 문제 해결사!",
        "jobs": ["🔧 기술자", "✈️ 조종사", "🕵️ 수사관", "💻 프로그래머"]
    },
    "ISFP": {
        "desc": "🎨 감성적이고 온화한 예술가!",
        "jobs": ["🖌️ 디자이너", "👩‍🍳 요리사", "🧘 물리치료사", "🎭 예술가"]
    },
    "INFP": {
        "desc": "🌱 이상적이고 창의적인 중재자!",
        "jobs": ["✍️ 작가", "🧠 상담사", "📖 교사", "🎨 예술가"]
    },
    "INTP": {
        "desc": "🧪 지적 호기심이 넘치는 사색가!",
        "jobs": ["🔬 연구원", "💡 발명가", "💻 프로그래머", "📊 분석가"]
    },
    "ESTP": {
        "desc": "⚡ 모험적이고 현실적인 활동가!",
        "jobs": ["💼 세일즈", "👮 경찰", "🏅 운동선수", "🚀 기업가"]
    },
    "ESFP": {
        "desc": "🌈 에너지가 넘치는 분위기 메이커!",
        "jobs": ["🎬 배우", "🎤 가수", "🎉 이벤트 플래너", "🗺️ 관광 가이드"]
    },
    "ENFP": {
        "desc": "🔥 열정적이고 창의적인 아이디어 뱅크!",
        "jobs": ["📢 마케터", "✍️ 작가", "🎤 강연가", "🗂️ 기획자"]
    },
    "ENTP": {
        "desc": "💡 재치 넘치고 창의적인 혁신가!",
        "jobs": ["🚀 벤처기업가", "🏛️ 정치가", "📰 기자", "📢 마케터"]
    },
    "ESTJ": {
        "desc": "📏 체계적이고 실용적인 관리자!",
        "jobs": ["🏢 경영자", "🪖 군인", "📋 프로젝트 매니저", "🏛️ 행정가"]
    },
    "ESFJ": {
        "desc": "🤗 사교적이고 따뜻한 돌봄 전문가!",
        "jobs": ["👩‍🏫 교사", "💉 간호사", "🧑‍💼 인사담당자", "🤝 사회복지사"]
    },
    "ENFJ": {
        "desc": "🌟 타인을 이끄는 따뜻한 리더!",
        "jobs": ["👑 리더", "📚 교사", "🧠 상담사", "📣 홍보담당자"]
    },
    "ENTJ": {
        "desc": "🏆 목표 지향적이고 결단력 있는 지도자!",
        "jobs": ["💼 CEO", "⚖️ 변호사", "📊 경영 컨설턴트", "📋 프로젝트 리더"]
    }
}

# 🎨 페이지 설정
st.set_page_config(page_title="MBTI 직업 추천 💼", page_icon="🌟", layout="centered")

# 🌈 헤더
st.markdown("<h1 style='text-align: center; color: #ff69b4;'>💼✨ MBTI 기반 화려한 직업 추천 🌈</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>당신의 성격에 꼭 맞는 직업을 찾아드릴게요 💖</p>", unsafe_allow_html=True)

# 🧩 MBTI 선택
mbti = st.selectbox("🔍 당신의 MBTI를 선택하세요", list(mbti_jobs.keys()))

# 🎯 결과 출력
if mbti:
    st.markdown(f"<h2 style='color:#ffa500;'>📌 {mbti} 유형 분석</h2>", unsafe_allow_html=True)
    st.write(mbti_jobs[mbti]["desc"])
    st.markdown("### 🌟 추천 직업 리스트 🌟")
    for job in mbti_jobs[mbti]["jobs"]:
        st.markdown(f"- {job}")

    # 💡 팁
    st.markdown("---")
    st.markdown("💡 **Tip:** 이 직업들 중 관심 있는 분야를 찾아보고, 필요한 공부와 경험을 차근차근 쌓아가세요! 🚀")

# 🎉 하단 장식
st.markdown("<p style='text-align:center; font-size:14px;'>✨ Made with ❤️ using Streamlit ✨</p>", unsafe_allow_html=True)

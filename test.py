import streamlit as st
from datetime import datetime

# 🌌 커스텀 CSS로 배경 이미지 설정
def set_background():
    st.markdown(
        """
        <style>
        body {
            background-image: url('https://images.unsplash.com/photo-1503264116251-35a269479413?auto=format&fit=crop&w=1950&q=80');
            background-size: cover;
            background-attachment: fixed;
        }
        .main {
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# 🌟 별자리

  


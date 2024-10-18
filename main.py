import streamlit as st

st.set_page_config(page_title="Login Page", page_icon="🔒", layout="centered")

st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .title {
        color: #ff6347;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
    }
    .emoji {
        font-size: 60px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown('<div class="emoji">🐝 🐝</div>', unsafe_allow_html=True)
st.markdown('<div class="title">안녕</div>', unsafe_allow_html=True)

username = st.text_input("👤 Username", placeholder="아이디를 입력해주세요")
password = st.text_input("🔒 Password", type="password", placeholder="패스워드를 입력해주세요")

if st.button("로그인"):
    if username == "admin" and password == "password":
        st.success(f"🎉 Welcome {username}! 🎉")
    else:
        st.error("❌ 유저 정보가 일치하지 않습니다. 다시 시도해주세요. ❌")

st.markdown("계정이 없으신가요? [회원가입](signup.py)")

import streamlit as st

st.set_page_config(page_title="회원가입", page_icon="📝", layout="centered")

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
st.markdown('<div class="title">회원가입</div>', unsafe_allow_html=True)

existing_users = ["admin", "user1", "user2"]

username = st.text_input("👤 아이디", placeholder="사용할 아이디를 입력해주세요")
password = st.text_input("🔒 비밀번호", type="password", placeholder="비밀번호를 입력해주세요")
confirm_password = st.text_input("🔒 비밀번호 확인", type="password", placeholder="비밀번호를 다시 입력해주세요")

if st.button("회원가입"):
    if not username or not password or not confirm_password:
        st.error("모든 필드를 입력해주세요.")
    elif username in existing_users:
        st.error(f"'{username}'는 이미 사용 중인 아이디입니다. 다른 아이디를 선택해주세요.")
    elif password != confirm_password:
        st.error("비밀번호가 일치하지 않습니다.")
    else:
        st.success(f"🎉 '{username}'님, 회원가입이 완료되었습니다!")
        existing_users.append(username)

st.markdown("이미 계정이 있으신가요? [로그인](main)")
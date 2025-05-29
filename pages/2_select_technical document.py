import streamlit as st

st.title("📌 기술적 특성 선택지")

# 질문
questions = {
    "q1": "1. 전기를 사용하나요?",
    "q2": "2. 인체에 접촉 또는 주입되나요?",
    "q3": "3. 방사선을 이용하거나 노출되나요?",
    "q4": "4. 전자파 안전성이 요구되나요?",
    "q5": "5. 혈액, 체액 또는 약물과 접촉하나요?",
}

# 답변
answers = {}
for key, question in questions.items():
    answers[key] = st.radio(question, ("Yes", "No"))

# 페이지 이동
if st.button("다음 단계로 이동"):
    for key, value in answers.items():
        st.session_state[key] = value
    st.switch_page("pages/3_output_document.py")

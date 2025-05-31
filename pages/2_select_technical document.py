import streamlit as st

st.title("📌 기술적 특성 선택지")

category = st.session_state.get('분류', '정보없음')
ivd = category in ["I", "J", "K", "L", "M", "N", "O", "P"]

# 질문_기본
questions = {
    "q1": "1. 전기를 사용하나요?",
    "q2": "2. 인체에 접촉 또는 주입되나요?",
    "q3": "3. 방사선을 이용하거나 노출되나요?",
    "q4": "4. 전자파 안전성이 요구되나요?",
    "q5": "5. 혈액, 체액 또는 약물과 접촉하나요?",
}

# 답변
answers ={}

if ivd:
    ivd_type = st.radio("체외진단의료기기의 종류를 선택하세요:", ["체외진단시약", "체외진단장비"])
    st.session_state["ivd_type"] = ivd_type
    
    if ivd_type == "체외진단시약":
        st.success("체외진단시약은 추가 질문이 없습니다. 다음 페이지로 이동하세요")
        st.session_state["q1_IVD"] = "N/A"
        st.session_state["q2_IVD"] = "N/A"
        st.session_state["q3_IVD"] = "N/A"

    elif ivd_type == "체외진단장비":
        st.subheader("체외진단장비 관련 추가 질문")
        q1_IVD = st.radio("1. 전기, 전자회로를 사용하나요?", ["Yes", "No"])
        q2_IVD = st.radio("2. 방사선을 이용하거나 노출되나요?", ["Yes", "No"])

        st.session_state["q1_IVD"] = q1_IVD
        st.session_state["q2_IVD"] = q2_IVD
        st.session_state["q3_IVD"] = q1_IVD
else:
    for key, question in questions.items():
        answers[key] = st.radio(question, ("Yes", "No"))

# 페이지 이동
if st.button("다음 단계로 이동"):
    for key, value in answers.items():
        st.session_state[key] = value
    st.switch_page("pages/3_output_document.py")
